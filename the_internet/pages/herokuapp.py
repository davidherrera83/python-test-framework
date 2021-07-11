from pylenium.driver import Pylenium
from models.user import UserModel


class HerokuApp:
    """
    Herokuapp Wrapper
    Args:
        py: Instance of Pylenium Driver to use for this session.
        user: Instance of UserModel to use for this session.
    """
    def __init__(self, py: Pylenium, user: UserModel):
        self.py = py
        self.user = user

    def visit_herokuapp(self):
        """
        Using Pylenium driver(py), visit http://the-internet.herokuapp.com/
        """
        self.py.visit('http://the-internet.herokuapp.com/')
        return self

    def click_on_example(self, available_example: str):
        """
        Clicks on an Element
        :param
        available_example: Instance of Examples variables in fw.py for each test.
        """
        self.py.get('a[href=' + f'"{available_example}"').click()
        return self

    def secure_login(self):
        self.py.get('#username').type(self.user.username)
        self.py.get('#password').type(self.user.password)
        self.py.get('.fa.fa-2x.fa-sign-in').click()
        return self



