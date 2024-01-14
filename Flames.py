#Where only one character at a time is cancelled.
#if a character is in both names, not all occurences are cancelled
#if name1 = Harishraj
#if name2 = Selvakumar
#no of r in 'name1' is '2' and in 'name2' is '1'.
#then only one 'r' in harishraj and one 'r' in selvakumar gets cancelled
#not all 'r' are cancelled in both of them

name1 = input("Enter Name 1: ").lower()
name2 = input("Enter Name 2: ").lower()

name1_edit = []
name2_edit = []

#For finding the occurences of each letter in each word
name1_freq=[]
name2_freq=[]

name1_hist = {}
name2_hist = {}

for chr in name1:
    if chr not in name1_freq and chr != " ":
        name1_hist[chr] = 1
        name1_freq.append(chr)
    elif chr in name1_freq and chr != " ":
        name1_hist[chr] += 1
        
for chr in name2:
    if chr not in name2_freq and chr != " ":
        name2_hist[chr] = 1
        name2_freq.append(chr)
    elif chr in name2_freq and chr != " ":
        name2_hist[chr] += 1 

print ("occurences of each letter in each name:")
print (name1_hist)
print (name2_hist)

#for removing the occurences in each word              ##'\u0336' - for striking out
for i in name1_hist:
    if i in name2_hist:
        if name1_hist[i] >= name2_hist[i]:
            name1_hist[i] = name1_hist[i] - name2_hist[i]
            name2_hist[i] = name2_hist[i] - name2_hist[i]
        elif name2_hist[i] >= name1_hist[i]:
            name2_hist[i] = name2_hist[i] - name1_hist[i]
            name1_hist[i] = name1_hist[i] - name1_hist[i] 

print ("after removing the common letters with same amount of occurences: ")
print (name1_hist)
print (name2_hist)

#for making new lists of leftover letters:

for i in name1_hist:
    if name1_hist[i] != 0:
        for n in range(name1_hist[i]):
            name1_edit.append(i)

# name1_edit = [i for n in range(name1_hist[i]) for i in name1_hist if name1_hist[i] !=0]  #lst comprehension
    #only works for non-repeated letters in leftover letters
    #if there are two 'r' in leftover letters, this is not working.

for i in name2_hist:
    if name2_hist[i] != 0:
        for n in range(name2_hist[i]):
            name2_edit.append(i)

print ("Leftover letters:")
print (name1_edit)
print (name2_edit)

#calculating the number of leftover letters and counting it in FLAMES

rem = len(name2_edit) + len(name1_edit)
print ("The number of remaining letters are: ")
print (rem)

if rem>6:
    while rem>6:
        rem=rem-6
    n=rem
else:
    n=rem

if n==1:
    print ("Friends".center(50))
elif n==2:
    print ("Love".center(50))
elif n==3:
    print ("Affection".center(50))
elif n==4:
    print ("Marriage".center(50))
elif n==5:
    print ("Enemy".center(50))
elif n==6:
    print ("Siblings".center(50))