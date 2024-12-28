import json
from app import db, Project, app

def seed_database():
    # Load project data from projects.json
    with open('projects.json', 'r') as f:
        projects_data = json.load(f)

    with app.app_context():
        # Drop existing tables and create new ones
        db.drop_all()
        db.create_all()

        # Iterate over project data and add to the database
        for project in projects_data:
            new_project = Project(
                id=project['id'],
                company=project['company'],
                title=project['title'],
                term=project['term'],
                image_url=project.get('image_url'),
                images=project.get('images', [project.get('image_url')]) if project.get('image_url') else [],
                role=project['role'],
                description=project['description'],
                link=project['link'],
                model_url=project.get('model_url')
            )
            db.session.add(new_project)

        # Commit the session to save data
        db.session.commit()
        print("Database seeded with project data successfully!")

if __name__ == "__main__":
    seed_database()
