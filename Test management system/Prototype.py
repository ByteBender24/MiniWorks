def get_details():
    choice1=1
    student={}
    while choice1==1:
        year=int(input("Enter the academic year: "))
        print("Add details of students: \n")
        reg_no = int(input("Enter register number of student: "))
        name = input("Enter name of student: ")
        section = input("Enter section of student: ")
        mail=input("Enter email ID of student: ")
        ph_no=input("Enter contact number of student: ")
        print("\nEnter marks of student: ")
        marks=[]
        eng = marks.append(int(input("Enter English marks: ")))
        maths = marks.append(int(input("Enter Maths marks: ")))
        eg = marks.append(int(input("Enter EG marks: ")))
        phy = marks.append(int(input("Enter Physics marks: ")))
        chem = marks.append(int(input("Enter Chemistry marks: ")))
        pyth = marks.append(int(input("Enter Python marks: ")))
        # all_data = {year:student}
        student[reg_no]={name:[section,mail,ph_no,marks]}
        all_data = {year:student}
        print("\nPress 1 to continue adding details\nPress 2 to exit")
        choice1=int(input("Enter choice: "))
    # print(student)
    print (all_data)
# all_data={2023: {68: {'Achu': ['12', 'gmail', '99', [1, 2, 3, 4, 5, 6]]}, 69: {'Prani': ['01', 'gmail', '98', [2, 3, 4, 5, 6, 7]]}},2024 : {420: {'Sweety': ['10', 'gmail', '999', [1, 2, 3, 4, 5, 6]]}, 421: {'HariharanD': ['01', 'gmail', '911', [2, 3, 4, 5, 6, 7]]}}}


# def search():
#     for year in all_data:
#         year=int(input("Enter Academic year to be searched: "))
#         print(f"\nFor the year {year}, the details of the students are:")
#         for reg_no in all_data[year]:
#             reg_search=int(input("\nEnter the register number to be searched: "))
#             if reg_no==reg_search:
#                 print(f"Register number: {reg_no}")
#                 for details in all_data[year][reg_no]:
#                     x=details
#                     print(f"Name:{details}")
#                     for name in all_data[year][reg_no][details]:
#                             print(f"Section: {all_data[year][reg_no][details][0]}")
#                             print(f"email ID : {all_data[year][reg_no][details][1]}")
#                             print(f"contact number: {all_data[year][reg_no][details][2]}")
#                             print(f"\nTotal Aggregate Marks in each subject of {x}:")
#                             for n in all_data[year][reg_no][details][3]:
#                                 if n==all_data[year][reg_no][details][3][0]:
#                                     print(f"English marks: {n}")
#                                 elif n==all_data[year][reg_no][details][3][1]:
#                                     print(f"Maths marks: {n}")
#                                 elif n==all_data[year][reg_no][details][3][2]:
#                                     print(f"EG marks: {n}")
#                                 elif n==all_data[year][reg_no][details][3][3]:
#                                     print(f"Physics marks: {n}")
#                                 elif n==all_data[year][reg_no][details][3][4]:
#                                     print(f"Chemistry marks: {n}")
#                                 elif n==all_data[year][reg_no][details][3][5]:
#                                     print(f"Python marks: {n}")
#                             print("_____________________________________________________")
#                             break
#                 print("\nFor searching via year,exit the current menu.")
#                 print("\nPress 1 to continue\nPress 2 to exit")
#                 choice_break=int(input("Enter your choice: "))
#                 if choice_break==3:
#                     print("\n               EXITED CURRENT MENU")
#                     break
#         print("\nPress 1 to search via Year\nPress 2 to exit the Search Menu")
#         choice_break=int(input("Enter your choice: "))
#         if choice_break==2:
#             print("\n---------------------------EXIT---------------------------")
#         break



# choice1=1
# student={}
# while choice1==1:
#     year=int(input("Enter the academic year: "))
#     print("Add details of students: \n")
#     reg_no = int(input("Enter register number of student: "))
#     name = input("Enter name of student: ")
#     section = input("Enter section of student: ")
#     mail=input("Enter email ID of student: ")
#     ph_no=input("Enter contact number of student: ")
#     print("\nEnter marks of student: ")
#     marks=[]
#     eng = marks.append(int(input("Enter English marks: ")))
#     maths = marks.append(int(input("Enter Maths marks: ")))
#     eg = marks.append(int(input("Enter EG marks: ")))
#     phy = marks.append(int(input("Enter Physics marks: ")))
#     chem = marks.append(int(input("Enter Chemistry marks: ")))
#     pyth = marks.append(int(input("Enter Python marks: ")))
#     all_data = {year:student}
#     student[reg_no]={name:[section,mail,ph_no,marks]}
#     print("\nPress 1 to continue adding details\nPress 2 to exit")
#     choice1=int(input())
# # print(student)
# print (all_data)
# all_data={2023: {68: {'Achu': ['12', 'gmail', '99', [1, 2, 3, 4, 5, 6]]}, 69: {'Prani': ['01', 'gmail', '98', [2, 3, 4, 5, 6, 7]]}},2024 : {420: {'Sweety': ['10', 'gmail', '999', [1, 2, 3, 4, 5, 6]]}, 421: {'HariharanD': ['01', 'gmail', '911', [2, 3, 4, 5, 6, 7]]}}}

