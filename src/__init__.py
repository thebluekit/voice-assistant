from src.controller.skill_upload import upload_skill, check_skill


from flask import Flask, request
from dotenv import load_dotenv
import os


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
        upload_status = upload_skill(data)
        return upload_status

    @app.route('/checkSkill', methods=['POST'])
    def check_skill():
        data = request.json
        validation_status = check_skill(data)
        return validation_status

    app.run(debug=True, host='localhost', port=PORT)
