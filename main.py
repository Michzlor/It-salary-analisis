import pandas as pd
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8" ,"9"]
drop_count = 0
data_frame = pd.read_csv("Salary Dataset.csv")

def cut_prefix(a):
    prefix = ""
    for i in range(len(a)):
        if a[i] in num:
            break
        else:
            prefix += a[i]
    a = (a.replace(prefix,""))
    return a, prefix


for idx in data_frame.index:
    try:
        cell = cut_prefix(data_frame.loc[idx, "Salary"])

        val = cell[0].split(sep="/")[0]
        val = "".join(val.split(sep=","))

        if cell[0].split(sep="/")[1] == "yr" :
            pass
            data_frame.loc[idx, "Salary"] = int(val)
        elif cell[0].split(sep="/")[1] == "mo" :
            pass
            data_frame.loc[idx, "Salary"] = int(val) * 12
        else:
            drop_count += 1
            data_frame.drop(idx, inplace=True)
    except Exception as e:
        print(e)
        data_frame.drop(idx, inplace=True)

print(data_frame)


print(data_frame.loc[11, "Salary"])