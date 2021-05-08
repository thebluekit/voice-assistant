from model.sentence.converter import SentenceConverter
from model.database.node import Node
from model.skill import constants

from random import sample

SCRIPTS_FOLDER = constants.SCRIPTS_FOLDER


class MessageRecognizer:
    ERROR_MESSAGE = 'NOT_RECOGNIZED'

    def __init__(self, cypher_manager):
        self.sc = SentenceConverter()
        self.cypher_manager = cypher_manager

    def __get_cypher_nodes(self, words):
        nodes = []
        for word in words:
            node = Node(node_params={"name": word}, node_type='word')
            cypher_nodes = self.cypher_manager.get_nodes_by_name(node)
            nodes.append(cypher_nodes[0])
        return nodes

    @staticmethod
    def __get_script(cypher_nodes):
        params = {
            'action': set(),
            'entity': set(),
            'context': set()
        }
        for i in range(len(cypher_nodes)):
            action = cypher_nodes[i].node_params['action']
            entity = cypher_nodes[i].node_params['entity']
            context = cypher_nodes[i].node_params['context']

            params["action"].update(action)
            params["entity"].update(entity)
            params["context"].update(context)

        scripts_name = params["action"] & params["entity"] & params["context"]
        script_name = sample(scripts_name, 1)[0]
        return script_name

    def __check_relations(self, cypher_nodes):
        for i in range(len(cypher_nodes)-1):
            is_relation = self.cypher_manager.check_relation(cypher_nodes[i], cypher_nodes[i + 1])
            if not is_relation:
                return False
        return True

    @staticmethod
    def __get_full_script_path(script_name):
        return SCRIPTS_FOLDER + script_name + '.py'

    def recognize_script(self, message):
        words = self.sc.get_words_from_sentence(message)
        cypher_nodes = self.__get_cypher_nodes(words)

        if len(words) != len(cypher_nodes):
            return self.ERROR_MESSAGE

        relations = self.__check_relations(cypher_nodes)
        if not relations:
            return self.ERROR_MESSAGE

        script_name = self.__get_script(cypher_nodes)
        script_path = self.__get_full_script_path(script_name)

        return script_path
