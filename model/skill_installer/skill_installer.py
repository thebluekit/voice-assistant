from controller.market import constants
import json


def install_skill(skill_id):
    properties_path = constants.SKILLS_FOLDER + str(skill_id) + '/' + constants.SKILL_JSON_NAME
    with open(properties_path) as json_file:
        skill_properties = json.load(json_file)
        print(skill_properties)
