# print("Hello")
# num_char = len("Hello")

# print(num_char)

def my_function():
    print("Hello")
    print("Bye")


my_function()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#with for
for step in range(6):
    jump()
#with while
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)