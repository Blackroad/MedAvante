class NavigationHelper:
    def __init__(self,app):
        self.app = app



    def open_dashboard(self):
        wd=self.app.wd
        if len(wd.find_elements_by_id("page-title"))== 0:
            wd.find_element_by_xpath("//*[@class='icon-small icon-home']").click()
        wd.find_element_by_xpath('//*[@href="/study"]').click()

    def select_study(self, study_name):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath('//*[@class="dashboard-tile root-filter"]'))== 0:
            wd.find_element_by_xpath('//*[@class="btn-group ng-isolate-scope"]').click()
            wd.find_element_by_xpath("//div[@class='dropdown-menu']//li//span[text()='  %s']" % study_name).click()
            self.wait("//a[@class='dashboard-tile root-filter']/span[text()='Subjects']")
        self.open_subject_list()

    def open_subject_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@class='dashboard-tile root-filter']/span[text()='Subjects']").click()


    def open_new_subject_screen(self):
        wd = self.app.wd
        site = self.app.config['study']
        wd.find_element_by_xpath("//*[@class='icon-small icon-add']").click()
        wd.find_element_by_xpath("//*[@class='dropdown-menu inline-dropdown']/li/a[text()='%s']" % site['site1']).click()
        self.wait("//div[@id='page-title']//h1")

    def wait(self, elem_path, url_string = None):
        wd = self.app.wd
        while not (len(wd.find_elements_by_xpath(elem_path)) > 0):
            pass
        wd.implicitly_wait(3)
