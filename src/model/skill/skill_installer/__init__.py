import json
from shutil import copyfile
from model.skill import constants


SKILLS_FOLDER = constants.SKILLS_FOLDER
SCRIPTS_FOLDER = constants.SCRIPTS_FOLDER


class SkillInstaller:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @staticmethod
    def __unpack_skill(skill_id: int):
        properties_path = constants.SKILLS_FOLDER + str(skill_id) + '/' + constants.SKILL_JSON_NAME
        with open(properties_path) as json_file:
            skill_properties = json.load(json_file)
            return skill_properties

    def install(self, skill_id: int):
        skill_properties = self.__unpack_skill(skill_id)
        skill_name = skill_properties['skillName']
        skill_sentences = skill_properties['phrases']
        for skill_sentence in skill_sentences:
            sentence = skill_sentence['phrase']
            action = skill_sentence['normalized_action']
            entity = skill_sentence['normalized_entity']
            context = skill_sentence['normalized_context']

            self.db_manager.upload_sentence(sentence, skill_name, action, entity, context)
        self.__save_script(skill_id, skill_name)
        return 'OK'

    @staticmethod
    def __save_script(skill_id: int, skill_name: str):
        folder = str(skill_id)
        script_path = SKILLS_FOLDER + folder + '/' + "script.py"
        new_script_path = SCRIPTS_FOLDER + skill_name + ".py"
        copyfile(script_path, new_script_path)

