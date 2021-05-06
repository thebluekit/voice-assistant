from model.database.cypher import CypherManager
from model.sentence_upload import SentenceManager
from controller.market.skill_install import SkillInstaller

from controller.market import publish_skill
from controller.skill_validation import skill_checker

# DB_LINK = "http://localhost:7474/db/data/"
# DB_PASSWORD = "12345"
import json
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

import psycopg2

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

    @app.route('/')
    def index():
        conn = psycopg2.connect(
            host="localhost",
            database="assistant",
            user="postgres",
            password="1234"
        )
        cur = conn.cursor()

        # with open('public/0/skillProperties.json') as json_file:
        #     data = json.load(json_file)
        #     print(skill_checker.check_skill_properties(data, 3))
        return '0'

    # @app.route('/')
    # def index():
    #     with open('public/0/skillProperties.json') as json_file:
    #         data = json.load(json_file)
    #         print(skill_checker.check_skill_properties(data, 3))
    #     return '0'

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

    # cm = CypherManager()
    # cm.delete_all_nodes()
    # db_manager = SentenceManager(cm)
    #
    # skill_installer = SkillInstaller(db_manager)
    # skill_installer.install('time')
    #
    #
    # sen_1 = "Включи, свет в ванной!!!!!"
    # action_1 = ['включить']
    # entity_1 = ['свет']
    # context_1 = ['ванная']
    #
    # sen_2 = "Переключи свет в ванной комнате"
    # action_2 = ['переключить']
    # entity_2 = ['свет']
    # context_2 = ['ванная', 'комната']
    #
    # cm = CypherManager(DB_INK, DB_PASSWORD)
    # cm.delete_all_nodes()
    # db_manager = SentenceManager(cm)
    #
    # db_manager.upload_sentence(sen_1, "test_func", action_1, entity_1, context_1)
    # db_manager.upload_sentence(sen_2, "test_func2", action_2, entity_2, context_2)
