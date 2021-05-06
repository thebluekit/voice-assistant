from model.sentence_upload.sentence_converter import SentenceConverter


class SentenceManager:
    sentence_converter = SentenceConverter()

    def __init__(self, cypher_manager):
        self.cypher_manager = cypher_manager

    def get_words_from_sentence(self, sentence):
        return self.sentence_converter.get_words_from_sentence(sentence)

    def upload_sentence(self, sentence, script_name, action, entity, context):
        words = self.get_words_from_sentence(sentence)
        nodes = self.sentence_converter.get_nodes_from_words(words, script_name, action, entity, context)

        nodes[0] = self.__upload_word(nodes[0])
        for i in range(1, len(nodes)):
            nodes[i] = self.__upload_word(nodes[i])
            self.__upload_relation(nodes[i-1], nodes[i])
        return 0

    def __upload_word(self, node):
        founded_nodes = self.cypher_manager.get_nodes_by_name(node)
        if len(founded_nodes) > 0:
            node = self.cypher_manager.update_node(founded_nodes[0], node)
        else:
            node = self.cypher_manager.create_node(node)
        return node

    def __upload_relation(self, node_1, node_2):
        current_node_relations = self.cypher_manager.get_relations(node_2, 'from')

        if len(current_node_relations) == 0:
            self.cypher_manager.create_relation(node_1, node_2, 'goto')
        else:
            real_relation_exist = False
            for relation in current_node_relations:
                if relation['node'].node_id == node_1.node_id:
                    real_relation_exist = True
            if not real_relation_exist:
                self.cypher_manager.create_relation(node_1, node_2, 'goto')

