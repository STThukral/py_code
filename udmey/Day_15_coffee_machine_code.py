#3 hot flavours
#coins operate
# step 1
# expresso £1.50, latte £2.50 and cappuccion £3.00
# 50 ml water, 18g coffee
# 200ml water , 24g coffee and 150 ml milk
#250ml water ,24g coffee and 100ml milk resp.
# resources in coffee
# 300 ml water , 200ml milk and 100g coffee
# Second feature coins
# 1 pence , 5 pence ,10 pences and 25 pence
#prgram requiremrnt
# how much resources left after coffee making by asking for "report"
# What would you like (expresso/lattee / cappuccine) ?
#please insert coins.
#how many 25 pences? :
#how many 10 pences? :
#how many 5 pences? :
#how many 0 pences? :
# What would you like (expresso/lattee / cappuccine): report
#Water : 100 ml
#milk:50ml
#coffee:76gm
#check the resource efficiency is someone order latte but resources not enough
#give message sorry not enough water / milk or coffee as every time we make coffee
#deduct rsources
#is someone order latte and money not enough , give message
#Sorry that's not enough money . Money refunded
#show the total coisns paid in poubd or pence

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#print (MENU)
#print (resources)
''' function drink_cost is defined to check how much drink will cost
    by getting user_choice and checking cost through dictionary'''
def drink_cost(user_choice):
    espresso_cost =0
    lattee_cost =0
    cappuccino_cost =0
    #print(MENU["cappuccino"]["ingredients"])
    # Get the cost of each item in menu
    espresso_cost= (MENU["espresso"].get("cost"))
    latte_cost= (MENU["latte"].get("cost"))
    cappuccino_cost= (MENU["cappuccino"].get("cost"))

    # check the user choice and get the cost of item
    coffee_cost =0
    if user_choice ==  "espresso":
        coffee_cost = espresso_cost        
    elif user_choice ==  "latte":
        coffee_cost = latte_cost
    elif user_choice ==  "cappuccino":
        coffee_cost = cappuccino_cost

    return coffee_cost

'''are_resources_sufficient function is to check the resources every time user
   orders item and if resources are not sufficient then show message'''
def are_resources_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

# variable for while loop
# if user_choice if "off" loop will end
keep_on_going = True
while keep_on_going:
    user_choice=input("What would you like (espresso/ latte /cappuccino) ? :")
    ''' when user types "report" then code will give resources left in
        coffee machine'''
    if user_choice == "report":
        for key in resources:
            print(f' {key} : {resources[key]}')
    ## off then end loop
    elif user_choice == "off":
        keep_on_going = False
    else:
        #print(f' resources : {resources}')
        drink= (MENU[user_choice])
        ordered_ingredients = (drink["ingredients"])
        # check the drink optation and check resources
        # if all ok then procceed
        # as for coins
        if are_resources_sufficient(ordered_ingredients):
            print("Please insert coins.")
            quarter_pence=int(input("how many 25 pences? : "))
            ten_pence=int(input("how many 10 pences? : "))
            five_pence=int(input("how many 5 pences? : "))
            one_pence=int(input("how many 1 pences? : "))

            # calculate the total coins entered and check
            # money is suffcient to create coffee
            total_price = float((quarter_pence*25)+(ten_pence*10)+(five_pence*5)+(one_pence*1))/100
            print(f'Here is £{total_price} in change.')
 
            if total_price < drink_cost(user_choice):
                print ("Sorry NOT enough Money. Money refunded.")
            else:
                print(f'Here is your {user_choice} Enjoy !')
                extra_money=0
                extra_money= total_price - drink_cost(user_choice)
                if extra_money > 0:
                    print(f'Please collect your extra coins {extra_money}')
                # when coffee is served then deduct the resources from
                # previous resources and give the left over resources
                for item in ordered_ingredients:
                 resources[item] -= ordered_ingredients[item]
    
            #print(f' resources : {resources}')    
            #print(f' ordered_ingredients : {ordered_ingredients}')

            
