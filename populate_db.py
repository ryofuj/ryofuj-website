from app import app, db
from models import Logo, Profile, Name, Project, Image

def populate():
    with app.app_context():
        db.drop_all()
        db.create_all()

        logo = Logo(image_filename='logo.png')
        db.session.add(logo)

        profile = Profile(image_filename='profile.jpg')
        db.session.add(profile)

        name = Name(
            full_name='Ryo Fujimura',
            title='Software Engineer',
            intro='Student at CSULB, majoring in computer science. Add something more here...'
        )
        db.session.add(name)

        projects_data = [
            {
                "company": "Matcha Time",
                "type": "Work",
                "term": "March 2024 - April 2024",
                "image": "matchatime.svg",
                "title": "Co-PM and Developer",
                "description": "Developed and created application functions with Swift/SwiftUI...",
                "link": "https://apps.apple.com/us/app/matcha-time/id6497067918?mt=12"
            },
            {
                "company": "American Honda Motor Company, Inc.",
                "type": "Project",
                "term": "June 2024 - August 2024",
                "image": "honda.svg",
                "title": "Software Engineer Intern",
                "description": "Conducted comprehensive research on on-device generative AI...",
                "link": "https://www.honda.com/"
            },
            {
                "company": "Poker Percentage",
                "type": "Project",
                "term": "January 2022 - April 2024",
                "image": "poker.png",
                "title": "Developer",
                "description": "Developed a poker percentage calculator application for watchOS...",
                "link": "https://apps.apple.com/us/app/poker-pocket-odds/id6499280318"
            },
            {
                "company": "CUSCO USA Inc.",
                "type": "Work",
                "term": "October 2021 - May 2024",
                "image": "cusco.svg",
                "title": "Data Engineer",
                "description": "Led a three-member team in developing a Python application...",
                "link": "https://cuscousainc.com/"
            },
            {
                "company": "Schedule Mastermind",
                "type": "Project",
                "term": "December 2023 - February 2024",
                "image": "schedule.jpg",
                "title": "Developer",
                "description": "Engineered a Python-based application with the Flask framework...",
                "link": "/app1"
            },
            {
                "company": "Bose Corporation",
                "type": "Work",
                "term": "June 2025 - August 2025",
                "image": "bose.svg",
                "title": "Mobile Application Developer Intern",
                "description": "iOS / Android developer.",
                "link": "https://www.bose.com/"
            },
            {
                "company": "FUJITSUBO GIKEN KOGYO CO., LTD",
                "type": "Work",
                "term": "September 2023 - November 2023",
                "image": "fujitsubo.svg",
                "title": "Data Engineer",
                "description": "Engineered a Python-based software program employing web scraping...",
                "link": "https://www.fujitsubo.co.jp/"
            },
            {
                "company": "Shohei Home Ground",
                "type": "Project",
                "term": "March 2023 - November 2023",
                "image": "shoheihomeground.svg",
                "title": "Developer and Project Leader",
                "description": "Engineered and deployed a streamlined content scheduling...",
                "link": "https://www.instagram.com/shoheihomeground/"
            },
            {
                "company": "Amazon Web Services",
                "type": "Leadership",
                "term": "September 2023 - November 2023",
                "image": "aws.png",
                "title": "Trainer",
                "description": "Provided training sessions to professionals on Amazon Web Services...",
                "link": "/"
            },
            {
                "company": "Research Paper",
                "type": "Publication",
                "term": "September 2024",
                "image": "resume.png",
                "title": "6G Network and Data Management with Blockchain",
                "description": "Provided training sessions to professionals on Amazon Web Services...",
                "link": "https://docs.google.com/document/d/1K49_6etVnN7hcCNUc1l-0wJpp3B-NT9J/edit?usp=sharing"
            },
        ]

        new_projects = []
        grid_counter = 1
        for item in projects_data:
            if item["type"].lower() in ["work", "leadership"]:
                project_type = "Experience"
            elif item["type"].lower() in ["project", "publication"]:
                project_type = "Project"
            else:
                project_type = "Experience"

            grid_pos = f"project{grid_counter}"
            grid_counter += 1

            p = Project(
                title=item["title"],
                image_filename=item["image"],
                grid_position=grid_pos,
                project_type=project_type,
                position=item["company"],
                term=item["term"],
                description=item["description"],
                link=item["link"]
            )
            db.session.add(p)
            db.session.commit()

            # Example for adding background slides + images in DB (optional):
            # For demonstration, we'll add 3 images with descriptions
            extra_images = [
                Image(project_id=p.id, image_filename=f"{item['image'].split('.')[0]}_1.jpg", image_description="Slide 1 description"),
                Image(project_id=p.id, image_filename=f"{item['image'].split('.')[0]}_2.jpg", image_description="Slide 2 description"),
                Image(project_id=p.id, image_filename=f"{item['image'].split('.')[0]}_3.jpg", image_description="Slide 3 description")
            ]
            db.session.add_all(extra_images)

        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
