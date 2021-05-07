class ConnectTypeError(Exception):
    def __init__(self, message, expected_type, given_type):
        self.message = message + " must be " + expected_type + ", not " + given_type
        super().__init__(self.message)
