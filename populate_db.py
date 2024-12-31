# populate_db.py

from app import app, db
from models import Logo, Profile, Project, Name

def populate():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Add Logo
        logo = Logo(
            image_filename='logo.jpg',
            # Removed the 'text' field
            # text='Maison Luxury Living'
        )
        db.session.add(logo)
        
        # Add Profile
        profile = Profile(
            image_filename='profile.jpg'
        )
        db.session.add(profile)
        
        # Add Name
        name = Name(
            full_name='John Doe',
            title='Senior Interior Designer',
            intro='Passionate about creating luxurious and comfortable living spaces.'
        )
        db.session.add(name)
        
        # Add Projects
        projects = [
            Project(title='Project1', image_filename='project1.jpg', grid_position='project1'),
            Project(title='Project2', image_filename='project2.jpg', grid_position='project2'),
            Project(title='Project3', image_filename='project3.jpg', grid_position='project3'),
            Project(title='Project4', image_filename='project4.jpg', grid_position='project4'),
            Project(title='Project5', image_filename='project5.jpg', grid_position='project5'),
            Project(title='Project6', image_filename='project6.jpg', grid_position='project6'),
            Project(title='Project7', image_filename='project7.jpg', grid_position='project7'),
            Project(title='Project8', image_filename='project8.jpg', grid_position='project8'),
            Project(title='Project9', image_filename='project9.jpg', grid_position='project9'),
            Project(title='Project10', image_filename='project10.jpg', grid_position='project10'),
            Project(title='Project11', image_filename='project11.jpg', grid_position='project11'),
            Project(title='Project12', image_filename='project12.jpg', grid_position='project12'),
            Project(title='Project13', image_filename='project13.jpg', grid_position='project13'),
            Project(title='Project14', image_filename='project14.jpg', grid_position='project14'),
            Project(title='Project15', image_filename='project15.jpg', grid_position='project15'),
        ]
        
        db.session.bulk_save_objects(projects)
        
        # Commit all changes
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
