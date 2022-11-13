import csv

# save each row into a list 
list_data = []
with open ("states_all.csv") as infile:
    #load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

print("List of dictionaries length is", len(list_data))

state_data = [row for row in list_data if row["STATE"] == "GEORGIA"]
print(len(state_data))

AVG_MATH_4_SCORE = [float(row["AVG_MATH_4_SCORE"]) for row in state_data if row ["AVG_MATH_4_SCORE"]!=""]


print("GA list length is", len(AVG_MATH_4_SCORE))
print("Our average math scores for Georgia are:", AVG_MATH_4_SCORE)


print("List of dictionaries length is", len(list_data))

all_state_data = [row for row in list_data if row["STATE"] == "GEORGIA"]
print(len(state_data))

AVG_MATH_4_SCORE = [float(row["AVG_MATH_4_SCORE"]) for row in state_data if row ["AVG_MATH_4_SCORE"]!=""]


print("GA list length is", len(AVG_MATH_4_SCORE))
print("Our average math scores for Georgia are:", AVG_MATH_4_SCORE)
