from app import db, Project, app

with app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Project(
        title="Project Alpha",
        description="This is the first test project",
        image_url="/images/alpha.jpg"
    )
    p2 = Project(
        title="Project Beta",
        description="Second test project, includes a 3D model",
        image_url="/images/beta.jpg"
    )

    db.session.add_all([p1, p2])
    db.session.commit()

    print("Database seeded with sample projects!")
