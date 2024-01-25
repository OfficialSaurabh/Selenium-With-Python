import pytest
@pytest.fixture()
def setUp():
    print("Running confest method setup")
    yield
    print("Running confest method tearDown")

@pytest.fixture(scope="class")
def OneTimesetUp(request, browser, osType):
    print("Running conftest method one time setup")
    if browser == "firefox":
        value = 10
        print("Running on firefox")
    else:
        value = 20
        print("Running on chrome")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running conftest method one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")