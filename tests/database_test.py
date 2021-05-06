from model.database.cypher import CypherManager
from model.sentence_upload import SentenceManager
from model.database.node import Node
import pytest


class Graph:
    def __init__(self):
        pass

    def run(self, query):
        return query


class CM(CypherManager):
    def __init__(self):
        self.graph = Graph()

    def __connection(self, ip_address: str = None, password: str = None):
        graph = Graph()
        return graph


@pytest.fixture(scope='module')
def data_builder():
    cm = CypherManager()
    cm.delete_all_nodes()

    sen_1 = "Включи, свет в ванной!!!!!"
    action_1 = ['включить']
    entity_1 = ['свет']
    context_1 = ['ванная']

    sen_2 = "Переключи свет в ванной комнате"
    action_2 = ['переключить']
    entity_2 = ['свет']
    context_2 = ['ванная', 'комната']

    db_manager = SentenceManager(cm)
    db_manager.upload_sentence(sen_1, "test_func", action_1, entity_1, context_1)
    db_manager.upload_sentence(sen_2, "test_func2", action_2, entity_2, context_2)

    return cm


class TestDataBase:
    def test_update_node_1(self):
        cm = CM("test1", "test2")

        node_1_type = "test_type"
        node_1_params = {'param1': ["1", "2"]}
        node_1_id = 1
        node_1 = Node(node_1_type, node_1_params, node_1_id)

        node_2_type = "test_type"
        node_2_params = {'param1': ["3", "4"], 'param2': 'param2_test'}
        node_2_id = 1
        node_2 = Node(node_2_type, node_2_params, node_2_id)

        merged_params = {'param1': ['1', '2', '3', '4'], 'param2': 'param2_test'}

        merged_node = cm.update_node(node_1, node_2)
        assert merged_node.node_params == merged_params

    def test_update_node_2(self):
        cm = CM("test1", "test2")

        node_1_type = "test_type"
        node_1_params = {'param1': ["1", "2"]}
        node_1_id = 1
        node_1 = Node(node_1_type, node_1_params, node_1_id)

        node_2_type = "test_type"
        node_2_params = {'param1': "1", 'param2': 'param2_test'}
        node_2_id = 1
        node_2 = Node(node_2_type, node_2_params, node_2_id)

        merged_params = {'param1': "1", 'param2': 'param2_test'}

        merged_node = cm.update_node(node_1, node_2)
        assert merged_node.node_params == merged_params

    def test_update_node_3(self):
        cm = CM("test1", "test2")

        node_1_type = "test_type"
        node_1_params = {}
        node_1_id = 1
        node_1 = Node(node_1_type, node_1_params, node_1_id)

        node_2_type = "test_type"
        node_2_params = {'param1': "test", 'param2': 'param2_test'}
        node_2_id = 1
        node_2 = Node(node_2_type, node_2_params, node_2_id)

        merged_params = {'param1': "test", 'param2': 'param2_test'}

        merged_node = cm.update_node(node_1, node_2)
        assert merged_node.node_params == merged_params

    def test_data(self):
        cm = data_builder()
        assert len(cm.get_all_nodes()) == 6

    def test_create_node(self):
        node_1_type = "test_type"
        node_1_params = {'param1': ["1", "2"], "name": "test"}
        node_1 = Node(node_1_type, node_1_params)
        cm = data_builder()
        cm.create_node(node_1)
        assert node_1.node_id != -1
