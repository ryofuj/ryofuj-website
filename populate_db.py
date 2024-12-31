# populate_db.py

from app import app, db
from models import Logo, Profile, Project, Name, Image

def populate():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Add Logo
        logo = Logo(
            image_filename='logo.jpg',
            # Removed the 'text' field as per previous updates
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
        
        # Add Projects with project_type and other details
        projects = [
            Project(
                title='Modern Living Room',
                image_filename='project1.jpg',
                grid_position='project1',
                project_type='Project',
                position='Lead Designer',
                term='Summer 2023',
                description='Designed a modern living room with minimalist aesthetics and functional furniture.',
                link='https://example.com/projects/modern-living-room'
            ),
            Project(
                title='Corporate Workspace',
                image_filename='project2.jpg',
                grid_position='project2',
                project_type='Experience',
                position='Project Manager',
                term='Winter 2022',
                description='Managed the design and implementation of a corporate workspace to enhance productivity.',
                link='https://example.com/experiences/corporate-workspace'
            ),
            # Add more projects as needed
        ]
        
        # **Important:** Use `add_all` instead of `bulk_save_objects` to ensure IDs are populated
        db.session.add_all(projects)
        db.session.commit()  # Commit to assign IDs to projects
        
        # Add Images for each project
        # It's crucial to associate images with the correct project IDs
        images = []
        for project in projects:
            if project.title == 'Modern Living Room':
                images.extend([
                    Image(project_id=project.id, image_filename='project1_1.jpg'),
                    Image(project_id=project.id, image_filename='project1_2.jpg'),
                ])
            elif project.title == 'Corporate Workspace':
                images.extend([
                    Image(project_id=project.id, image_filename='project2_1.jpg'),
                    Image(project_id=project.id, image_filename='project2_2.jpg'),
                ])
            # Add images for other projects accordingly

        # **Again, use `add_all` instead of `bulk_save_objects`**
        db.session.add_all(images)
        db.session.commit()
        
        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
