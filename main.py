import pandas as pd
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8" ,"9"]
drop_count = 0
data_frame = pd.read_csv("Salary_Dataset.csv")
currency_list = []

def cut_prefix(a):
    prefix = ""
    for i in range(len(a)):
        if a[i] in num:
            break
        else:
            prefix += a[i]
    a = (a.replace(prefix,""))
    return a, prefix

#DONE#Avarge salary on each position in given city
#temp df for given city + temp df for each position return [(psition_name,mean)]
def avarge(df, city):
    temp_ = []

    for idx in df.index:
        if df.loc[idx, "Location"] == city:
            temp_.append(df.loc[idx])
    df_city = pd.DataFrame(temp_, columns=df.columns)

    job_titles = []
    for idx in df_city.index:
        if df_city.loc[idx, "Job Title"] in job_titles:
            pass
        else:
            job_titles.append(df_city.loc[idx, "Job Title"])

    result = []
    for job in job_titles:
        temp_ = []
        for idx in df_city.index:
            if df_city.loc[idx, "Job Title"] == job:
                temp_.append(df_city.loc[idx])
            else:
                continue
        df_job = pd.DataFrame(temp_, columns=df.columns)
        result.append((job, df_job.mean(numeric_only=True)["Salary"]))
    temp_ = None
    return result, job_titles, df_city
#DONE#List 3 best paying companys in givrn city
#temp df for givrn city sort by salary print first 3 company names
def top_employers(df, city):
    temp_ = []

    for idx in df.index:
        if df.loc[idx, "Location"] == city:
            temp_.append(df.loc[idx])
    df_city = pd.DataFrame(temp_, columns=df.columns)
    df_city_sorted = df_city.sort_values(by="Salary", ascending=False)
    temp_ = df_city_sorted.head(3)

    return temp_
#How much(%) highier are salaries in top 3 than avarge of given position
def top3_employers(top3, avr):
    for idx in top3.index:
        for idx1 in range(len(avr)):
            if top3.loc[idx, "Job Title"] == avr[idx1][0]:
                diff = top3.loc[idx, "Salary"]/ avr[idx1][1]
                diff = diff*100
                print(round(diff, 2),"%")
            else:
                continue
#Recomend best paying positon in each company return [(Company Name, Job Title)]
def recomedation(df, job_titles):
    company_list = []
    result = []
    for idx in df.index:
        if df.loc[idx, "Company Name"] in company_list:
            pass
        else:
            company_list.append(df.loc[idx, "Company Name"])
    for company in company_list:
        temp_ = []
        for job in job_titles:
            job_max = 0
            for idx in df.index:
                if df.loc[idx, "Salary"] > job_max and df_city.loc[idx, "Job Title"] == job:
                    job_max = df.loc[idx, "Salary"]
            temp_.append(job, job_max)

for idx in data_frame.index:
    try:
        cell = cut_prefix(data_frame.loc[idx, "Salary"])

        val = cell[0].split(sep="/")[0]
        val = "".join(val.split(sep=","))

        if cell[0].split(sep="/")[1] == "yr" :
            pass
            data_frame.loc[idx, "Salary"] = int(val)
            currency_list.append(cell[1])
        elif cell[0].split(sep="/")[1] == "mo" :
            pass
            data_frame.loc[idx, "Salary"] = int(val) * 12
            currency_list.append(cell[1])

        else:
            drop_count += 1
            data_frame.drop(idx, inplace=True)
    except Exception as e:
        print(e)
        data_frame.drop(idx, inplace=True)

currency_series = pd.Series(currency_list)
data_frame["Currency"] = currency_series
currency_list = []
data_frame["Salary"] = pd.to_numeric(data_frame["Salary"])
print("Avarge salary in Banglore")
avr = (avarge(data_frame, "Bangalore"))
print(avr[0])
print("----------------------------------------------------------------------")
print("Top 3 paying companies in Banglore")
top3 = top_employers(data_frame, "Bangalore")
print(top3)
print("----------------------------------------------------------------------")
print("How much more are they paying")
top3_employers(top3, avr[0])
print("----------------------------------------------------------------------")
recomedation(avr[2], avr[1])