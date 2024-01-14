timetable={'CAT1': [['22-02-2022', 'Maths', 'MA'], ['23-02-2022', 'English', 'EN'], ['24-02-2022', 'Python', 'PY'], ['25-02-2022', 'Physics', 'PHY'], ['26-02-2022', 'Chemistry', 'CHEM'], ['27-02-2022', 'Graphics', 'EG']], 'CAT2': [['03-03-2022', 'Maths', 'MA'], ['04-03-2022', 'English', 'EN'], ['05-03-2022', 'Python', 'PY'], ['06-03-2022', 'Graphics', 'EG'], ['07-03-2022', 'Physics', 'PHY'], ['08-03-2022', 'Chemistry', 'CHEM']], 'END SEM': [['23-03-2022', 'English', 'EN'], ['24-03-2022', 'Maths', 'MA'], ['25-03-2022', 'Python', 'PY'], ['26-03-2022', 'Physics', 'PHY'], ['27-03-2022', 'Chemistry', 'CHEM'], ['28-03-2022', 'Graphics', 'EG']]}
# all_data={2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'gmail', 'Ph_no': '99441', 'Marks': [[43, 44, 45, 46, 47, 48], [12, 13, 14, 15, 16, 17], [50, 49, 48, 
# 47, 46, 45]]}, 2210699: {'Name': 'Prani', 'Section': '1', 'Email': '2', 'Ph_no': '3', 'Marks': [[4, 12, 3, 2, 2, 3], [2, 2, 2, 2, 3, 4], [2, 2, 2, 3, 2, 1]]}}
print (timetable)
all_data={2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'gmail.com', 'Ph_no': '99441', 'Marks': [[12, 12, 23, 32, 23, 34], [32, 23, 23, 22, 22, 22], [33, 33, 33, 33, 33, 33]]}, 2210699: {'Name': 'Sahana', 'Section': '12', 'Email': 'sahana@gmail.com', 'Ph_no': '9203923233', 'Marks': [[34, 34, 343, 34, 34, 34], [45, 45, 45, 45, 34, 34], [45, 45, 45, 50, 50, 40]]}}

absent_data={}
absentee_list=[]
for i in timetable.keys():
    print("\n"+i.rjust(29)+"\n")
    for j in timetable[i]:
        print()
        print(j[0],j[1],j[2],sep="\t\t")
        while True:
            absentee=int(input("\nEnter the register number of the absentee: "))

            if absentee in all_data.keys() and absentee not in absentee_list:
                absentee_list.append(absentee)
            else:
                print("You have entered a wrong register number!")
            
            choice_absentee=input("\nPress 1 to continue\t\tPress 2 to move to next subject\nEnter your choice: ")
            if choice_absentee=="2":
                absent_data[j[0]]=absentee_list
                absentee_list=[]
                break

print(absent_data) 
# {'22-02-2022': [2210713, 2210699], '23-02-2022': [2210713], '24-02-2022': [2210699], '25-02-2022': [2210699], '26-02-2022': [], '27-02-2022': [], '03-03-2022': [2210699], '04-03-2022': [], '05-03-2022': [2210699, 2210713], '06-03-2022': [], '07-03-2022': [], '08-03-2022': [], '23-03-2022': [], '24-03-2022': [2210713], '25-03-2022': [], '26-03-2022': [], '27-03-2022': [], '28-03-2022': [2210699]}
# #for number of absentees:
# # d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
# # d_lists = {}
# # for key, value in d.items():
# #     if value not in d_lists:
# #         d_lists[value] = [key]
# #     else:
# #         d_lists[value].append(key)
# # count = 0
# # for value_list in d_lists.values():
# #     if len(value_list) > 1:
#         # count += 1

