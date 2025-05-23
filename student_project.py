"""
Automation
Student Project
Project Title:
"""


import random

# Restaurant options with dine-in and takeout options
#restaurants:
cuisines = ["Italian", "Mexican", "Japanese", "American", "Vegan"]

american_in = ["Burger Barn", "BBQ Grillhouse"]
american_out = ["Steakhouse Deluxe", "Fast Burger Shack"]

vegan_in = ["Vegan Delight", "Earth Cafe"]
vegan_out = ["Green Planet", "Vegan on the Go"]

japanese_in = ["Sushi World", "Tokyo Bites"]
japanese_out = ["Ramen House", "Bento Express"]

mexican_in = ["Taco Town", "La Fiesta"]
mexican_out = ["Burrito Brothers", "Taco Stand"]

italian_in = ["Pasta Palace", "Olive Grove"]
italian_out = ["Pizza Planet", "Lasagna Corner"]




### Get user preferences for type of food and dining option ###


#type of food#
print ("Available cuisines: Italian, Mexican, Japanese, American, Vegan")
food_choice = input ("What type of food are you in the mood for? ")

#check food-if not in cuisines#
while food_choice not in cuisines:
    print("Sorry, we don't have any %s options." %food_choice)
    food_choice = input("What type of food are you in the mood for? ")

#if in cuisines, continue for dining option#
if food_choice in cuisines:
    dining_choice = input("Do you prefer dine-in or take out? ")
#check dining option- if not dine-in or take out#
    while dining_choice != "dine-in" and dining_choice != "take out":
        dining_choice = input("Please choose either 'dine-in' or 'take out': ")
        
        
        
        
#American#
    if dining_choice == "take out" and food_choice == "American":
        restaurant = random.choice(american_out)
        
    elif dining_choice == "dine-in" and food_choice == "American":
        restaurant = random.choice(american_in)

#Vegan#
    elif dining_choice == "take out" and food_choice == "Vegan":
        restaurant = random.choice(vegan_out)
        
    elif dining_choice == "dine-in" and food_choice == "Vegan":
        restaurant = random.choice(vegan_in)

#Japanese#
    elif dining_choice == "take out" and food_choice == "Japanese":
        restaurant = random.choice(japanese_out)
        
    elif dining_choice == "dine-in" and food_choice == "Japanese":
        restaurant = random.choice(japanese_in)
        
#Mexican#
    elif dining_choice == "take out" and food_choice == "Mexican":
        restaurant = random.choice(mexican_out)
        
    elif dining_choice == "dine-in" and food_choice == "Mexican":
        restaurant = random.choice(mexican_in)

#Italian#
    elif dining_choice == "take out" and food_choice == "Mexican":
        restaurant = random.choice(italian_out)
        
    elif dining_choice == "dine-in" and food_choice == "Italian":
        restaurant = random.choice(italian_in)
        
        #Final message#
print("We recommend you try %s for %s cuisine and %s." % (restaurant, food_choice, dining_choice))

    
    