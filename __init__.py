from controller.market import publish_skill
from controller.skill_validation import skill_checker

from flask import Flask, request
from dotenv import load_dotenv
import os


from controller.market import constants


SKILLS_FOLDER = constants.SKILLS_FOLDER
if __name__ == '__main__':
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")

    app = Flask(__name__)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response


    @app.route('/addSkill', methods=['POST'])
    def add_skill():
        data = request.json

        skill_step = publish_skill.get_skill_step(data)
        check_data = skill_checker.check_skill_properties(data, skill_step)

        if check_data != 'OK':
            return check_data

        skill_properties = publish_skill.get_skill_properties(data)
        skill_script = publish_skill.get_skill_script(data)

        publish_skill.skill_upload(skill_properties, skill_script)

        return 'OK'

    app.run(debug=True, host='localhost', port=PORT)
