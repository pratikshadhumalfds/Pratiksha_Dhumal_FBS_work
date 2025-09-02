###Python program to concatenate two Dictionaries into one...

d1 = {'name':'Pratu', 'Rollno':14}    ##define two dictionaries
d2 = {'dept':'Computer engg', 'Year':'final'}
Merged_dict = {**d1, **d2}   ##concatenate two dictionaries
print(Merged_dict)   