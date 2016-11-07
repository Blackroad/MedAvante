class AssertationHelper:
    def __init__(self,app):
        self.app = app


    def element_present(self, dom_element = None,sub_dom_element = None, class_type=None, class_name=None):
        wd = self.app.wd
        if not dom_element and sub_dom_element and class_type and class_name is None:
            if wd.find.element_by_xpath("//%s//%s[@%s='%s']" % dom_element, sub_dom_element, class_type, class_name):
                return True
            return False