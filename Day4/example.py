import random

ramdom_integer = random.randint(1, 10)
print(ramdom_integer)

ramdom_float = random.random()
print(ramdom_float)

ramdomFloat = random.random() * 5
print(ramdomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0])

# states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(len(states_of_america))

print(states_of_america)

# index de 0 a 49(50 itens)

num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

print(states_of_america[49])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

#print(dirty_dozen)

print(dirty_dozen[0])

print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])


