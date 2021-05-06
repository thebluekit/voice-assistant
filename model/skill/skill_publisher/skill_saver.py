import json
from model.skill import constants

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


def save(skill_properties, skill_script):
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
