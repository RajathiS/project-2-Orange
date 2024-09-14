from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.forgot_password_link = (By.LINK_TEXT, "Forgot your password?")
        self.username_input = (By.ID, "txtUsername")
        self.reset_password_button = (By.ID, "btnSearchValues")
        self.success_message = (By.ID, "successMessage")  # Replace with correct locator

    def click_forgot_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.forgot_password_link)
        ).click()

    def enter_reset_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def click_reset_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reset_password_button)
        ).click()

    def get_reset_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        ).text
