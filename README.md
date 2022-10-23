# api_automation

This is API automation project for sample project, using API in this link: `https://reqres.in/`
The postman collection for manual cases is stored in folder: postman_testcases

## Getting started
- This automation solution is built in Visual code, so the guideline below is applied for VS code
- Install python for your machine, the link is here: `https://www.python.org/downloads/`
- If your python is install successfully, you can check it by run this cmd in terminal: `python --version`
- Install pipenv for your machine, you can find download file and install in this link: `https://pipenv.pypa.io/en/latest/`
- Activate your virtual env with pipenv using this cmd: `PIPENV_VENV_IN_PROJECT=1 pipenv shell`
- After virtual env is activates successfully, please select interpreter for your project is this environment and select test is pytest
- Run below cmd to install required packages to start: 
`pip install requests`
`pip install pytest`
`pip install black`
`pip install pytest-xdist`
`pip install pytest-html`
- When all these steps are done, please run this cmd to ensure everything is setup correctly: `pytest --version`
- Run all tests and generate html report with this cmd: `pytest testcases --html=report.html --self-contained-html`
- Run parallels using this cmd:  `pytest -n 2`

## The reason why I'm choosing python and pytest:
- Python code is shorter and more flexible than Java
- Python community now is also huge, so it's easy to search for solution on line
- Compare with Java testNg, Python has pytest, this testing framework is very powerfull, and lots of plugins to support. For example, to running parameters tests, I only need to mark tests run with parameters. Another is running parallel with pytest is extremely easy compare with testNg, I just need to install pytest-xdist plugin and declare threads 
- Another reason, I really like python is its flexibility in data type initiation, for Eg. this variable: string = "This is a string" this will be automatically understood by Python compiler, but with Jav I need to write it clearly
- But there are some thing I need to work around like: Python has not switch statement, and it has no matrix type either, so in theses cases, I need to find work around solutions for them
- Another think is why I'm using pipenv, because this is one package management tool for Python, it helps activate and deactivate virtual environment automatically.
- I'm using VS code, sometimes the combination of VS code, Python, Pytest, Pipenv are not always smoothly so the setup part need to do quite carefully
- The setup part is for Mac machine, but I tried with friend Windows machine and the steps are very similar, also run this on Gitlab CICD (Linux environment) and it still works :)
 
 ## The code structure
 - For API automation solution, I have 3 main parts: 
     + The first part is `base` part -> This part will help to build model of test cases. 
     + This solution is for demo only, in real world cases, will be authentication part to get token for API
     + The second part is `testcases` part -> This will help to code test cases of our API
     + The third part is `utils` part -> this will include helper class to help use store some information like Route, base_URL, logging, data_test
 
