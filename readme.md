### Example of UI Testing Framework using Python, Pytest, Pytest-BDD, and Selenium.
### How to Build/Run locally:
#### clone repo:
```
git clone https://github.com/Tolstr/python-pytest-gherkin-bdd.git
cd python-pytest-gherkin-bdd
```
#### Dependencies 
1. In order to run you have to install Python3.6+
2. You need to have pip installed
3. install python3 - pip  https://www.python.org/downloads/
5. Chrome Browser https://www.google.com/chrome
6. Chrome driver needs to be in the path https://chromedriver.chromium.org/downloads
7. Getting dependencies:
```
$ pip install virtualenv
$ python3 virtualenv env
$ env/Scripss/activate (for win)
$ source env/bin/activate (for mac-linux)
$ pip install -r requirements.txt
```
#### Running  tests
* Headful is default run
```
pytest 
```
* in order to run Headless 
```
pytest --headless true
```
