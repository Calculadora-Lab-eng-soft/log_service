from models.database import Log, db


class LogController:
    def __init__(self):
        self.db = db

    def create(self, log):
        new_log = Log(
            log["type"], log["operation"], log["arguments"], log["created_at"]
        )

        self.db.session.add(new_log)
        self.db.session.commit()

    def index(self):
        logs_objetos = Log.query.all()

        logs_json = [log.to_json() for log in logs_objetos]

        return logs_json
