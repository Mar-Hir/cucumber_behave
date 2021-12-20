# cucumber_behave
This repository contains automated tests written for [page](http://automationpractice.com/index.php) using Behave.

## Requirements and setup
This code requires `Python 3.6+`, `selenium` and `behave` package. You can install it by running: 
```
pip install behave selenium
```
The tests were executed with Behave ver. 1.2.6 and Selenium ver. 3.141.0.
In order to execute you also need to set environment variable containing path to your chrome driver:
```
set CHROME_EXE_PATH=<your_path>//chromedriver.exe
```

## Running tests
To run the test execute in the root of your repository:
```
behave
```
