timetable={}
sub_time=[]
n=int(input("Enter number of tests in CAT1: "))
for i in range(n):
    sub_list=[]
    sub_list.append(input("Enter the Date in the format DD-MM-YYYY: "))
    sub_list.append(input("Enter the subject name: "))
    sub_list.append(input("Enter the subject code: "))
    sub_time.append(sub_list)
timetable['CAT1']=sub_time

sub_time=[]
n=int(input("Enter number of tests in CAT2: "))
for i in range(n):
    sub_list=[]
    sub_list.append(input("Enter the Date in the format DD-MM-YYYY: "))
    sub_list.append(input("Enter the subject name: "))
    sub_list.append(input("Enter the subject code: "))
    sub_time.append(sub_list)
timetable['CAT2']=sub_time

sub_time=[]
n=int(input("Enter number of tests in END SEMESTER: "))
for i in range(n):
    sub_list=[]
    sub_list.append(input("Enter the Date in the format DD-MM-YYYY: "))
    sub_list.append(input("Enter the subject name: "))
    sub_list.append(input("Enter the subject code: "))
    sub_time.append(sub_list)
timetable['END SEM']=sub_time

print (timetable)
print("DISPLAY OPTIONS:")
for i,j in timetable.items():
    print ("           ",i)
    print ("   DATE              SUBJECT          CODE")
    for k in range(len(j)):
        for l in range(3):
            print (j[k][l],end="           ")
        print()

print(timetable)
print("EDITING OPTIONS") 

while True:
    print('''Press 1 to edit the examination name.\nPress 2 to edit the subject and dates\nPress 3 to exit this menu''')
    choice_edit=int(input("Enter your choice: "))
    if choice_edit==1:
        key1=input("Enter the examination name(CAT1,CAT2,END SEM) to be changed: ")
        key2=input("Enter the updated examination name: ")
        timetable[key2]=timetable.pop(key1)  
        print(timetable)
    if choice_edit==2:
        key1=input("Enter the examination name to edit:\nCAT1,CAT2,END SEM\nEnter your choice: ")
        for j in timetable[key1]:
            print(j)
        choice_edit_sub=int(input("Enter your choice, choose 1 to 6 to edit the shown subjects or date."))
        n=choice_edit_sub
        while True:
            choice_edit_date=int(input("Enter 1 to change subject name\t\tEnter 2 to change subject code\t\tEnter 3 to change date\t\tEnter 4 toexit this current menu\nEnter your choice: "))
            if choice_edit_date==1:
                timetable[key1][n-1][0]=input("Enter the updated test date: ")
            elif choice_edit_date==2:
                timetable[key1][n-1][1]=input("Enter the updated test name: ")
            elif choice_edit_date==3:
                timetable[key1][n-1][2]=input("Enter the updated test code: ")
            elif choice_edit_date==4:
                break
    if choice_edit==3:
        break
print(timetable)