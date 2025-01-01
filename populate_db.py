import json
import os
from app import app
from models import db, Experience

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

def populate_db():
    data_file = os.path.join('data', 'experiences.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        experiences_data = json.load(f)

    with app.app_context():
        db.create_all()
        for exp in experiences_data["experiences"]:
            tags_joined = ",".join(exp.get("tags", [])) if exp.get("tags") else ""
            new_exp = Experience(
                experience_type=exp.get("experience_type"),
                title=exp.get("title"),
                subtitle=exp.get("subtitle"),
                short_description=exp.get("short_description"),
                long_description=exp.get("long_description"),
                main_link=exp.get("main_link"),
                main_image=exp.get("main_image"),
                tile_size=exp.get("tile_size"),
                tags=tags_joined
            )
            db.session.add(new_exp)
        db.session.commit()

if __name__ == '__main__':
    populate_db()
