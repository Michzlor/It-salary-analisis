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
def avarge_salary(df, city):
    result = []
    for location, city_db in data_frame.groupby("Location"):
        if location == city:
            for job, subdb in city_db.groupby("Job Title"):
                subdb = subdb.mean(numeric_only=True)
                result.append((job, int(subdb.loc["Salary"])))
            break
        else:
            continue

    return result
#DONE#List 3 best paying companys in givrn city
#temp df for givrn city sort by salary print first 3 company names
def top_employers(df, city):
    result = []
    for location, city_df in df.groupby('Location'):
        if location == city:
            city_df = city_df.sort_values(['Salary'], ascending=False)
            top3 = city_df.head(3)

        else:
            continue
    for row in top3.itertuples():
        for job, subdb in city_df.groupby("Job Title"):

            if row[2] == job:
                subdb = subdb.mean(numeric_only=True)
                diff = ((float(row[5]) / float(subdb.loc["Salary"])) * 100)
                result.append((row[1], job, row[5], str(int(diff))+"%"))

    return result

#How much(%) highier are salaries in top 3 than avarge_salary of given position
def top3_comapred_to_avarge(df, city):
    result = []
    for location, city_df in df.groupby('Location'):
        if location == city:
            city_df = city_df.sort_values(['Salary'], ascending=False)
            top3 = city_df.head(3)

        else:
            continue

    for row in top3.itertuples():
        for job, subdb in city_df.groupby("Job Title"):

            if row[2] == job:
                subdb = subdb.mean(numeric_only=True)
                diff = ((float(row[5]) / float(subdb.loc["Salary"])) * 100)
                result.append((row[1], job, str(round(diff, 2))+"%"))

            else:
                continue
    return result

#Recomend best paying positon in each company return [(Company Name, Job Title)]
def recomedation(df, city):

    result = []
    for location, city_df in df.groupby('Location'):
        if location == city:
            for company, subdf in city_df.groupby('Company Name'):
                subdf = subdf.sort_values(['Salary'], ascending=False)
                temp = subdf.iloc[0]
                result.append((temp.loc["Company Name"], temp.loc["Job Title"],temp.loc["Salary"]))
            break
        else:
            continue
    return result



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



data_frame["Salary"] = pd.to_numeric(data_frame["Salary"])

# print("Avarge")
# print(avarge_salary(data_frame, "Hyderabad"))
# print("----------------------------------------------------------------------")
# print("Top 3")
# print(top_employers(data_frame, "Hyderabad"))
# print("----------------------------------------------------------------------")
# print("Top 3 vs avarge")
# print(top3_comapred_to_avarge(data_frame, "Hyderabad"))
# print("----------------------------------------------------------------------")
# print("Recomendation")
# print(recomedation(data_frame, "Hyderabad"))


