# Company API
A project to scraping, storing and serving data as an API.

## Preparation    
### Install virtualenvironment
Assuming you have pip3 on your machine  
```
$ sudo pip3 install virtualenv 
```
create virtual environment with python3  
```
$ virtualenv -p python3 venv
```
activating your virtual environment
```
$ source venv/bin/activate
```
deactivating it later
```
$ deactivate
```

### Install required library  
```
$(venv) pip install -r requirements.txt  
```
Environment preparations  
```
$(venv) export FLASK_app=run:app  
$(venv) export FLASK_ENV=development
```

## Data Scraping  
On the project root, run this command  
```
$(venv) python3 app/runnable/company_scrape.py
```
wait for it. When it's done, please see if company_index.json file is created/updated under dir: app/static/data/  
then try to run the project


## Running flask project

run it
```
$(venv) flask run
```
You can stop it by using  CTRL + C  anytime

On the other terminal, try this
## Storing the saved json file into database
```
$ curl --data "secretkey=inirahasia" http://localhost:5000/db_update
```
Please notice that this secretkey is just for dummy/development usage. This kind of auth should not be used in production. My suggestion is you can use something more secure than this, like JWT or other token-based authentication.

## Getting served data  
### All company profile  
```
GET http://localhost/companies  
```
### Get Company based on their name  
```
http://localhost:5000/companies?company_name=<string>
```
### Get company based  on their industry  
```
http://localhost:5000/companies?industry=<string>
```
