from models.database import Database
from bson.json_util import dumps

class LogController():
  def __init__(self):
    self.db_model = Database()
    self.db = self.db_model.getDB()

  def create(self, new_log):
    logs = self.db.logs

    logs.insert_one(new_log)

    return 

  def findAll(self):
    logs = self.db.logs

    json_logs = dumps(list(logs.find()))

    return json_logs