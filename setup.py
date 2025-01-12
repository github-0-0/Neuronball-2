from models import db, DataItem
from app import app

def initialize_database():
    with app.app_context():
        db.create_all()
        db.session.add_all([
            DataItem(name="Card 1", value=0),
            DataItem(name="Card 2", value=0),
        ])
        db.session.commit()
        print("Database initialized and data added!")

if __name__ == "__main__":
    initialize_database()
