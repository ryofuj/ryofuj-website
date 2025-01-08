from flask import Flask, render_template
from models import db, Profile, Experience, Tag, ExperienceType
import os

app = Flask(__name__)

# Configure SQLite (local) database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def get_or_create_experience_type(name):
    """
    Helper function to either retrieve an existing ExperienceType
    or create a new one if it doesn't exist.
    """
    et = ExperienceType.query.filter_by(name=name).first()
    if not et:
        et = ExperienceType(name=name)
        db.session.add(et)
        db.session.commit()
    return et

def get_or_create_tag(tag_name):
    """
    Helper function to either retrieve an existing Tag
    or create a new one if it doesn't exist.
    """
    t = Tag.query.filter_by(name=tag_name).first()
    if not t:
        t = Tag(name=tag_name)
        db.session.add(t)
        db.session.commit()
    return t

@app.before_request
def create_tables():
    """
    Create all tables in the database before the first request.
    This is just a demo approach. In production, you might manage 
    migrations using Flask-Migrate or Alembic. 
    """
    db.create_all()
    seed_data()  # Insert sample data

def seed_data():
    """
    Insert/update initial data if the tables are empty (or if you want to 
    ensure certain records exist). Adjust as needed for your use case.
    """
    # 1. Profile
    if not Profile.query.first():
        profile = Profile(
            name="Ryo Fujimura",
            title="Software Engineer",
            bio="Aspiring CS student with expertise in AI, data engineering, and software solutions.",
            img_path="/static/images/ryosketch-1.png"
        )
        db.session.add(profile)
    
    # 2. Experience Types (pre-create common ones)
    #    We expect to see Work, Project, Leadership, Publication, etc. 
    #    We'll add or create on-the-fly in the loop below as well.
    base_types = ["Work", "Project", "New", "Leadership", "Publication"]
    for base_type in base_types:
        get_or_create_experience_type(base_type)

    # 3. Pre-create some tags or rely on dynamic creation below
    #    Add a few to illustrate
    default_tags = ["Python", "Flask", "Web Dev", "AI", "Data", "Swift", "C++", "AWS", "computer_science", "adobe", "project_management"]
    for tag_name in default_tags:
        get_or_create_tag(tag_name)

    # 4. Experience data (from your JSON)
    data = {
      "experiences": [
        {
          "experience_type": "Project",
          "title": "Software Engineer Intern",
          "subtitle": "American Honda Motor Company, Inc. (June 2024 - August 2024)",
          "short_description": "Conducted on-device AI research for automotive applications.",
          "long_description": "Conducted comprehensive research on on-device generative AI, focusing on its potential applications within the automotive industry to enhance vehicle functionalities. Developed and demonstrated applications on an NVIDIA Jetson Orin Nano 8GB using Linux and CUDA, showcasing on-device generative AI capabilities with Meta's Llama 3 model to enhance vehicle autonomy and local AI performance.",
          "main_link": "https://www.honda.com/",
          "main_image": "honda.svg",
          "tags": ["swift", "computer_science"]
        },
        {
          "experience_type": "Work",
          "title": "Data Engineer",
          "subtitle": "CUSCO USA Inc. (October 2021 - May 2024)",
          "short_description": "Led a team to develop Python apps extracting data from thousands of PDFs.",
          "long_description": "Led a three-member team in developing a Python application that extracted data from 11,560 archived PDF files, utilizing advanced software development methodologies. Demonstrated proficiency in testing and development, including the creation of comprehensive test cases to ensure software quality and functionality. Enhanced user access to historical data dating back to 1977, resulting in a 30% increase in revenue by enabling precise retrieval of previously inaccessible information for new users.",
          "main_link": "https://cuscousainc.com/",
          "main_image": "cusco.svg",
          "tags": ["python", "project_management", "adobe"]
        },
        {
          "experience_type": "Work",
          "title": "Data Engineer",
          "subtitle": "FUJITSUBO GIKEN KOGYO CO., LTD (September 2023 - November 2023)",
          "short_description": "Python-based scraper to automate data extraction.",
          "long_description": "Engineered a Python-based software program employing web scraping techniques to meticulously extract crucial data from diverse websites. Automated generation workflows with Adobe InDesign, significantly boosting efficiency and achieving a 100% error-free rate by eliminating manual effort across various cases, ensuring software quality and functionality.",
          "main_link": "https://www.fujitsubo.co.jp/",
          "main_image": "fujitsubo.svg",
          "tags": ["python", "adobe"]
        },
        {
          "experience_type": "Work",
          "title": "Co-PM and Developer",
          "subtitle": "Matcha Time (March 2024 - April 2024)",
          "short_description": "Swift/SwiftUI project with multi-city sync.",
          "long_description": "Developed and created application functions with Swift/SwiftUI, implemented multi-city synchronization, designed and tested features, fixed bugs, and deployed solutions. Planned and completed the project in 4 weeks, launched the application on the Mac App Store, and managed cross-functional team collaboration to ensure seamless integration and project success.",
          "main_link": "https://apps.apple.com/us/app/matcha-time/id6497067918?mt=12",
          "main_image": "matchatime.svg",
          "tags": ["swift", "project_management"]
        },
        {
          "experience_type": "Project",
          "title": "Developer",
          "subtitle": "Poker Percentage (January 2022 - April 2024)",
          "short_description": "WatchOS app for real-time poker odds.",
          "long_description": "Developed a poker percentage calculator application for watchOS using Swift and WatchKit, facilitating real-time calculation of odds and probabilities. Improved user decision-making by providing accurate insights into poker hands, resulting in a 15% increase in win rates among users.",
          "main_link": "https://apps.apple.com/us/app/poker-pocket-odds/id6499280318",
          "main_image": "poker.png",
          "tags": ["swift", "project_management"]
        },
        {
          "experience_type": "Project",
          "title": "Developer",
          "subtitle": "Schedule Mastermind (December 2023 - February 2024)",
          "short_description": "Streamlined scheduling with Python & Flask.",
          "long_description": "Engineered a Python-based application with the Flask framework, streamlining scheduling operations for over 500 classes. Created a user-friendly interface for course selection, timetable generation, and conflict resolution, achieving a 100% reduction in scheduling errors and boosting overall productivity by 25% through automation.",
          "main_link": "/app1",
          "main_image": "schedule.jpg",
          "tags": ["python", "computer_science"]
        },
        {
          "experience_type": "Project",
          "title": "Developer and Project Leader",
          "subtitle": "Shohei Home Ground (March 2023 - November 2023)",
          "short_description": "Automated Instagram posting, grew 11k followers.",
          "long_description": "Engineered and deployed a streamlined content scheduling and posting process using Python and the Instagram API, achieving 685 posts and increasing followers by 11,000 in 8 months. Transformed the project from a non-revenue-generating initiative to a profitable venture by enhancing engagement and expanding the audience.",
          "main_link": "https://www.instagram.com/shoheihomeground/",
          "main_image": "shoheihomeground.svg",
          "tags": ["python", "project_management"]
        },
        {
          "experience_type": "Leadership",
          "title": "Trainer",
          "subtitle": "Amazon Web Services (September 2023 - November 2023)",
          "short_description": "AWS cloud infrastructure training.",
          "long_description": "Provided training sessions to professionals on Amazon Web Services, imparting knowledge on cloud infrastructure and services.",
          "main_link": "/",
          "main_image": "aws.png",
          "tags": ["aws"]
        },
        {
          "experience_type": "Publication",
          "title": "6G Network and Data Management with Blockchain",
          "subtitle": "Research Paper (September 2024)",
          "short_description": "Research on AWS & Blockchain for 6G networks.",
          "long_description": "Provided training sessions to professionals on Amazon Web Services, imparting knowledge on cloud infrastructure and services.",
          "main_link": "https://docs.google.com/document/d/1K49_6etVnN7hcCNUc1l-0wJpp3B-NT9J/edit?usp=sharing",
          "main_image": "resume.png",
          "tags": ["computer_science"]
        }
      ]
    }

    # Insert Experiences
    for item in data["experiences"]:
        # 4a. Get or create the ExperienceType
        etype = get_or_create_experience_type(item["experience_type"])

        # 4b. Create the Experience object
        exp = Experience(
            experience_type_id=etype.id,
            title=item.get("title"),
            subtitle=item.get("subtitle"),
            short_description=item.get("short_description"),
            long_description=item.get("long_description"),
            main_link=item.get("main_link"),
            main_image=item.get("main_image"),
            tile_size=""  # optional: set if you have a desired tile_size
        )

        db.session.add(exp)
        db.session.flush()  # flush to get the new exp.id if needed

        # 4c. Handle tags
        tag_list = item.get("tags", [])
        for tag_name in tag_list:
            tag_obj = get_or_create_tag(tag_name)
            exp.tags.append(tag_obj)

    db.session.commit()

@app.route('/')
def home():
    """
    Example route rendering some data in a simple way.
    """
    profile = Profile.query.first()
    experiences = Experience.query.all()
    
    return render_template(
        'index.html',
        profile=profile,
        experiences=experiences
    )

if __name__ == '__main__':
    # Make sure the DB file directory is valid
    if not os.path.exists('local_database.db'):
        open('local_database.db', 'a').close()

    app.run(debug=True)
