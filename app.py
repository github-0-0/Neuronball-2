from flask import Flask, render_template, jsonify, request
from models import db, DataItem, Neuron, Team, HQ
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

@app.route("/")
def index():
    items = DataItem.query.all()
    return render_template("index.html", items=items)

@app.route('/increment/<cardId>', methods=['POST'])
def increment_card_count(cardId):
    item = DataItem.query.filter_by(name=f'Card {cardId}').first()
    if item:
        item.value += 1
    else:
        item = DataItem(card_id=cardId, value=1)
        db.session.add(item)
    db.session.commit()
    return jsonify({"new_value": item.value})
@app.route('/neuron/<neuron_id>', methods=['GET'])
def getNeuron(neuron_id):
    item = Neuron.query.filter_by(id=neuron_id).first()
    return jsonify(item.__repr__())
@app.route('/create', methods=['POST'])
def create_team():
    data = request.get_json()
    teamId = db.session.query(Team).count()
    item = Team.query.filter_by(id=teamId).first()
    if item:
        return None
    else:
        neuronIdList = []
        for i in range(5):
            neuronId = db.session.query(Neuron).count()
            neuronIdList.append(neuronId)
            db.session.add(Neuron(id=neuronId,name="Joe",type=0,acc=15,spd=15,str=15,cap=1.00,hp=1.00,bat=0,ia=0,cpu=0,price=None,onMarket=False))
        item = Team(id=teamId,name=data['name'],nwl=800,xp=0,neuron_list=neuronIdList,game_list=[])
        db.session.add(item)
    db.session.commit()
    return jsonify(item.__repr__())
    
if __name__ == "__main__":
    app.run(debug=True)
