from flask_cors import CORS
from flask import request, Response
from models.database import app, db
from controllers.LogController import LogController
import json

CORS(app)


@app.route("/add", methods=["POST"])
def add():
    controller.create(request.json)

    return {"status_text": "success", "status": 201}


@app.route("/", methods=["POST", "GET"])
def get():
    logs = controller.index()

    return Response(json.dumps(logs))


if __name__ == "__main__":
    controller = LogController()
    db.create_all()
    app.run(port=5003)
