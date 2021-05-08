from model.assistant.message_recognizer import MessageRecognizer
from model.skill import constants

import importlib.util

SCRIPT_MAIN_FUNCTION = constants.SCRIPT_MAIN_FUNCTION


class Assistant:
    def __init__(self, cypher_manager):
        self.message_recognizer = MessageRecognizer(cypher_manager)

    @staticmethod
    def __get_script_result(script_path, message, script_params):
        spec = importlib.util.spec_from_file_location(SCRIPT_MAIN_FUNCTION, script_path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)

        action = script_params['action']
        entity = script_params['entity']
        context = script_params['context']

        script_result = m.main(action, entity, context, message)
        return script_result

    def get_answer(self, message):
        recognize_result = self.message_recognizer.recognize_script(message)
        script_path = recognize_result[0]
        script_params = recognize_result[1]
        script_result = self.__get_script_result(script_path, message, script_params)
        answer = script_result

        return answer
