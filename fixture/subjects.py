

class SubjectHelper:
    def __init__(self, app):
        self.app = app



    def add_new_subject(self,Subjects):
        wd = self.app.wd
        self.fill_subject_fields(Subjects)



    def fill_subject_fields(self, Subjects):
        wd = self.app.wd
        self.change_field_value("screeningNum", Subjects.screening)
        self.change_field_value("temporaryId", Subjects.temporary_id)
        self.consent_to_record()
        self.language()
        wd.find_element_by_xpath("//div[@class='editing-controls']//span[@class='icon-small icon-save']").click()

    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def consent_to_record(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='row collapsed-row']//button ").click()
        wd.find_element_by_xpath("//div[@class='dropdown-menu']//li/span[text()='  Yes']").click()

    def language(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='value col-xs-15']//button ").click()
        wd.find_element_by_xpath("//div[@class='dropdown-menu']//li/span[text()='  English (US)']").click()


