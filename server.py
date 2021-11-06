from flask import Flask, request
from flask_cors import CORS
from controllers import LogController

app = Flask(__name__)
controller = LogController.LogController()
CORS(app)


@app.route('/create', methods=['POST'])
def create_log():
  log = request.json

  controller.create(log)

  return { 'response': 'success'}


@app.route('/',  methods=['POST', 'GET'])
def home():
  res = controller.findAll()

  return { 'logs': res}

app.run(port=5003)
