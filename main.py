import random

fortune_cookie_num = random.randint(1, 8)
fortune_lucky_num = random.randint(1,777)

if fortune_cookie_num == 1:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("Today is going to be a great day for you.")

elif fortune_cookie_num == 2:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("You should look for a different job.")

elif fortune_cookie_num == 3:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("Always tip your waiter/waitress.")

elif fortune_cookie_num == 4:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("You should take a trip.")

elif fortune_cookie_num == 5:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("Things don't always work out.")

elif fortune_cookie_num == 6:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("If you're reading this it's too late.")

elif fortune_cookie_num == 7:
    print(f"Your lucky number is: {fortune_lucky_num}")
    print("Lucky number 7, a large amount of money is in your future.")

else:
    print("You get nothing!")
    exit()

# simple code

# import random
#
# fortune_cookie = random.randint(1,777)
#
# print(f'Don\'t forget to tip the waiter/waitress! \nYour Lucky Number is: {fortune_cookie}')