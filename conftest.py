import pytest

@pytest.fixture(scope = "session")
def browser():
    print("Открываем браузер")
    yield
    print("Закрываем браузер")