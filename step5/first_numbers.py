for value in range(1, 7):
    print(value)
squares = [value for value in range(1, 111)]
squares2 = [value for value in range(3, 31, 3)]
squares3 = [value**3 for value in range(1, 11)]
print(squares, min(squares), max(squares))
print(squares2)
print(squares3)
favorit_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f"The irst three items in the list are:{favorit_food[:3]}\n"
      f"The irst three items in the list are:{favorit_food[3:]}\n"
      f"The irst three items in the list are:{favorit_food[1:4]}\n")

friend_pizzas = favorit_food[:]
friend_pizzas.append("1")
favorit_food.append("2")
print(f"{friend_pizzas},{favorit_food}")

