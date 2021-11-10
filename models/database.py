from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqlconnector://root:root@localhost:3306/teste"

db = SQLAlchemy(app)


@dataclass
class Log(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    operation = db.Column(db.String(50))
    arguments = db.Column(db.String(50))
    created_at = db.Column(db.String(50))

    def __init__(self, type, operation, arguments, created_at):
        self.type = type
        self.operation = operation
        self.arguments = arguments
        self.created_at = created_at

    def to_json(self):
        return {
            "type": self.type,
            "operation": self.operation,
            "arguments": self.arguments,
            "created_at": self.created_at,
        }


db.create_all()
