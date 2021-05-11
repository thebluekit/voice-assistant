from model.skill import constants
import json
import os


def get_skills_id():
    folder = constants.SKILLS_FOLDER
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    if len(sub_folders) != 0:
        folders_num = []
        for sub_folder in sub_folders:
            folders_num.append(int(sub_folder))

        return folders_num
    else:
        return []


def get_all_skills():
    skills_id = get_skills_id()
    skills_props = []
    for skill_id in skills_id:
        skill_props = get_current_skill(skill_id)
        skills_props.append(skill_props)

    return skills_props


def get_current_skill(skill_id):
    skill_id = int(skill_id)
    skill_props = get_skill_props(skill_id)
    return skill_props


def get_skill_props(skill_id: int):
    properties_path = constants.SKILLS_FOLDER + str(skill_id) + '/' + constants.SKILL_JSON_NAME
    with open(properties_path) as json_file:
        skill_properties = json.load(json_file)
        return skill_properties
