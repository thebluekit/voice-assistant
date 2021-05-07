import py2neo
from string import Template
from dotenv import load_dotenv
import os

from model.database.cypher import cypherError
from model.database.node import Node


class CypherManager:
    graph = None

    def __init__(self, ip_address: str = None, password: str = None):
        self.graph = self.__connection(ip_address, password)

    def __connection(self, ip_address: str = None, password: str = None):
        expected_type = 'str'

        if ip_address is None or password is None:
            ip_address, password = self.__load_from_dotenv()

        if type(ip_address) is not str:
            given_type = str(type(ip_address).__name__)
            raise cypherError.ConnectTypeError("database link type", expected_type, given_type)
        if type(password) is not str:
            given_type = str(type(password).__name__)
            raise cypherError.ConnectTypeError("database password type", expected_type, given_type)

        try:
            graph = py2neo.Graph(ip_address, password=password)
            return graph
        # except py2neo.database.work.ClientError:
        #     raise cypherError.LoginError() from None
        except AttributeError:
            raise cypherError.ConnectionProfileError()
        except Exception as ex:
            if 'Cannot open connection to' in str(ex.args):
                raise cypherError.ConnectError() from None
            else:
                raise ex

    @staticmethod
    def __load_from_dotenv():
        load_dotenv()
        db_link = os.getenv("DB_LINK")
        db_password = os.getenv("DB_PASSWORD")
        return db_link, db_password

    @staticmethod
    def __cypher_to_node(cypher_node: dict):
        node_info = cypher_node['n']
        node_id = int(cypher_node['ID(n)'])
        node_type = str(node_info.labels)[1:]
        node_params = dict(node_info)

        node = Node(node_type, node_params, node_id)
        return node

    def create_node(self, node: Node):
        if type(node) != Node:
            raise cypherError.NodeTypeError()

        node_type = node.publish('node_type')
        node_params = node.publish('node_params')

        query_template = Template("CREATE (n: $node_type $node_params) RETURN n, ID(n)")
        query = query_template.substitute(node_type=node_type, node_params=node_params)
        query_result = self.graph.run(query).data()[0]
        node.node_id = int(query_result['ID(n)'])
        node_tmp = Node(node.node_type, node.node_params, node.node_id)
        return node_tmp

    def delete_node(self, node: Node):
        if type(node) != Node:
            raise cypherError.NodeTypeError()
        query_template = Template("MATCH (n) WHERE id(n)=$node_id DELETE n")
        query = query_template.substitute(node_id=node.node_id)
        self.graph.run(query)
        return 0

    def get_nodes_by_name(self, node: Node):
        if type(node) != Node:
            raise cypherError.NodeTypeError()
        query_template = Template("MATCH (n) WHERE n.name='$node_name' return n, ID(n)")
        node_name = node.node_params["name"]

        query = query_template.substitute(node_name=node_name)
        query_result = self.graph.run(query).data()

        nodes = []
        for node in query_result:
            nodes.append(self.__cypher_to_node(node))
        return nodes

    def update_node(self, old_node: Node, new_node: Node):
        old_params = old_node.node_params
        new_params = new_node.node_params

        merged_type = new_node.node_type
        merged_params = {}

        for param in new_params:
            if param in old_params:
                if type(new_params[param]) == list:
                    merged_params[param] = old_params[param] + new_params[param]
                else:
                    merged_params[param] = new_params[param]
            else:
                merged_params[param] = new_params[param]

        merged_node = Node(merged_type, merged_params, old_node.node_id)

        node_id = old_node.node_id
        for param in old_params:
            query_template = Template("MATCH (n) WHERE id(n)=$node_id SET n.$param = NULL RETURN n")
            query = query_template.substitute(node_id=node_id, param=param)
            self.graph.run(query)

        for param in merged_params:
            value = merged_params[param]
            if type(value) == str:
                value = "'" + value + "'"

            query_template = Template("MATCH (n) WHERE id(n)=$node_id SET n.$param = $value RETURN n")
            query = query_template.substitute(node_id=node_id, param=param, value=value)
            self.graph.run(query)

        return merged_node

    def create_relation(self, node_1: Node, node_2: Node, relation):
        if type(node_1) != Node or type(node_2) != Node:
            raise cypherError.NodeTypeError()
        query_template = Template("MATCH (a:$node_1_type),(b:$node_2_type) WHERE ID(a) = $node_1_id AND ID(b) = $node_2_id CREATE (a)-[r:$relation]->(b) RETURN type(r)")
        query = query_template.substitute(node_1_type=node_1.node_type,
                                          node_2_type=node_2.node_type,
                                          node_1_id=node_1.node_id,
                                          node_2_id=node_2.node_id,
                                          relation=relation)
        self.graph.run(query)
        return 0

    def get_relations(self, node: Node, direction: str):
        if type(node) != Node:
            raise cypherError.NodeTypeError()
        if type(direction) != str:
            raise cypherError.RelationDirectionError()
        if direction != 'from' and direction != 'to':
            raise cypherError.RelationDirectionError()

        if direction == 'from':
            query_template = Template("MATCH (n)-[r]->(n1) WHERE id(n1)=$node_id  RETURN r, n, ID(n)")
        else:
            query_template = Template("MATCH (n1)-[r]->(n) WHERE id(n1)=$node_id  RETURN r, n, ID(n)")
        query = query_template.substitute(node_id=node.node_id)
        query_results = self.graph.run(query).data()
        nodes = []
        for query_result in query_results:
            relation_type = type(query_result['r']).__name__
            node = self.__cypher_to_node(query_result)
            nodes.append({"node": node, "relation_type": relation_type})
        return nodes

    def get_all_nodes(self, limit: int = -1):
        query = "MATCH (n) RETURN n, ID(n)"
        if limit > 0:
            query += 'LIMIT' + str(limit)

        query_result = self.graph.run(query).data()
        nodes = []
        for node in query_result:
            nodes.append(self.__cypher_to_node(node))
        return nodes

    def delete_all_nodes(self):
        query = "MATCH (n) DETACH DELETE n"
        self.graph.run(query)
        return 0
