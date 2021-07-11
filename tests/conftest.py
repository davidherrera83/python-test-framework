import pytest

import fw
from models.user import UserModel
from the_internet.pages.herokuapp import HerokuApp


@pytest.fixture
def user() -> UserModel:
    """Instance of user which reads from users.json to set user for each test."""
    _user = fw.get_user()
    return _user


@pytest.fixture
def herokuapp(py, user) -> HerokuApp:
    """Instance of HerokuApp for each test."""
    return HerokuApp(py, user)
