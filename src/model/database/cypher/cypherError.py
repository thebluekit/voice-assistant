class LoginError(Exception):
    def __init__(self, message="Invalid username or password"):
        self.message = message
        super().__init__(self.message)


class ConnectError(Exception):
    def __init__(self, message="Database is offline"):
        self.message = message
        super().__init__(self.message)


class ConnectTypeError(Exception):
    def __init__(self, message, expected_type, given_type):
        self.message = message + " must be " + expected_type + ", not " + given_type
        super().__init__(self.message)


class ConnectionProfileError(Exception):
    def __init__(self, message="Wrong database link"):
        self.message = message
        super().__init__(self.message)


class NodeTypeError(Exception):
    def __init__(self, message="Incorrect node type"):
        self.message = message
        super().__init__(self.message)


class RelationDirectionError(Exception):
    def __init__(self, message="Incorrect relation direction"):
        self.message = message
        super().__init__(self.message)
