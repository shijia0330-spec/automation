class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page): # constructor
        self.page = page # instance variable
        self.username_input = page.locator("#username") # locators
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")
        self.flash_close_button = page.locator("#flash a.close")
        self.logout_link = page.locator("a.button.secondary.radius")
   

    def logout(self):
        self.logout_link.click()
        self.flash_message.wait_for(state="visible")
    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def flash_text(self) -> str: # getter method
        return self.flash_message.inner_text()


    def flash_close(self):
        self.flash_close_button.click()
        self.flash_message.wait_for(state="hidden")

    