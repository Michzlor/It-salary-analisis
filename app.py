from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
import main
import re

city_list = main.data_frame.Location.unique().tolist()

result = []

app = Flask(__name__)
app.secret_key = "blah"
if __name__ == 'app':
    main.clean_data(main.data_frame)


@app.route('/', methods=['POST', 'GET'])
def index():
    """strona startowa"""

    return render_template("index.html", city_list=city_list)


@app.route('/<city>/', methods=['POST', 'GET'])
def output(city):
    """wyswitlenie danych dla miasta wpisanego w URL"""
    if city in city_list:
        result = []
        result.append(main.avarge_salary(main.data_frame, city))
        result.append(main.top_employers(main.data_frame, city))
        result.append(main.top3_comapred_to_avarge(main.data_frame, city))
        result.append((main.recomedation(main.data_frame, city)))
        print("result: ", city, result[:2])
    else:
        flash(f'"{city}" not found in dataset')
        return render_template("index.html", city=city, result=[], city_list=city_list)
    return render_template("city.html", city=city, result=result, city_list=city_list)


@app.route('/summaryJ/<querry>/<city>')
def summaryJ(querry, city):
    """"podsumowanie po kliknieciu na nazwe stanowiska"""
    for location, city_db in main.data_frame.groupby("Location"):
        if location == city:
            for job, subdb in city_db.groupby("Job Title"):
                if job == querry:
                    out = subdb.describe(include="all").itertuples()
        else:
            continue
    cols = (main.data_frame.columns)
    return render_template("summary.html", querry=querry, content=out, cols=cols, city=city, city_list=city_list)


@app.route('/summaryC/<querry>/<city>')
def summaryC(querry, city):
    """"podsumowanie po kliknieciu na nazwe firmy"""
    for location, city_db in main.data_frame.groupby("Location"):
        if location == city:
            for company, subdb in city_db.groupby("Company Name"):
                if company == querry:
                    out = subdb.describe(include="all").itertuples()
        else:
            continue
    cols = (main.data_frame.columns)
    return render_template("summary.html", querry=querry, content=out, cols=cols, city=city, city_list=city_list)
