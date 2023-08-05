# # Create list
# my_list = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'Kotlin', 'RUST' ]


###############
# # INDEXING
###############
# # Access list element
# first_language = my_list[0]
# print(first_language) 

# # Output: 
# # 'Python'

###############
# # REVERSE INDEXING
###############

# last_language = my_list[-1]
# print(last_language) 

# # Output: 
# # 'RUST'

# #####################################
# #############
# # Slice list
# #############
# first_two_languages = my_list[:2]
# print(first_two_languages) 

# # Output: 
# # ['Python', 'Java']



#####################################
# #############
# # nested list
# #############

# # Creates a nested list with elements 
# my_list = ['Python', ['Java', 'C++'], ['JavaScript', ['Scala', 'Kotlin']]]

# # Accesses the first element of the list
# first_element = my_list[0] 

# # Accesses the first element of the second list
# second_element = my_list[1][0] 

# # Accesses the first element of the third list
# third_element = my_list[2][1][0] 

# print('first_element',first_element)
# print('second_element',second_element)
# print('third_element',third_element)

#####################################
# #############
# # Loop List
# #############


# For loop example to iterate list
languages = ['Python','Java','C++','JavaScript']
for language in languages:
    print(language)

# Ouput:
# Python
# Java

#####################################
# #############
# # Length list
# #############

# # Using len() function
# technology= ['Spark','Pandas','Pyspark','Java']
# result = len(technology)

# if len(technology) == 0:
#     print("The list is empty")
# else:
#     print("The list is not empty")
    
    
#####################################
# #############
# # SORT list
# #############

# my_list = ['Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'Kotlin', 'RUST' ]
# print(sorted(my_list))

#####################################