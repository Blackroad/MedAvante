from model.subjects_model import Subjects

def test_add_subject(app):
    app.navigation.open_dashboard()
    app.navigation.select_study('pharma - Dev R Study')
    app.navigation.open_new_subject_screen()
    app.subjects.add_new_subject(Subjects(screening='21343'))




