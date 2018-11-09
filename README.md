# Automated-Feed-Liker
Likes the pictures from your feed until 10 consecutive already liked pictures are detected. Also includes features such as user recognition.

## Prerequisites
* Selenium
* Python 2.7
* The latest version of chromedriver.

## How does it work?
In order to run the program, you'd have to insert your credentials to the:
```
id = ''
```
AND 
````
passd = ''
````
And where the chromedriver is installed (it should be in PATH).
```
driver = webdriver.Chrome(executable_path='')
   
eg driver = webdriver.Chrome(executable_path='/Users/bia/Documents/chromedriver')
```
