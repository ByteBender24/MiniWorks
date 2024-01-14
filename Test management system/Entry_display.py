all_data={}
choice1=1
while choice1==1:
    marks=[]
    cat1=[]
    cat2=[]
    sem=[]
    print ("Enter student credentials:\n")

    reg_no = int(input("Enter Register number of student: "))
    name = input("Enter Name of student: ")
    section = input("Enter Section of student: ")
    mail=input("Enter Email ID of student: ")
    ph_no=input("Enter Contact Number of student: ")

    print("\nEnter marks of student: ")

    print("Enter CAT1 marks:")
    eng = cat1.append(int(input("Enter English marks: ")))
    maths = cat1.append(int(input("Enter Maths marks: ")))
    eg = cat1.append(int(input("Enter EG marks: ")))
    phy = cat1.append(int(input("Enter Physics marks: ")))
    chem = cat1.append(int(input("Enter Chemistry marks: ")))
    pyth = cat1.append(int(input("Enter Python marks: ")))

    print("\nEnter CAT2 marks:")
    eng = cat2.append(int(input("Enter English marks: ")))
    maths = cat2.append(int(input("Enter Maths marks: ")))
    eg = cat2.append(int(input("Enter EG marks: ")))
    phy = cat2.append(int(input("Enter Physics marks: ")))
    chem = cat2.append(int(input("Enter Chemistry marks: ")))
    pyth = cat2.append(int(input("Enter Python marks: ")))

    print("\nEnter End Semester marks:")
    eng = sem.append(int(input("Enter English marks: ")))
    maths = sem.append(int(input("Enter Maths marks: ")))
    eg = sem.append(int(input("Enter EG marks: ")))
    phy = sem.append(int(input("Enter Physics marks: ")))
    chem = sem.append(int(input("Enter Chemistry marks: ")))
    pyth = sem.append(int(input("Enter Python marks: ")))

    marks.append(cat1)
    marks.append(cat2)
    marks.append(sem)

    all_data[reg_no] = {"Name":name,"Section":section,"Email":mail,"Ph_no":ph_no,"Marks":marks}  #enter year
    
    choice1=int(input("\nPress 1 to Continue\nPress 2 to Exit\nEnter your choice: "))
    if choice1==2:
        break

print()
print(all_data)

# all_data={2210713: {'Name': 'Harishraj', 'Section': '12', 'Email': 'gmail', 'Ph_no': '99441', 'Marks': [[43, 44, 45, 46, 47, 48], [12, 13, 14, 15, 16, 17], [50, 49, 48, 
# 47, 46, 45]]}, 2210699: {'Name': 'Prani', 'Section': '1', 'Email': '2', 'Ph_no': '3', 'Marks': [[4, 12, 3, 2, 2, 3], [2, 2, 2, 2, 3, 4], [2, 2, 2, 3, 2, 1]]}}

def Display_option():
    print ("\n           DISPLAY OPTIONS ENABLED\n")
    choice_search=1
    while choice_search==1:
        reg_search=int(input("\nEnter Register number of student: "))
        print()
        print(f"Name : {all_data[reg_search]['Name']}")
        print(f"Section : {all_data[reg_search]['Section']}")
        print(f"Email ID : {all_data[reg_search]['Email']}")
        print(f"Contact Number : {all_data[reg_search]['Ph_no']}")

        print(f"\nMarks of {all_data[reg_search]['Name']}:")
        for mark1 in all_data[reg_search]['Marks']:
            if mark1==all_data[reg_search]['Marks'][0]:
                print ("\nCAT1 MARKS: \n")
                print (f"English = {mark1[0]}")
                print (f"Maths = {mark1[1]}")
                print (f"EG = {mark1[2]}")
                print (f"Physics = {mark1[3]}")
                print (f"Chemistry = {mark1[4]}")
                print (f"Python = {mark1[5]}")
            elif mark1==all_data[reg_search]['Marks'][1]:
                print ("\nCAT2 MARKS: \n")
                print (f"English = {mark1[0]}")
                print (f"Maths = {mark1[1]}")
                print (f"EG = {mark1[2]}")
                print (f"Physics = {mark1[3]}")
                print (f"Chemistry = {mark1[4]}")
                print (f"Python = {mark1[5]}")
            elif mark1==all_data[reg_search]['Marks'][2]:
                print ("\nEND SEMESTER MARKS: \n")
                print (f"English = {mark1[0]}")
                print (f"Maths = {mark1[1]}")
                print (f"EG = {mark1[2]}")
                print (f"Physics = {mark1[3]}")
                print (f"Chemistry = {mark1[4]}")
                print (f"Python = {mark1[5]}")   

        choice_search=int(input("\nPress 1 to Continue\nPress 2 to Exit\nEnter your choice: "))
        if choice_search==2:
            break

Display_option()