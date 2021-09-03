import random
import pandas

numbers = [1, 2, 3]
new_list1 = []

for n in numbers:
    add_1 = n + 1
    new_list1.append(add_1)
print(new_list1)

# list comprehensions
# new_list = [new_item for item in list if test]

new_list2 = [(n + 1) for n in numbers]
print(new_list2)

name = 'Theo'
list = [letter for letter in name]
print(list)

list2 = [n * 2 for n in range(1, 5)]
print(list2)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

with open("file1.txt") as file1:
    data1 = file1.read().split()

with open("file2.txt") as file2:
    data2 = file2.read().split()

num_list = [int(num) for num in data1 if num in data2]
print(num_list)

# dictionary comprehensions
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for key(value) in dict.items() if test}


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_count = {word: len(word) for word in sentence.split()}
print(word_count)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

# loop through dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


