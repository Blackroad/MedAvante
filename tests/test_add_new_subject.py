from model.subjects_model import Subjects

def test_add_subject(app):
    subject = Subjects(screening='21443')
    app.subject.add_new_subject(subject)




