####################
# Python Exercises #
####################

#################################################
# Task 1: Examine the types of data structures. #
#################################################

x = 8
type(x)  # int

y = 3.2
type(y)  # float

z = 8j + 18
type(z)  # complex

a = 'Hello World'
type(a)  # str

b = True
type(b)  # bool

c = 23 < 22
type(c)  # bool

l = [1, 2, 3, 4, 'String', 3.2, False]
type(l)  # list

d = {'Name': 'Jake',
     'Age': [27, 56],
     'Adress': 'Downtown'}
type(d)  # dict

t = ('Machine Learning', 'Data Science')
type(t)  # tuple

s = {'Python', 'Machine Learning', 'Data Science', 'Python'}
type(s)  # set

############################################################################################################################################
# Task 2: Convert all letters of the given string expression to uppercase. Put space instead of comma and dot, separate them word by word. #
#                                                                                                                                          #
# Expected Output:                                                                                                                         #
# ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']                              #
############################################################################################################################################

text = 'The goal is to turn data into information, and information into insight.'

text.upper().replace(',', '').replace('.', '').split()
# ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

#############################################################
# Task 3: Do the following tasks for the given list.        #
#############################################################

lst = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

# Step 1: Look at the number of elements of the given list.
len(lst)  # 11

# Step 2: Call the elements at index zero and ten.
lst[0]  # 'D'
lst[10]  # 'E'

# Step 3: Create a list ['D', 'A', 'T', 'A'] from the given list.
lst[0:4]  # ['D', 'A', 'T', 'A']

# Step 4: Delete the element in the eighth index.
lst.pop(8)  # 'N'
lst  # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

# Step 5: Add a new element.
lst.append('python')
lst  # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 'python']

# Step 6: Re-add element 'N' to the eighth index.
lst.insert(8, 'N')
lst  # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 'python']

#########################################################################
# Task 4: Apply the following steps to the given dictionary structure.  #
#########################################################################

dict = {'Christian': ['America', 18],
        'Daisy': ['England', 12],
        'Antonio': ['Spain', 22],
        'Dante': ['Italy', 25]}

# Step 1: Access the key values.
dict.keys()  # dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])

# Step 2: Access the values.
dict.values() # dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])

# Step 3: Update the value 12 of the Daisy key to 13.
dict.update({'Daisy': ['England', 13]})
dict # {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Antonio': ['Spain', 22], 'Dante': ['Italy', 25]}

# or
# dict['Daisy'][1] = 13

# Step 4: Add a new value whose key is Ahmet and value is [Turkey, 24].
dict.update({'Ahmet': ['Turkey', 24]})
dict  # {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Antonio': ['Spain', 22], 'Dante': ['Italy', 25], 'Ahmet': ['Turkey', 24]}

# or
# dict['Ahmet'] = ['Turkey', 24]

# Step 5: Delete Antonio from dictionary.
dict.pop('Antonio')
dict # {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Dante': ['Italy', 25], 'Ahmet': ['Turkey', 24]}

###########################################################################################################################################################
# Task 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists.     #
###########################################################################################################################################################

l = [2, 13, 18, 93, 22]


def numbers(num_list):
    even = []
    odd = []
    for n in num_list:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd


even_list, odd_list = numbers(l)
even_list  # [2, 18, 22]
odd_list  # [13, 93]

##############################################################################################################################
# Task 6: In the list given below, there are the names of the students who won degrees in engineering and medical faculties. #
# Respectively, the first three students represent the success rank of the engineering faculty,                              #
# while the last three students belong to the rank of the medical faculty.                                                   #
# Print student grades specific to faculty using enumarate.                                                                  #
##############################################################################################################################

ogrenciler = ['Ali', 'Veli', 'Ayşe', 'Talat', 'Zeynep', 'Ece']

# Notes:
# 'ogrenciler' refers to 'students'
# 'Mühendislik Fakültesi' refers to 'Engineering Faculty'
# 'Tıp Fakültesi' refers to 'Medical Faculty'

# I.
for index, students in enumerate(ogrenciler):
    if index < 3:
        index += 1
        print(f'Mühendislik Fakültesi: {index}. öğrenci: {students}')
    else:
        index -= 2
        print(f'Tıp Fakültesi: {index}. öğrenci: {students}')

# II.
for index, students in enumerate(ogrenciler, 1):
    if index <= 3:
        print(f'Mühendislik Fakültesi: {index}. öğrenci: {students}')
    else:
        index -= 3
        print(f'Tıp Fakültesi: {index}. öğrenci: {students}')

#######################################################################################################################
# Task 7: 3 lists are given below. In the lists, there is a lecture code, credit and quota information, respectively. #
# Print course information using zip().                                                                               #
#######################################################################################################################

ders_kodu = ['CMP1005', 'PSY1001', 'HUK1005', 'SEN2204']
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

# Notes:
# 'ders_kodu' refers to 'lecture code'
# 'kredi' refers to 'credit'
# 'kontenjan' refers to 'quota'

# I.
for a, b, c in zip(ders_kodu, kredi, kontenjan):
    print(f'Kredisi {b} olan {a} kodlu dersin kontenjanı {c} kişidir.')

# II.
print(list(zip(ders_kodu, kredi, kontenjan)))  # as a list

#####################################################################################
# Task 8: Below are 2 sets.                                                         #
# If the 1st set includes the 2nd set, print the common elements.                   #
# If not then print the elements of the 2nd set that doesn't occure in the 1st set. #
#####################################################################################

kume1 = set(['data', 'python'])
kume2 = set(['data', 'function', 'qcut', 'lambda', 'python', 'miuul'])

# Note:
# 'kume' refers to 'set'

def sets(set1, set2):
    if set1.issuperset(set2):
        print('İki kümenin ortak elemanları', set1.intersection(set2))
    else:
        print('2.nci kümenin 1.nci kümeden farkı:', set2.difference(set1))


sets(kume1, kume2)