from model.assistant.message_recognizer import MessageRecognizer


class Assistant:
    def __init__(self, cypher_manager):
        self.message_recognizer = MessageRecognizer(cypher_manager)

    def get_answer(self, message):
        answer = self.message_recognizer.recognize_script(message)
        return answer
