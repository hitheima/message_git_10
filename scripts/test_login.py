import pytest


class TestLogin:

    def test_login1(self):
        print("test_login1")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login2(self):
        print("test_login2")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login3(self):
        print("test_login3")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_login4(self):
        print("test_login4")
        assert 1