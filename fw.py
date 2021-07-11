import json
import os

from models.user import UserModel

_root_dir = os.path.dirname(os.path.abspath(__file__))


class Examples:
    """
    Available examples coming from http://the-internet.herokuapp.com/. This is expandable by adding more variables as
    they become available. The variables are set with the href link of the Element in test.
    """
    DYNAMIC_CONTENT = '/dynamic_content'
    HOVERS = '/hovers'
    LOGIN = '/login'


def get_user() -> UserModel:
    """
    Get the UserModel from users.json
    """
    with open(_root_dir + '/users.json', 'r') as json_file:
        _json = json.loads(json_file.read())
        return UserModel(**_json)
