class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        #login to main dashboard
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("WebLogin$UserName").clear()
        wd.find_element_by_name("WebLogin$UserName").send_keys(username)
        wd.find_element_by_name("WebLogin$Password").clear()
        wd.find_element_by_name("WebLogin$Password").send_keys(password)
        wd.find_element_by_name("WebLogin$Login").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@class='pull-left name']/label").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)



