import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestForgotPassword:
    def test_forgot_password(self):
        login_page = LoginPage(self.driver)

        # Step 1: Click on "Forgot your password?" link
        login_page.click_forgot_password()

        # Step 2: Enter username/email
        login_page.enter_reset_username("Admin")  # Replace "Admin" with the actual username

        # Step 3: Submit reset password request
        login_page.click_reset_password()

        # Verify expected result
        success_message = login_page.get_reset_success_message()
        assert "Reset Password link sent successfully" in success_message, "Password reset failed."