choice1=1
student={}
while choice1==1:
    year=int(input("Enter the academic year: "))
    print("Add details of students: \n")
    reg_no = int(input("Enter register number of student: "))
    name = input("Enter name of student: ")
    section = input("Enter section of student: ")
    mail=input("Enter email ID of student: ")
    ph_no=input("Enter contact number of student: ")
    print("\nEnter marks of student: ")
    marks=[]
    eng = marks.append(int(input("Enter English marks: ")))
    maths = marks.append(int(input("Enter Maths marks: ")))
    eg = marks.append(int(input("Enter EG marks: ")))
    phy = marks.append(int(input("Enter Physics marks: ")))
    chem = marks.append(int(input("Enter Chemistry marks: ")))
    pyth = marks.append(int(input("Enter Python marks: ")))
    all_data = {year:student}
    student[reg_no]={name:[section,mail,ph_no,marks]}
    print("\nPress 1 to continue adding details\nPress 2 to exit")
    choice1=int(input())
# print(student)
print (all_data)
all_data={2023: {68: {'Achu': ['12', 'gmail', '99', [1, 2, 3, 4, 5, 6]]}, 69: {'Prani': ['01', 'gmail', '98', [2, 3, 4, 5, 6, 7]]}},2024 : {420: {'Sweety': ['10', 'gmail', '999', [1, 2, 3, 4, 5, 6]]}, 421: {'HariharanD': ['01', 'gmail', '911', [2, 3, 4, 5, 6, 7]]}}}



for year in all_data:
    year=int(input("Enter Academic year to be searched: "))
    print(f"\nFor the year {year}, the details of the students are:")
    for reg_no in all_data[year]:
        reg_search=int(input("\nEnter the register number to be searched: "))
        if reg_no==reg_search:
            print(f"Register number: {reg_no}")
            for details in all_data[year][reg_no]:
                x=details
                print(f"Name:{details}")
                for name in all_data[year][reg_no][details]:
                        print(f"Section: {all_data[year][reg_no][details][0]}")
                        print(f"email ID : {all_data[year][reg_no][details][1]}")
                        print(f"contact number: {all_data[year][reg_no][details][2]}")
                        print(f"\n Total Aggregate Marks in each subject of {x}:")
                        for n in all_data[year][reg_no][details][3]:
                            if n==all_data[year][reg_no][details][3][0]:
                                print(f"English marks: {n}")
                            elif n==all_data[year][reg_no][details][3][1]:
                                print(f"Maths marks: {n}")
                            elif n==all_data[year][reg_no][details][3][2]:
                                print(f"EG marks: {n}")
                            elif n==all_data[year][reg_no][details][3][3]:
                                print(f"Physics marks: {n}")
                            elif n==all_data[year][reg_no][details][3][4]:
                                print(f"Chemistry marks: {n}")
                            elif n==all_data[year][reg_no][details][3][5]:
                                print(f"Python marks: {n}")
                        print("_____________________________________________________")
                        break
            print("\nFor searching via year,exit the current menu.")
            print("\nPress 1 to continue\nPress 2 to exit")
            choice_break=int(input("Enter your choice: "))
            if choice_break==2:
                print("\n               EXITED CURRENT MENU")
                break
    print("\nPress 1 to search via Year\nPress 2 to exit the Search Menu")
    choice_break=int(input("Enter your choice: "))
    if choice_break==2:
        print("\n---------------------------EXIT---------------------------")
        break


# for year in all_data:
#     year=int(input("Enter Academic year to be searched: "))
#     print("For Editing & Updation:\nPress 1 to edit\nPress 2 to exit")
#     choice_edit=int(input("Enter your choice: "))
#     if choice_edit==1:
#         all_data
#     elif choice_edit==2:
#         pass
#     print(f"\nFor the year {year}, the details of the students are:")
#     for reg_no in all_data[year]:
#         reg_search=int(input("\nEnter the register number to be searched: "))
#         if reg_no==reg_search:
#             print(f"Register number: {reg_no}")
#             for details in all_data[year][reg_no]:
            #     x=details
            #     print(f"Name:{details}")
            #     for name in all_data[year][reg_no][details]:
            #             print(f"Section: {all_data[year][reg_no][details][0]}")
            #             print(f"email ID : {all_data[year][reg_no][details][1]}")
            #             print(f"contact number: {all_data[year][reg_no][details][2]}")
            #             print(f"\n Total Aggregate Marks in each subject of {x}:")
            #             for n in all_data[year][reg_no][details][3]:
            #                 if n==all_data[year][reg_no][details][3][0]:
            #                     print(f"English marks: {n}")
            #                 elif n==all_data[year][reg_no][details][3][1]:
            #                     print(f"Maths marks: {n}")
            #                 elif n==all_data[year][reg_no][details][3][2]:
            #                     print(f"EG marks: {n}")
            #                 elif n==all_data[year][reg_no][details][3][3]:
            #                     print(f"Physics marks: {n}")
            #                 elif n==all_data[year][reg_no][details][3][4]:
            #                     print(f"Chemistry marks: {n}")
            #                 elif n==all_data[year][reg_no][details][3][5]:
            #                     print(f"Python marks: {n}")
            #             print("_____________________________________________________")
            #             break
            # print("\nFor searching via year,exit the current menu.")
            # print("\nPress 1 to continue\nPress 2 to exit")
            # choice_break=int(input("Enter your choice: "))
            # if choice_break==2:
            #     print("\n               EXITED CURRENT MENU")
            #     break
#     print("\nPress 1 to search via Year\nPress 2 to exit the Search Menu")
#     choice_break=int(input("Enter your choice: "))
#     if choice_break==2:
#         print("\n---------------------------EXIT---------------------------")
#         break

# print("\nFor Editing & Updation:\nPress 1 to edit\nPress 2 to exit")
# choice_edit=int(input("Enter your choice: "))
# if choice_edit==1:
#     pass
# elif choice_edit==2:
#     pass