from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<DataItem {self.name}, Value {self.value}>"
class Neuron(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer)
    acc = db.Column(db.Integer)
    spd = db.Column(db.Integer)
    str = db.Column(db.Integer)
    cap = db.Column(db.Float)
    hp = db.Column(db.Float)
    bat = db.Column(db.Integer)
    ia = db.Column(db.Integer)
    cpu = db.Column(db.Integer)
    price = db.Column(db.Integer)
    onMarket = db.Column(db.Boolean)
    def __repr__(self):
        return (f"<Neuron id={self.id}, name={self.name}, type={self.type}, acc={self.acc}, spd={self.spd}, str={self.str}, bat={self.bat}, ia={self.ia}, cpu={self.cpu}>")
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nwl = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    neuron_list = db.Column(db.JSON, nullable=False, default=list)
    game_list = db.Column(db.JSON, nullable=False, default=list)
    def __repr__(self):
        return (f"<Team id={self.id}, name={self.name}, nwl={self.nwl}, xp={self.xp}, neuron_list={self.neuron_list}, game_list={self.game_list}")
class HQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upgrading = db.Column(db.String(100))


