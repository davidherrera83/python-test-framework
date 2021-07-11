from pylenium.driver import Pylenium


class HerokuApp:
    def __init__(self, py: Pylenium):
        self.py = py

    def click_on_example(self, example):
        """
        Clicks on an Element
        :param
        example: 
        :return:
        self
        """
        self.py(f'{example}').click()
        return self
