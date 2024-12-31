# populate_db.py

from app import app, db
from models import Logo, Profile, Name, Project, Image

def populate():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add Logo
        logo = Logo(
            image_filename='logo.png'
        )
        db.session.add(logo)

        # Add Profile
        profile = Profile(
            image_filename='profile.jpg'
        )
        db.session.add(profile)

        # Add Name
        name = Name(
            full_name='Ryo Fujimura',
            title='Software Engineer',
            intro='Student at CSULB, majoring in computer science. Add something more here...'
        )
        db.session.add(name)

        # Add Projects with project_type and other details
        projects_data = [
            {
                "company": "American Honda Motor Company, Inc.",
                "type": "Project",
                "term": "June 2024 - August 2024",
                "image": "honda.svg",
                "title": "Software Engineer Intern",
                "description": "Conducted comprehensive research on on-device generative AI, focusing on its potential applications within the automotive industry to enhance vehicle functionalities. Developed and demonstrated applications on an NVIDIA Jetson Orin Nano 8GB using Linux and CUDA, showcasing on-device generative AI capabilities with Meta's Llama 3 model to enhance vehicle autonomy and local AI performance.",
                "link": "https://www.honda.com/"
            },
            {
                "company": "CUSCO USA Inc.",
                "type": "Work",
                "term": "October 2021 - May 2024",
                "image": "cusco.svg",
                "title": "Data Engineer",
                "description": "Led a three-member team in developing a Python application that extracted data from 11,560 archived PDF files, utilizing advanced software development methodologies. Demonstrated proficiency in testing and development, including the creation of comprehensive test cases to ensure software quality and functionality. Enhanced user access to historical data dating back to 1977, resulting in a 30% increase in revenue by enabling precise retrieval of previously inaccessible information for new users.",
                "link": "https://cuscousainc.com/"
            },
            {
                "company": "CUSCO USA Inc.",
                "type": "Work",
                "term": "October 2021 - May 2024",
                "image": "cusco.svg",
                "title": "Full Stack Web Developer",
                "description": "Collaborated with a team of 2 to develop a modern website utilizing Svelte with Svelte Kit, focusing on UI and information accessibility, resulting in a 50% reduction in exit rate. Implemented data management systems including Google Drive, Cloudinary, and Sanity for efficient content organization and delivery, leading to a 250% increase in revenue over the past three years.",
                "link": "https://cuscousainc.com/"
            },
            {
                "company": "FUJITSUBO GIKEN KOGYO CO., LTD",
                "type": "Work",
                "term": "September 2023 - November 2023",
                "image": "fujitsubo.svg",
                "title": "Data Engineer",
                "description": "Engineered a Python-based software program employing web scraping techniques to meticulously extract crucial data from diverse websites. Automated generation workflows with Adobe InDesign, significantly boosting efficiency and achieving a 100% error-free rate by eliminating manual effort across various cases, ensuring software quality and functionality.",
                "link": "https://www.fujitsubo.co.jp/"
            },
            {
                "company": "Matcha Time",
                "type": "Work",
                "term": "March 2024 - April 2024",
                "image": "matchatime.svg",
                "title": "Co-PM and Developer",
                "description": "Developed and created application functions with Swift/SwiftUI, implemented multi-city synchronization, designed and tested features, fixed bugs, and deployed solutions. Planned and completed the project in 4 weeks, launched the application on the Mac App Store, and managed cross-functional team collaboration to ensure seamless integration and project success.",
                "link": "https://apps.apple.com/us/app/matcha-time/id6497067918?mt=12"
            },
            {
                "company": "Poker Percentage",
                "type": "Project",
                "term": "January 2022 - April 2024",
                "image": "poker.png",
                "title": "Developer",
                "description": "Developed a poker percentage calculator application for watchOS using Swift and WatchKit, facilitating real-time calculation of odds and probabilities. Improved user decision-making by providing accurate insights into poker hands, resulting in a 15% increase in win rates among users.",
                "link": "https://apps.apple.com/us/app/poker-pocket-odds/id6499280318"
            },
            {
                "company": "Schedule Mastermind",
                "type": "Project",
                "term": "December 2023 - February 2024",
                "image": "schedule.jpg",
                "title": "Developer",
                "description": "Engineered a Python-based application with the Flask framework, streamlining scheduling operations for over 500 classes. Created a user-friendly interface for course selection, timetable generation, and conflict resolution, achieving a 100% reduction in scheduling errors and boosting overall productivity by 25% through automation.",
                "link": "/app1"
            },
            {
                "company": "Shohei Home Ground",
                "type": "Project",
                "term": "March 2023 - November 2023",
                "image": "shoheihomeground.svg",
                "title": "Developer and Project Leader",
                "description": "Engineered and deployed a streamlined content scheduling and posting process using Python and the Instagram API, achieving 685 posts and increasing followers by 11,000 in 8 months. Transformed the project from a non-revenue-generating initiative to a profitable venture by enhancing engagement and expanding the audience.",
                "link": "https://www.instagram.com/shoheihomeground/"
            },
            {
                "company": "Amazon Web Services",
                "type": "Leadership",
                "term": "September 2023 - November 2023",
                "image": "aws.png",
                "title": "Trainer",
                "description": "Provided training sessions to professionals on Amazon Web Services, imparting knowledge on cloud infrastructure and services.",
                "link": "/"
            },
            {
                "company": "Research Paper",
                "type": "Publication",
                "term": "September 2024",
                "image": "resume.png",
                "title": "6G Network and Data Management with Blockchain",
                "description": "Provided training sessions to professionals on Amazon Web Services, imparting knowledge on cloud infrastructure and services.",
                "link": "https://docs.google.com/document/d/1K49_6etVnN7hcCNUc1l-0wJpp3B-NT9J/edit?usp=sharing"
            },
            # Add more projects as needed
        ]

        new_projects = []
        grid_pos_counter = 1

        for item in projects_data:
            # Determine project_type based on 'type' field
            type_lower = item["type"].lower()
            if type_lower in ["work", "leadership"]:
                project_type = "Experience"
            elif type_lower in ["project", "publication"]:
                project_type = "Project"
            else:
                project_type = "Experience"  # Default fallback

            grid_position = f"project{grid_pos_counter}"
            grid_pos_counter += 1

            project = Project(
                title=item["title"],
                image_filename=item["image"],
                grid_position=grid_position,
                project_type=project_type,
                position=item.get("company", ""),
                term=item.get("term", ""),
                description=item.get("description", ""),
                link=item.get("link", "")
            )
            new_projects.append(project)

        # Add all projects to the session and commit to assign IDs
        db.session.add_all(new_projects)
        db.session.commit()

        # Add Images for each project if needed (optional)
        # Since each project in your data has only one image, we can skip this step
        # If you have multiple images per project, you can add them here
        #
        # Example:
        # images = [
        #     Image(project_id=new_projects[0].id, image_filename='project1_1.jpg'),
        #     Image(project_id=new_projects[0].id, image_filename='project1_2.jpg'),
        #     # Add more images as needed
        # ]
        # db.session.add_all(images)
        # db.session.commit()

        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
