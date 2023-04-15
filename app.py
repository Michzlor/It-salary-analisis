from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import main
import re
city_list = main.data_frame.Location.unique().tolist()
result = []

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        city = (request.form.get("city"))
        result = []
        result.append(main.avarge_salary(main.data_frame, city))
        result.append(main.top_employers(main.data_frame, city))
        result.append(main.top3_comapred_to_avarge(main.data_frame, city))
        result.append((main.recomedation(main.data_frame, city)))
        print("result: ", city, result[:2])
        return render_template("city.html", city=city, result=result, city_list=city_list)


    else:
        print("turd")
    return render_template("city.html", city_list=city_list, result= [], city="Analiza zarobków")


@app.route('/<city>/', methods=['POST', 'GET'])
def output(city):
    return render_template("city.html", city=city, result=result)

@app.route('/summaryJ/<querry>/<city>')
def summaryJ(querry, city):
    print(querry, city)
    for location, city_db in main.data_frame.groupby("Location"):
        if location == city:
            for job, subdb in city_db.groupby("Job Title"):
                if job == querry:
                    pass
        else:
            continue
    print(subdb)
    for i in subdb.describe(include="all").itertuples():
        print(i)
    return render_template("summary.html", querry= querry, content= subdb.describe(include="all").itertuples())

@app.route('/summaryC/<querry>/<city>')
def summaryC(querry, city):
    print(querry, city)
    for location, city_db in main.data_frame.groupby("Location"):
        if location == city:
            for company, subdb in city_db.groupby("Company Name"):
                if company == querry:
                    pass
        else:
            continue
    print(subdb)
    for i in subdb.describe(include="all").itertuples():
        print(i)
    return render_template("summary.html", querry= querry, content= subdb.describe(include="all").itertuples())