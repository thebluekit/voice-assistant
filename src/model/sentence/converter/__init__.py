from model.database.node import Node

import pymorphy2
import re


class SentenceConverter:
    node_type = "word"

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    @staticmethod
    def __get_pure_sentence(sentence: str):
        sentence = sentence.lower()
        sentence = re.sub(r'[^A-zА-я0-9 ]', '', sentence)
        return sentence

    @staticmethod
    def __sentence_to_list(sentence: str):
        return sentence.split(' ')

    def get_words_normal_form(self, words: list):
        normal_words = []

        for word in words:
            p = self.morph.parse(word)[0]
            normal_words.append(p.normal_form)
        return normal_words

    def get_words_from_sentence(self, sentence: str):
        pure_sentence = self.__get_pure_sentence(sentence)
        words = self.__sentence_to_list(pure_sentence)
        normal_words = self.get_words_normal_form(words)
        return normal_words

    @staticmethod
    def get_words_from_activators(activators):
        # print(activators)
        # words = activators.split(',')
        words = activators
        resulted_words = []
        for i in range(len(words)):
            words[i] = words[i].replace(" ", "")
            if len(words[i]) != 0:
                resulted_words.append(words[i])
        return resulted_words

    def get_pure_word(self, word: str):
        word = word.lower()
        word = re.sub(r'[^A-zА-я0-9 ]', '', word)
        p = self.morph.parse(word)[0]
        p = p.normal_form
        return p

    def get_nodes_from_words(self, words: list, script_name: str, action: list, entity: list, context: list):
        nodes = []
        for word in words:
            node_params = {'name': word, 'action': [], "entity": [], "context": []}
            if word in action:
                node_params['action'].append(script_name)
            if word in entity:
                node_params['entity'].append(script_name)
            if word in context:
                node_params['context'].append(script_name)
            node = Node(self.node_type, node_params)
            nodes.append(node)
        return nodes
