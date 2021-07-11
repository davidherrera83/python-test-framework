import pytest

from fw import Examples


@pytest.mark.parametrize('available_example',
                         [
                             Examples.DYNAMIC_CONTENT,
                             Examples.HOVERS,
                             Examples.LOGIN
                         ]
                         )
def test_available_examples(herokuapp, py, available_example):
    """
    Available Examples in main page are visible. By parametrizing each example, more tests may be created as the list of
    available examples are added to the site. each test uses the same test logic, but counts as individual tests.
    :param
    herokuapp: Instance of HerokuApp
    py: Instance of Pylenium driver
    available_example: Instance of Examples found in fw.py
    """
    herokuapp.visit_herokuapp()
    assert py.get('a[href=' + f'"{available_example}"').should().be_visible()


def test_dynamic_content(herokuapp, py):
    """
    Element in dynamic content contains text.
    :param
    herokuapp: Instance of HerokuApp
    py: Instance of Pylenium driver
    """
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.DYNAMIC_CONTENT)
    py.should().have_title('The Internet')
    dynamic_content = len(py.get('.example #content').children()[0].children()[1].text())
    assert dynamic_content > 1


def test_hover(herokuapp, py):
    """
    Hover on an Element to reveal Element in test.
    :param
    herokuapp: Instance of HerokuApp.
    py: Instance of Pylenium driver.
    """
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.HOVERS)
    py.get('.figure [src*=avatar]').hover()
    assert py.get('.figure .figcaption').should().contain_text('user1')


def test_secure_login(herokuapp, py):
    """
    Users are able to authenticate via secure login page
    :param
    herokuapp: Instance of HerokuApp.
    py: Instance of Pylenium driver.
    """
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.LOGIN)
    herokuapp.secure_login()
    assert py.get('#flash').should().be_visible()
