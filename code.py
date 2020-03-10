# --------------
#  Read the data of the format .yaml type
import json
# using with open command to read the file
with open(path) as f:
    data = json.load(f)
print(data)


#  Women who got the first Nobel Prize?
female = ['Full Name']
for i in range(len(data)):
    if((data[i]["Sex"] == 'Female')):
        for j in female:
            print(j ,':', data[i][j])
        print("\n")   
        break     

#  How many have come from india?
indian = ['Category','Full Name','Birth Country','Death Country','Sex']
for i in range(len(data)):
    if(data[i]["Birth Country"] == "India") or (data[i]["Death Country"] == "India") or (data[i]["Birth Country"] == "British India (India)"):
        for j in indian:
            print(j ,':', data[i][j])
        print("\n")        
#  Calculate category wise number of prizes for the people who came from India?
Nobel_category=['Medicine','Literature','Physics','Economics','Chemistry','Peace']
category = {}

for i in Nobel_category:
    cat_len=0
    for j in range(len(data)):
        if((data[j]["Birth Country"] == "India") or (data[j]["Death Country"] == "India") or (data[j]["Birth Country"] == "British India (India)")) and (data[j]["Category"]==i):
            cat_len=cat_len+1
    category[i]=cat_len
print(category)  
#   Which country has produced the highest number of Nobel winners for category `Chemistry`?
from collections import Counter
import operator

country = []
for i in range(len(data)):
    if (data[i]["Category"] == "Chemistry"):
        country.append(data[i]['Birth Country'])
b = country

c=Counter(b)
max_nobel_winners=max([i for i in c.values()]) 
print("Highest count of Noble Winners: ", max_nobel_winners)

max_country=[name for name, count in c.items() if count == max_nobel_winners]
print("The Country that has produced highest number of Nobel Winners: ",max_country[0])

#  Which Organization won the most nobel prizes in the category "Physics" and "Chemistry" ?

organization = []
category=['Physics','Chemistry']
for i in range(len(data)):
    for j in category:
        if (data[i]["Category"] == j):
            organization.append(data[i]['Organization Name'])
o = organization

c=Counter(o)
max_nobel_prizes=max([i for i in c.values()]) 
print("Count of Noble Prizes for Physics and Chemistry: ", max_nobel_prizes)

max_organization=[name for name, count in c.items() if count == max_nobel_prizes]
print("The Organization that has produced highest number of Nobel Winners: ",max_organization[0])


#  What was the Motivation for awarding the Nobel Prize for Marie Curie, nÃ©e Sklodowska?
indian = ['Motivation']
for i in range(len(data)):
    if(data[i]["Full Name"] == "Marie Curie, nÃ©e Sklodowska"):
        for j in indian:
            print(j ,':', data[i][j])
        print("\n")    


#  In which category people got Noble Prize in the year 1994?
indian = ['Category','Full Name']
for i in range(len(data)):
    if(data[i]["Year"] == 1994):
        for j in indian:
            print(j ,':', data[i][j])
        print("\n")  



