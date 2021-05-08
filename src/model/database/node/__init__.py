from model.database.node import nodeError


class Node(object):
    node_type = None
    node_id = -1
    node_params = {}

    def __init__(self, node_type: str, node_params: dict, node_id: int = -1):
        if self.__values_checker(node_type, node_params) == 0:
            self.node_type = node_type
            self.node_id = node_id
            self.node_params = node_params

    @staticmethod
    def __values_checker(node_type, node_params):
        if type(node_type) != str:
            expected_type = "str"
            given_type = str(type(node_type).__name__)
            raise nodeError.CreateError("Node type", expected_type, given_type)
        if type(node_params) != dict:
            expected_type = "dict"
            given_type = str(type(node_params).__name__)
            raise nodeError.CreateError("Node params", expected_type, given_type)
        return 0

    def __str__(self):
        printable_id = 'ID:' + '\t' + str(self.node_id) + '\n'
        printable_type = 'TYPE:' + '\t' + str(self.node_type) + '\n'
        printable_params = 'PARAMS:' + '\t' + str(self.node_params)
        return printable_id + printable_type + printable_params

    def publish(self, type_of_publish: str):
        if type_of_publish == 'node_type':
            node_type = self.node_type
            return node_type
        elif type_of_publish == 'node_params':
            node_params = '{'
            for key in self.node_params:
                if type(self.node_params[key]) == list:
                    node_params += key + ": " + str(self.node_params[key]) + ", "
                else:
                    node_params += key + ": '" + str(self.node_params[key]) + "', "
            node_params = node_params[:-2]
            node_params += '}'
            if node_params == '}':
                node_params = '{}'
            return node_params
        else:
            raise nodeError.PublishError()

    def __eq__(self, other):
        return self.node_id == other.node_id
