### Example of UI Testing Framework using Python, Pytest, Pytest-BDD, and Selenium.
![BCCC6EE0-EAE0-411F-A80C-92AC2DC73CF2](https://user-images.githubusercontent.com/10586980/129839352-b1641a35-cfc2-4da9-a02f-fcef6460d112.GIF)
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
