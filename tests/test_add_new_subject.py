from model.subjects_model import Subjects
from generator.sub_name_generator import random_string

def test_add_subject(app):
    subject = Subjects(screening=random_string('name',8,1,1))
    app.subject.add_new_subject(subject)
    assert app.assertation.element_present("//div/a[@class='circle-button btn btn-white']/span[@class='icon-small icon-add']") == False






