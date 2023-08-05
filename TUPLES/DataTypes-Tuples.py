# # Create tuple
# my_tuple = ('Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'Kotlin', 'RUST' )


###############
# # INDEXING
###############
# # Access tuple element
# first_language = my_tuple[0]
# print(first_language) 

# # Output: 
# # 'Python'

###############
# # REVERSE INDEXING
###############

# last_language = my_tuple[-1]
# print(last_language) 

# # Output: 
# # 'RUST'

# #####################################
# #############
# # Slice tuple
# #############
# first_two_languages = my_tuple[:2]
# print(first_two_languages) 

# # Output: 
# # ('Python', 'Java')



#####################################
# #############
# # nested tuple
# #############

# # Creates a nested tuple with elements 
# my_tuple = ('Python', ('Java', 'C++'), ('JavaScript', ('Scala', 'Kotlin')))

# # Accesses the first element of the tuple
# first_element = my_tuple[0] 

# # Accesses the first element of the second tuple
# second_element = my_tuple[1][0] 

# # Accesses the first element of the third tuple
# third_element = my_tuple[2][1][0] 

# print('first_element',first_element)
# print('second_element',second_element)
# print('third_element',third_element)

#####################################
# #############
# # Loop tuple
# #############


# # Example of tuple with for loop
# my_tuple = ('Python', 'Java', 'C++', 'JavaScript')
# for element in my_tuple:
#     print(element)

# # Output:
# # Python
# # Java
# # C++
# # JavaScript

#####################################
# #############
# # Length tuple
# #############

# # Using len() function
# technology= ('Spark','Pandas','Pyspark','Java')
# result = len(technology)

# if len(technology) == 0:
#     print("The tuple is empty")
# else:
#     print("The tuple is not empty")
    
    
#####################################
# #############
# # SORT tuple
# #############

# my_tuple = ('Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'Kotlin', 'RUST' )
# print(sorted(my_tuple))

#####################################