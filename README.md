# Project Name

Project name is Usana. Automation framework using [Pylenium](https://docs.pylenium.io/), a Selenium wrapper that bring 
the best of Selenium, Cypress and Python into one package. This will allow automation around Cypress known 
[limitations](https://docs.cypress.io/guides/references/trade-offs.html#Permanent-trade-offs-1) while still being true
to the mission of getting to writing tests faster. 

## Prerequisites

- [Python 3.x.x](https://www.python.org/downloads/)

## Installing Pylenium

1. Create a Virtual Environment
    ~~~
    $ python --version
    should print 3.x.x
     
    $ python -m venv "venv"
    ~~~
   
    *Note: On Macs create a Virtual Environment with*
   ~~~
   $ sudo pip install pipenv
   ~~~
   
    To check if you have Python 3x versions on a Mac, type:
    ~~~
        $ python3 --version
        should print 3.x.x
    ~~~
   
    Otherwise, you can manually configure your IDE to use the Virtual Environment as in this example from Pycharm:
    ~~~
    1. Open Preferences (or Settings)
    2. Open Project > Project Interpreter
    3. Select the venv for your Project in the Project Interpreter dropdown
    4. Click APPLY, then OK
    ~~~
2. Install Pylenium
    ~~~
    Terminal $ (venv)
    pipenv install pyleniumio
    ~~~
   - pip may also be used
3. Initialize Pylenium
    ~~~
    Terminal $ (venv)
    pylenium init
    ~~~
   Pylenium comes packaged with Pytest which it uses as the testing framework.
4. Select Pytest as the Test Framework

    This will give you
    - Intellisense
    - Autocomplete
    - Run/Debug Test functionality with breakpoints
    - More depending on IDE
    
    Example from Pycharm:
    ~~~
    1. Open Preferences (or Settings)
    2. Open Tools > Python Integrated Tools
    3. Select pytest in the "Default test runner" dropdown
    ~~~

## Running Tests

If you're using PyCharm, there should be a green Play button next to the test definition. Click it and select either Run
to execute normally or Debug to use breakpoints in Debug Mode. Otherwise, use the method your IDE provides. 

You can always use the CLI as well:
~~~
Terminal $ (venv)
python pytest tests/
~~~
*Note: In case of test failure of UI tests, test_results file will contain a snapshot of point of failure in UI.*

### Simple CLI

Pylenium comes with pytest and the pyest-xdist plugin to run tests concurrently. All you need to do is use the 
-n [NUMBER] option when running the tests in the CLI.
~~~
Terminal $ (venv) 
pytest tests/ -n 2
~~~
*Note: Runs 2 tests concurrently.*

### Run Tests in Containers

Regardless of the scaling option you go with (Selenoid, Zalenium, Docker vs Kubernetes, etc.), you will need to connect
your tests to a Remote URL.

You can do this two ways:
- Update remote_url in pylenium.json
- Pass in the argument when running the tests in the CLI

#### Run Tests in CLI
~~~
Terminal $ (venv) # example
pytest tests/ -n 2 --remote_url="http://localhost:4444/wd/hub"
~~~
*Note: This is the most common option.*

#### Update pylenium.json
~~~
pylenium.json
"remote_url": "http://localhost:4444/wd/hub"
~~~

### Config Layers

- Layer 1 - pylenium.json is deserialized into PyleniumConfig
- Layer 2 - If there are any CLI args, they will override their respective values in PyleniumConfig

