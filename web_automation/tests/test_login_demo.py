import pytest

@pytest.mark.smoke
def test_login_success(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in login_page.page.url.lower(), "Expected user to land on secure page."
    assert "You logged into a secure area!" in login_page.flash_text()


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("tomsmith", "wrong-password", "Your password is invalid!"),
        ("wrong-username", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
    ],
)
def test_login_failure_cases(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.flash_text()
    

@pytest.mark.regression
def test_close_flash_message(login_page):
    login_page.login("tomsmith", "wrong-password")

    assert "Your password is invalid!" in login_page.flash_text()
    login_page.flash_close()
    assert login_page.flash_message.is_hidden()

@pytest.mark.regression
def test_logout_success(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.logout()
    assert "login" in login_page.page.url.lower(), "Expected user to land on login page."
    assert "You logged out of the secure area!" in login_page.flash_text()

@pytest.mark.regression
def test_secure_page_requires_login_after_session_cleared(login_page):
    # Login first
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "/secure" in login_page.page.url.lower()

    # Secure page is accessible while logged in
    login_page.page.goto("https://the-internet.herokuapp.com/secure")
    assert "/secure" in login_page.page.url.lower()

    # Clear session and try secure page again
    login_page.page.context.clear_cookies() # Clear cookies
    login_page.page.goto("https://the-internet.herokuapp.com/secure") # Go to secure page again

    # Should be redirected to login with auth message
    assert "/login" in login_page.page.url.lower()
    assert "You must login to view the secure area!" in login_page.flash_text()