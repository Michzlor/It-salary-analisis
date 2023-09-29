# It salary analisis
[readme in PL](https://github.com/Michzlor/It-salary-analisis/blob/master/readmePL.md)

### 1.Summary
Comparison of annual salaries on various IT positions in some major in India

Dataset used for the app:
https://www.kaggle.com/iamsouravbanerjee/analytics-industry-salaries-2022-india
User picks a city - Bangalore, Pune, Hyderabad, New Delhi, Mumbai
App returns:
- Avarge annual salary for each recorded position in chosen city
- Top 3 best paying companies in chosen city and how much percentage wise are they paying
- Recommended position in each company based on highest salary
## 2.Instalation
#### Requierments:
-Python version 3.9.13 or higher
#### Manual instalation:

1. Create directory for the application
2. Copy all files from the repository to directory You created
#### Instalation with Git:
In command line execute :
>git clone https://github.com/Michzlor/It-salary-analisis

It will create a directory named analiza-zarobków in your active directory(default: C/Users/username)

## 3.Start-up

1. Creating virtual environment
In command line execute
>  python -m venv env
2. Activating virtual environment
>  env/Scripts/activate
3. Instalation of packets and libraries used by app
> pip install -r requirements.txt
4. Booting server for app. By default server runs on local host adress: http://127.0.0.1:5000
> flask run
