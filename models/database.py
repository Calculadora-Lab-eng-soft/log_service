from pymongo import MongoClient

class Database():
  def __init__(self):
    self.client = MongoClient("mongodb+srv://messiasleonardo:messiasleonardo@cluster0.y0p1v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    self.db = self.client.get_database('calc_db')

  def getDB(self):
    return self.db
    