class PublishError(Exception):
    def __init__(self, message='Type of publish must be "node_type" or "node_params"'):
        self.message = message
        super().__init__(self.message)


class UpdateError(Exception):
    def __init__(self, message='Type of update must be "node_type" or "node_params"'):
        self.message = message
        super().__init__(self.message)


class CreateError(Exception):
    def __init__(self, message, expected_type, given_type):
        self.message = message + " must be " + expected_type + ", not " + given_type
        super().__init__(self.message)
