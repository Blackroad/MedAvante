from model.subjects_model import Subjects

def test_add_subject(app):
    subject = Subjects(screening='21455')
    app.subject.add_new_subject(subject)
    assert app.wd.find_element_by_xpath("//div//a[@title='Edit']")
    assert app.wd.find_element_by_xpath("//div//a/span[@class='icon-small icon-delete']")
    assert app.wd.find_element_by_xpath("//div//a[@title='Add']")





