from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
import json
import requests
import main
import re

def currency_exchenge(current_currency, currency_to_exchenge_to, df):
    if current_currency == currency_to_exchenge_to:
        return currency_to_exchenge_to
    else:
        for idx in df.index:
            val = df.loc[idx, "Salary"]
            if current_currency == "PLN":
                df.loc[idx, "Salary"] = round(val / exchenge_rates[currency_to_exchenge_to], 0)
            elif currency_to_exchenge_to == "PLN":
                df.loc[idx, "Salary"] = round(val * exchenge_rates[current_currency], 0)


            else:
                temp = val * exchenge_rates[current_currency]
                df.loc[idx, "Salary"] = round(temp / exchenge_rates[currency_to_exchenge_to], 0)
        return currency_to_exchenge_to
def normaliize_currency(df):
    for idx in df.index:
        if df.loc[idx, "Currency"] != current_currency[0]:
            val = df.loc[idx, "Salary"]
            df.loc[idx, 'Salary'] = round(val / exchenge_rates[df.loc[idx, "Currency"]])
            df.loc[idx, "Currency"] = current_currency[0]


city_list = main.data_frame.Location.unique().tolist()

result = []

app = Flask(__name__)
app.secret_key = "blah"
if __name__ == 'app':
    main.clean_data(main.data_frame)
    current_currency = [main.data_frame.Currency.mode()[0]]
    content = json.loads(requests.get(url="https://api.nbp.pl/api/exchangerates/tables/a/?format=json").text)
    with open("rates.json", "w") as f:
        json.dump(content, f , indent=3)
    exchenge_rates = {"INR": content[0]['rates'][29]['mid'], "USD": content[0]['rates'][1]['mid'],
                      "EUR": content[0]['rates'][7]['mid'], "GBP": content[0]['rates'][10]['mid']}
    currency_list = ["PLN"]
    for k in exchenge_rates.keys():
        currency_list.append(k)
    normaliize_currency(main.data_frame)
print(main.data_frame.Currency.unique().tolist())
@app.route('/', methods=['POST', 'GET'])
def index():
    """strona startowa"""

    if request.method == 'POST':
        print(request.form)
        currency = (request.form.get("currency"))
        flash(f"{current_currency[0]} exchanging to {currency}")
        print(currency)
        print(current_currency[0])
        current_currency[0] = currency_exchenge(current_currency[0], currency, main.data_frame)

    return render_template("index.html", city_list=city_list, currency_list=currency_list)


@app.route('/<city>/', methods=['POST', 'GET'])
def output(city):
    """wyswitlenie danych dla miasta wpisanego w URL"""
    if city in city_list:
        result = []
        result.append(main.avarge_salary(main.data_frame, city))
        result.append(main.top_employers(main.data_frame, city))
        result.append(main.top3_comapred_to_avarge(main.data_frame, city))
        result.append((main.recomedation(main.data_frame, city)))

    else:
        flash(f'"{city}" not found in dataset')
        return render_template("index.html", city=city, result=[], city_list=city_list, currency_list=currency_list)
    return render_template("city.html", city=city, result=result, city_list=city_list, currency_list=currency_list,
                           currency=current_currency[0])


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




