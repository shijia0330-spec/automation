from playwright.sync_api import Page, Response


class LoginPage:
    URL = "https://rahulshettyacademy.com/client"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#userEmail")
        self.password_input = page.locator("#userPassword")
        self.login_button = page.locator("#login")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password) -> Response:
        self.username_input.fill(username)
        self.password_input.fill(password)

        with self.page.expect_response(
            lambda response: (
                "/api/ecom/auth/login" in response.url
                and response.request.method == "POST"
            )
        ) as response_info:
            self.login_button.click()

        return response_info.value