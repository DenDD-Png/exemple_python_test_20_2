import pytest

@pytest.fixture
def login_page(browser):
    print("Вводим логин")

@pytest.fixture
def user():
    print("Тест юзер")
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert_username = "username"
    assert_password = "password"

