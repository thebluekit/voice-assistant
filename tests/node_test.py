import pytest

from model.database.node import Node
from model.database.node import nodeError


class TestNode:
    def test_correct_input(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == node_id

    def test_correct_input_with_empty_params(self):
        node_type = "test_type"
        node_params = {}
        node = Node(node_type, node_params)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == -1

    def test_correct_input_without_id(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node = Node(node_type, node_params)

        assert node.node_params == node_params \
               and node.node_type == node_type \
               and node.node_id == -1

    def test_incorrect_node_type(self):
        node_type = 1
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        with pytest.raises(nodeError.CreateError):
            Node(node_type, node_params)

    def test_incorrect_node_params(self):
        node_type = "test_type"
        node_params = ["some_param1", "some_param2"]
        with pytest.raises(nodeError.CreateError):
            Node(node_type, node_params)

    def test_correct_publish_node_type(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        assert node.publish("node_type") == node_type

    def test_correct_publish_node_params_single(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        published_node_params = "{param1: 'param1_test'}"

        assert node.publish("node_params") == published_node_params

    def test_correct_publish_node_params_multi(self):
        node_type = "test_type"
        node_params = {'param1': 'param1_test', 'param2': 'param2_test'}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        published_node_params = "{param1: 'param1_test', param2: 'param2_test'}"

        assert node.publish("node_params") == published_node_params

    def test_correct_publish_node_params_empty(self):
        node_type = "test_type"
        node_params = {}
        node_id = 1
        node = Node(node_type, node_params, node_id)

        published_node_params = "{}"

        assert node.publish("node_params") == published_node_params
