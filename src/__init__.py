from model.database.cypher import CypherManager
from model.sentence.uploader import SentenceUploader
from model.skill.skill_installer import SkillInstaller
from model.assistant import Assistant

from controller.skill_upload import upload_skill, check_skill
from controller.skill_install import install_skill
from controller.assistant import get_answer

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

from model.skill.skill_modifier import get_all_skills

if __name__ == '__main__':
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")

    cm = CypherManager()
    # cm.delete_all_nodes()
    db_manager = SentenceUploader(cm)
    skill_installer = SkillInstaller(db_manager)
    assistant = Assistant(cypher_manager=cm)

    app = Flask(__name__)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.route('/marketplace')
    def render_marketplace():
        return render_template("marketplace.html")

    @app.route('/')
    def render_assistant():
        return render_template("assistant.html")

    @app.route('/addSkill', methods=['POST'])
    def add_skill():
        data = request.json
        upload_status = upload_skill(data)
        return upload_status

    @app.route('/checkSkill', methods=['POST'])
    def check_skill():
        data = request.json
        validation_status = check_skill(data)
        return validation_status

    @app.route('/installSkill')
    def install_selected_skill():
        install_skill(skill_installer, '0')
        return 'OK'

    @app.route('/getMessage')
    def get_message():
        message = request.args.get("message")
        answer = get_answer(assistant, message)
        return answer

    @app.route('/getAllSkills', methods=['GET'])
    def get_skills():
        all_skills = get_all_skills()
        d = {'skills': all_skills}
        return jsonify(d)

    app.run(debug=True, host='localhost', port=PORT)
