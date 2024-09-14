import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def setup(request):

    # Set up WebDriver
    driver = webdriver.Chrome(executable_path="C:\\Users\\VRM\\OneDrive\\Documents\\project 2 Orange\\testdata.csv")
    driver.maximize_window()

    # Access the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Assign the WebDriver instance to the class that calls this fixture
    request.cls.driver = driver

    # Yield to allow the tests to execute, then quit the driver after tests are done
    yield
    driver.quit()
