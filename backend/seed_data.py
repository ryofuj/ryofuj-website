# Example seed_data.py
from app import db, Project, app

with app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Project(
        title="Project Alpha",
        description="A test project",
        image_url="/images/alpha.jpg"
    )
    p2 = Project(
        title="Project Beta",
        description="Another test project",
        image_url="/images/beta.jpg"
    )

    db.session.add_all([p1, p2])
    db.session.commit()
    print("Database seeded!")
