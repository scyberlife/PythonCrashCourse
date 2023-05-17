age = ("infant", "youngster", "child", "teenager", "adult", "elderly person")
number = int(input())

if number < 2:
    print(age[0])

elif number >= 2 and number < 4:
    print(age[1])

elif number >= 13 and number < 20:
    print(age[2])

elif number >= 20 and number < 65:
    print(age[3])

else:
    print(age[4])

favorite_fruits = ["apple", "banana", "cherry"]
if "apple" in favorite_fruits:
    print(f"You really like {favorite_fruits[0]}")
if "banana" in favorite_fruits:
    print(f"You really like {favorite_fruits[1]}")
if "cherry" in favorite_fruits:
    print(f"You really like {favorite_fruits[2]}")
