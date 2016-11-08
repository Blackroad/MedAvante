class AssertationHelper:
    def __init__(self,app):
        self.app = app


    def element_present(self, xpath):
        wd = self.app.wd
        try:
            wd.find.element_by_xpath(xpath)
        except:
            return False
