timetable={}
sub=[]
date=[]
n=int(input("\nEnter number of exams in CAT1:"))
for j in range(1,n+1):
    sub_temp=input("\nEnter the subject name: ").capitalize()
    sub.append(sub_temp)
   
    print("\nGive input as date, then month, then year. The terminal will prompt and ask you seperately.")
    
    day=int(input("Date: "))
    month=int(input("Month as number : "))
    year=int(input("Year : "))

    date_final=str(day)+"-"+str(month)+"-"+str(year)
    date.append(date_final)

timetable['CAT1']=list(zip(sub,date))

sub=[]
date=[]
n=int(input("\nEnter number of exams in CAT2:"))
for j in range(1,n+1):
    sub_temp=input("\nEnter the subject name: ").capitalize()
    sub.append(sub_temp)

    print("\nGive input as date, then month, then year. The terminal will prompt and ask you seperately.")
    
    day=int(input("Date: "))
    month=int(input("Month as number : "))
    year=int(input("Year : "))

    date_final=str(day)+"-"+str(month)+"-"+str(year)
    date.append(date_final)

timetable['CAT2']=list(zip(sub,date))

sub=[]
date=[]
n=int(input("\nEnter number of exams in End semester:"))
for j in range(1,n+1):
    sub_temp=input("\nEnter the subject name: ").capitalize()
    sub.append(sub_temp)
    print("\nGive input as date, then month, then year. The terminal will prompt and ask you seperately.")
    day=int(input("Date: "))
    month=int(input("Month as number : "))
    year=int(input("Year : "))
    date_final=str(day)+"-"+str(month)+"-"+str(year)
    date.append(date_final)
timetable['End_sem']=list(zip(sub,date))

print (timetable) 

print("Display the timetable\n")
timetable = {'CAT1': [('English', '2-3-2023'), ('Maths', '3-3-2023')], 'CAT2': []}
for i,j in timetable.items():
    print (f"           {i}".upper())
    print("DATE","               ","SUBJECT")
    print()
    for i in j:
        print(i[1],"          ",i[0])
    print()


    



