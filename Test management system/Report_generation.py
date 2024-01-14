absent_data={'22-02-2022': [2210713, 2210699], '23-02-2022': [2210713], '24-02-2022': [2210699], '25-02-2022': [2210699], '26-02-2022': [], '27-02-2022': [], '03-03-2022': [2210699], '04-03-2022': [], '05-03-2022': [2210699, 2210713], '06-03-2022': [], '07-03-2022': [], '08-03-2022': [], '23-03-2022': [], '24-03-2022': [2210713], '25-03-2022': [], '26-03-2022': [], '27-03-2022': [], '28-03-2022': [2210699]}

timetable={'CAT1': [['22-02-2022', 'Maths', 'MA'], ['23-02-2022', 'English', 'EN'], ['24-02-2022', 'Python', 'PY'], ['25-02-2022', 'Physics', 'PHY'], ['26-02-2022', 'Chemistry', 'CHEM'], ['27-02-2022', 'Graphics', 'EG']], 'CAT2': [['03-03-2022', 'Maths', 'MA'], ['04-03-2022', 'English', 'EN'], ['05-03-2022', 'Python', 'PY'], ['06-03-2022', 'Graphics', 'EG'], ['07-03-2022', 'Physics', 'PHY'], ['08-03-2022', 'Chemistry', 'CHEM']], 'END SEM': [['23-03-2022', 'English', 'EN'], ['24-03-2022', 'Maths', 'MA'], ['25-03-2022', 'Python', 'PY'], ['26-03-2022', 'Physics', 'PHY'], ['27-03-2022', 'Chemistry', 'CHEM'], ['28-03-2022', 'Graphics', 'EG']]}

all_data={2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'gmail', 'Ph_no': '99441', 'Marks': [[43, 44, 45, 46, 47, 48], [12, 13, 14, 15, 16, 17], [50, 49, 48, 
47, 46, 45]]}, 2210699: {'Name': 'Prani', 'Section': '1', 'Email': '2', 'Ph_no': '3', 'Marks': [[4, 12, 3, 2, 2, 3], [2, 2, 2, 2, 3, 4], [2, 2, 2, 3, 2, 1]]}}

#a)List of students who were absent for 3 or more tests for each CAT

reg_nos=list(all_data.keys())
exams = list(timetable.keys())
x=timetable['CAT1']
y=[]
for i in x:
    y.append(i[0])
print (y)
dict={}
count=0
for reg in reg_nos:
    for key,val in absent_data.items():
        for value in val:
            if key in y:
                    if value==reg:
                        count+=1
    dict[reg]=count
    count=0
print(dict)
dict1=dict

x=timetable['CAT2']
y=[]
for i in x:
    y.append(i[0])
print (y)
dict={}
count=0
for reg in reg_nos:
    for key,val in absent_data.items():
        for value in val:
            if key in y:
                    if value==reg:
                        count+=1
    dict[reg]=count
    count=0
print(dict)
dict2=dict

#Student's report:
student = int(input("Enter register number for attedence report: "))
for key,vals in dict1.items():
    if key==student:
        print (f"Attendence report of {student} = absent for {dict1[student]}, present for {6-dict1[student]}")     
    if vals>=3:
        for key,val in dict1.items():
            if vals==val:
                print (key)

         