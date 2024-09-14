import pytest
from pages.admin_page import AdminPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestAdminHeaders:
    def test_admin_headers(self):
        login_page = LoginPage(self.driver)
        admin_page = AdminPage(self.driver)

        # Log in as Admin
        login_page.login("Admin", "admin123")  # Replace with actual credentials

        # Step 1: Go to Admin page
        admin_page.go_to_admin_page()

        # Step 2: Validate the title
        assert self.driver.title == "OrangeHRM", "Page title mismatch."

        # Step 3: Validate the presence of headers
        headers = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking",
                   "Configuration"]
        for header in headers:
            assert admin_page.is_header_present(header), f"Header '{header}' is not present."
