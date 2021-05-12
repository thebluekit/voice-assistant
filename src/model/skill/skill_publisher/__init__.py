from model.skill.skill_publisher import skill_saver
from model.skill.skill_validator import SkillValidator
from model.skill import constants
from model.skill import skill_informer as skill_info


class SkillPublisher:
    def __init__(self):
        self.skill_validator = SkillValidator()

    def __check_skill_properties(self, skill_data):
        skill_step = constants.MAX_STEP
        validation = self.skill_validator.check_skill(skill_data, skill_step)

        return validation

    def upload_skill(self, skill_data):
        validation = self.__check_skill_properties(skill_data)
        if validation == 'OK':
            skill_properties = skill_info.get_skill_properties(skill_data)
            skill_id = skill_info.get_skill_id(skill_data)
            # print(skill_id)
            skill_script = skill_info.get_skill_script(skill_data)

            skill_saver.save(skill_properties, skill_script, skill_id)
        return validation
