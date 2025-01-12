from models import db, DataItem
from app import app

def initialize_database():
    with app.app_context():
        db.create_all()
        db.session.commit()
        print("Database initialized and data added!")

if __name__ == "__main__":
    initialize_database()
