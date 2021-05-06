import json
from controller.market import constants


SKILLS_FOLDER = constants.SKILLS_FOLDER


class SkillInstaller:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def install(self, skill):
        skill_path = SKILLS_FOLDER + skill + ".json"
        with open(skill_path, 'r') as json_file:
            skill_properties = json.load(json_file)

        skill_name = skill_properties['skill_name']
        skill_sentences = skill_properties['skill_sentences']
        for skill_sentence in skill_sentences:
            sentence = skill_sentence['sentence']
            action = skill_sentence['skill_action']
            entity = skill_sentence['skill_entity']
            context = skill_sentence['skill_context']

            self.db_manager.upload_sentence(sentence, skill_name, action, entity, context)
