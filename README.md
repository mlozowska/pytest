# pytest-project
## This project contains:
#### 1) the calculator tests with the following methods: 
- adding
- subtraction
- square
- rest from division
- biggest common divisor (NWD)
- I've added 3-5 tests for every function (using multi-parameter)
#### 2) the factorial test
- with factorial method where 0!=1
#### 3) The printout of the report

</br>

#### Environment setup
1) pytest
```
pip install pytest
```
- pipevn vs venv vs conda/anaconda
- https://www.youtube.com/watch?v=HCVaqeQepno
2) Pipfile 
- https://www.youtube.com/watch?v=HCVaqeQepno

#### Running tests
```
python -m pytest _test_
```
or
```
pytest _test_
```
_test_ can be single test case, test method, test class or all tests

#### Test Reports
```
pip install pytest-html
pytest --html=report.html
```
- https://pypi.org/project/pytest-html/
- http://allure.qatools.ru/




#### Most common problems:
1) Incorrect/lack of environment path
2) Permission denied

#### Solutions
1) Add 2 paths to `System Environment Variables -> PATH`
- Python home folder (usually `C:\Users\x\AppData\Local\Programs\Python\Python_%version%`)
- Python Scripts folder ((usually `C:\Users\x\AppData\Local\Programs\Python\Python_%version%\Scripts`))
2) Open CMD or PowerShell `Run as administrator`
