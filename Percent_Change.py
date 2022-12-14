import csv

def perc_change_val(data, year1, column):
    for row in data:
        if row ["YEAR"] == year1:
            return row[column]


# save each row into a list 
list_data = []
with open ("states_all.csv") as infile:
    #load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

print("List of dictionaries length is", len(list_data))

state_data = [row for row in list_data if row["STATE"] == "GEORGIA"]
print(state_data[0])

AVG_MATH_4_SCORE = [row for row in state_data if row ["AVG_MATH_4_SCORE"]!=""]
year_data = []

for row in AVG_MATH_4_SCORE:
    print(row["YEAR"])

    year_data.append(row["YEAR"])
    print(year_data)


def perc_change_edu(data, year1, year2, column):
 """calculating the percent change between two year values

    Parameters
    ----------
    data : floats
       Data set we are pulling in`.
    year1:
        Previouse year value.
    year2:
        New year value.
    column:
        CSV file colum where value data is found.
    Returns
    -------
    float
        Percent change value in the form of a string.
    """
 old = float(perc_change_val(data, year1, column))
 new = float(perc_change_val(data, year2, column))

 score_change_val = ((old - new)/old) *100
 return (score_change_val)   

#print(float(x) - float(y))
#print("Our percent change for" +(year1)+ "&" +(year2) "is" +(str(perc_change_edu(AVG_MATH_4_SCORE, "2003", "2005", "AVG_MATH_4_SCORE")*-1)+"%"))

score_change_val=[]

for i in range(len(year_data)-1):
    year1 = year_data[i]
    year2 = year_data[i+1]
    print("Our percent change for " +(year1)+ " & " +(year2)+ " is " +(str(perc_change_edu(AVG_MATH_4_SCORE, year1, year2, "AVG_MATH_4_SCORE")*-1)+"%"))

    score_change_val.append((perc_change_edu(AVG_MATH_4_SCORE, year1, year2, "AVG_MATH_4_SCORE")*-1))
with open("Score_Percent_Change.csv", "w") as outfile:
    # load in data as DictReader
    writer = csv.writer(outfile)
  
    writer.writerow(year_data)
    writer.writerow(score_change_val)
