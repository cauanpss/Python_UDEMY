
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for  score in student_scores:

#     print(score)
#     print(f'Your grade is {student_scores[score]}')
#     student_grades = int(student_scores[score])

#     if  student_grades <= 70:
#         print('fail.\n')
#     if  71 < student_grades < 80:
#         print('Accetable.\n') 
#     if  81 < student_grades < 90:
#         print('Exceed expetations!\n')
#     if  90 < student_grades <= 100:
#         print('Outstanding!\n')

# capitals = {
#     'france':'Paris',
#     'Germany':'Berlin'
# }

# travel_log = {
#     'france' : ['paris', 'lille', 'Dijon'],
#     'germany' : ['stuttgard', 'Berlin']
#     }
# print(travel_log['france'][1])

# nested_list = ['a', 'b', 'c', [1, 2, 3]]
# # print(nested_list[3][1])
travel_log = {
    'france': { 'cities_visited' :['Paris', 'lille', 'dijon'],
    'total_visits' : 12 
},
'germany' : {
    'cities_visited' : ['Berlin', 'Hamburg', 'Stuttgard'],
    'total_visits': 5
}
}
print(travel_log['germany']['cities_visited'][1])
