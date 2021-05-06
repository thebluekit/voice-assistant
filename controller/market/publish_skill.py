import json
from controller.market import constants
from model.sentence_upload.sentence_converter import SentenceConverter
import os

SKILLS_FOLDER = constants.SKILLS_FOLDER


def generate_script_id():
    folder = SKILLS_FOLDER
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    if len(sub_folders) != 0:
        folders_num = []
        for sub_folder in sub_folders:
            folders_num.append(int(sub_folder))
        new_folder = max(folders_num) + 1
        return new_folder
    else:
        return 0


def get_skill_properties(data):
    skill_properties = {
        "skillName": data["skillName"],
        "skillDescription": data["skillDescription"],
        "skillDate": data["skillDate"],
        "phrases": get_converted_activators(data["phrases"]),
        "skillConstants": data["skillConstants"]
    }
    return skill_properties


def get_converted_activators(phrases):
    sc = SentenceConverter()
    for i in range(len(phrases)):
        normalized_action = sc.get_words_from_activators(phrases[i]['action'])
        normalized_entity = sc.get_words_from_activators(phrases[i]['entity'])
        normalized_context = sc.get_words_from_activators(phrases[i]['context'])

        phrases[i]['normalized_action'] = normalized_action
        phrases[i]['normalized_entity'] = normalized_entity
        phrases[i]['normalized_context'] = normalized_context
    return phrases


def get_skill_script(data):
    skill_file = data["skillScript"]
    return skill_file


def get_skill_step(data):
    skill_step = int(data["skillStep"])
    return skill_step


def skill_upload(skill_properties, skill_script):
    folder = str(generate_script_id())
    try:
        os.mkdir(SKILLS_FOLDER + folder)
    except FileExistsError:
        pass

    skill_path = SKILLS_FOLDER + folder + '/' + "skillProperties.json"
    script_path = SKILLS_FOLDER + folder + '/' + "script.py"

    with open(skill_path, "w") as outfile:
        json.dump(skill_properties, outfile, indent=4)

    f = open(script_path, "w")
    f.write(skill_script)
    f.close()

    return 0
