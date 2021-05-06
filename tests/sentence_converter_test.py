from model.sentence_upload.sentence_converter import SentenceConverter

import pytest

from model.database.node import Node
from model.database.node import nodeError


class TestSentenceConverter:
    def test_pure_sentence_1(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == node_id

    def test_pure_sentence_2(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == node_id

    def test_pure_sentence_3(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == node_id