# import Entry_display 

# all_data={2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'harishraj@gmail.com', 'Ph_no': '9944002200', 'Marks': [[45, 35, 33, 49, 41, 26], [48, 49,47,42,14,12], [11,12,1,3,4,5]]}, 2210696: {'Name': 'Prani', 'Section': '1', 'Email': 'praniakram@gmail.com', 'Ph_no': '9669669669', 'Marks': [[50, 49, 48, 49, 
# 50, 50], [50, 49, 49, 49, 49, 49], [49, 49, 49, 48, 46, 48]]}}

all_data = {2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'gmail.com', 'Ph_no': '99441', 'Marks': [[12, 12, 23, 32, 23, 34], [32, 23, 23, 22, 22, 22], [33, 33, 33, 33, 33, 33]]}, 2210699: {'Name': 'Sahana', 'Section': '12', 'Email': 'sahana@gmail.com', 'Ph_no': '9203923233', 'Marks': [[34, 34, 343, 34, 34, 34], [45, 45, 45, 45, 34, 34], [45, 45, 45, 50, 50, 40]]}}
sub=('English','Maths','EG','Physics','Chemistry','Python')

print ("EDIT OPTION ENABLED")

choice_cont=1
while choice_cont!=2:
    reg_edit =  int(input("Enter the Register number to be edited: "))
    choice_edit=0
    while choice_edit!=9:
        print(f'''
        Press 1 for editing Register number
        Press 2 for editing Name
        Press 3 for editing Section
        Press 4 for editing Email
        Press 5 for editing Contact number
        Press 6 for editing Marks of the student
        Press 9 to Exit this {reg_edit} updation menu
        ''')
        choice_edit = int(input("Enter your choice: "))

        if choice_edit==1:
            reg_edited=int(input("Enter the new updated Register number: "))
            all_data[reg_edited]=all_data.pop(reg_edit)
            reg_edit=reg_edited

        if choice_edit==2:  
            all_data[reg_edit]['Name']=input("Enter the updated Name: ")

        if choice_edit==3:
            all_data[reg_edit]['Section']=int(input("Enter the updated Section: "))

        if choice_edit==4:
            all_data[reg_edit]['Email']=input("Enter the updated Email Address: ")

        if choice_edit==5:
            all_data[reg_edit]['Ph_no']=int(input("Enter the updated Contact number: "))

        if choice_edit==6:
            for mark3 in all_data[reg_edit]['Marks']:
                if mark3==all_data[reg_edit]['Marks'][0]:
                    print('''\nPress Nothing and Enter until you reach the desired subject to change:\nPress 2 to exit CAT1 Mark updation Menu''')
                    for i in range (len(mark3)):
                        mark3[i] = int(input(f"Update {sub[i]} CAT1 marks: "))
                        if mark3[i]=='':
                            pass
                        elif mark3[i]==2:
                            break
                elif mark3==all_data[reg_edit]['Marks'][1]:
                    print('''\nPress 9 and Enter until you reach the desired subject to change:\nPress 2 to exit CAT2 Mark updation Menu''')
                    for i in range (len(mark3)):
                        mark3[i] = int(input(f"Update {sub[i]} CAT2 marks: "))
                        if mark3[i]==9:
                            pass
                        elif mark3[i]==2:
                            break
                elif mark3==all_data[reg_edit]['Marks'][2]:
                    print('''\nPress 9 and Enter until you reach the desired subject to change:\nPress 2 to exit END SEM Mark updation Menu''')
                    for i in range (len(mark3)):
                        mark3[i] = int(input(f"Update {sub[i]} End Semester marks: "))
                        if mark3[i]==9:
                            pass 
                        elif mark3[i]==2:
                            break
        if choice_edit==9:
            break
    print ("\nPress 1 for continue\nPress 2 to exit")
    choice_cont=int(input("Enter choice: "))
    if choice_cont==2:
        break

print(all_data)
                