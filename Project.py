import random
Pizza_Hut_menu = [
    {"name": "Chicken Supreme", "price": 150},
    {"name": "Super Supreme", "price": 170},
    {"name": "BBQ Chicken Ranch", "price": 180}
]

bazooka_menu = [
    {"name": "Combo Single", "price": 145},
    {"name": "BBQ Bazooka Burger", "price": 160},
    {"name": "Happiness Rocket", "price": 240}
]

buffalo_burger_menu = [
    {"name": "Old School Burger", "price": 150},
    {"name": "Blue Cheese Burger", "price": 155},
    {"name": "Double Jab Burger", "price": 210}
]

menus = {
    "Pizza Hut": Pizza_Hut_menu,
    "Bazooka": bazooka_menu,
    "Buffalo Burger": buffalo_burger_menu
}

cart = []


def registration():
    while True:
        print("""Welcome To Our Talabat App \nRegistration""")
        registration_choice = input("Please Choose Sign Up Or Login: ").lower()

        if registration_choice == "sign up":
            user_info = sign_up()
            break
        elif registration_choice == "login":
            user_info = login()
            break
        else:
            print("Please choose Sign Up or Login.")
    return user_info


def sign_up():
    name = input("Please Enter Your Full Name: ")
    phone = int(input("Please Enter Your Phone Number: "))
    address = input("Please Enter Your Address: ")
    user_name = input("Please Create A User Name: ")

    user_info = {
        "name": name,
        "phone": phone,
        "address": address,
        "user_name": user_name
    }

    while True:
        password = input("Please Create A Strong Password: ")
        confirm_password = input("Please Confirm Your Password: ")
        if password == confirm_password:
            print("Sign Up successfully")
            break
        else:
            print("Passwords don't match. Please try again.")
    return user_info


def login():
    username = input("Please Enter Your User Name: ")
    password = input("Please Enter Your Password: ")
    print("Login successfully")

    user_info = {
        "name": username,
        "phone": int(input("Please Enter Your Phone Number: ")),
        "address": input("Please Enter Your Address: "),
        "user_name": username
    }
    return user_info


def display_categories():
    print("Main Categories:")
    categories = ["1. Food", "2. Groceries", "3. Electronics", "4. Health and Beauty"]
    for category in categories:
        print(category)


def process_choice(choice):
    if choice == 1:
        print("You choose Food")
        display_restaurant_menu()
        return True
    elif choice == 2:
        print("You choose Groceries Stay tuned coming soon")
        return True
    elif choice == 3:
        print("You choose Electronics Stay tuned coming soon")
        return True
    elif choice == 4:
        print("You choose Health and Beauty Stay tuned coming soon")
        return True
    else:
        print("Invalid Choice. Please choose a valid category number from 1 to 4. ")
        return False


def display_restaurant_menu():
    print("Select a Restaurant:")
    restaurants = ["1. Pizza Hut", "2. Bazooka", "3. Buffalo Burger"]
    for restaurant in restaurants:
        print(restaurant)

    while True:
        restaurant_choice = int(input("Please select a restaurant number: "))
        if 1 <= restaurant_choice <= 3:
            break
        else:
            print("Invalid restaurant choice. Please choose 1 or 2 or 3")
            continue


    if restaurant_choice == 1:
         restaurant = "Pizza Hut"
    elif restaurant_choice == 2:
         restaurant = "Bazooka"
    elif restaurant_choice == 3:
         restaurant = "Buffalo Burger"
    else:
         print("Invalid restaurant choice. Returning to main categories.")
         return
    print(f"Menu for {restaurant}:")

    item_number = 1
    for item in menus[restaurant]:
        item_name = item["name"]
        item_price = item["price"]
        print(f"{item_number}. {item_name} : {item_price} EGP")
        item_number += 1

    add_to_cart(restaurant)

def add_to_cart(restaurant):
    while True:
        item_choice = input(f"Please enter the item number from{restaurant}'s menu to add to your cart, or 'done' to finish: ").lower()

        if item_choice == 'done':
            break

        item_choice = int(item_choice)

        if 1 <= item_choice <= len(menus[restaurant]):
            item = menus[restaurant][item_choice - 1]
            item_name = item["name"]
            item_price = item["price"]
            quantity = int(input(f"How many of the {item_name} would you like to add to your cart? "))
            cart.append({"name": item_name, "price": item_price,
                         "quantity": quantity})
            print(f"You have added {quantity} x {item_name} to your cart.")
        else:
            print("Incorrect number. Please choose again.")


def update_cart():
    view_cart()
    if cart:
        item_to_update = input("Enter the name of the item you want to update, or 'done' to finish: ").lower()

        if item_to_update == 'done':
            return

        for item in cart:
            if item_to_update.lower() in item["name"].lower():
                new_quantity = input(f"Enter the new quantity for {item['name']}: ")
                item["quantity"] = int(new_quantity)
                print(f"You've updated the quantity for {item['name']} to {item['quantity']}. ")

                return
        print("Item not found in your cart.")


def remove_from_cart():
    view_cart()
    if cart:
        item_to_remove = input("Enter the name of the item you want to remove, or 'done' to finish: ").lower()

        if item_to_remove == 'done':
            return

        for item in cart:
            if item_to_remove.lower() in item["name"].lower():
                cart.remove(item)
                print(f"{item['name']} has been removed from your cart.")
                return
        print("Item not found in your cart.")


def view_cart():
    if cart:
        print("Your Cart:")
        total_price = 0
        for item in cart:
            item_name = item["name"]
            item_price = item["price"]
            item_quantity = item["quantity"]
            item_total = item_price * item_quantity
            total_price += item_total
            print(f"{item_quantity} x {item_name} - {item_price} EGP each, Total: {item_total} EGP ")
            print(f"Total Cart Value: {total_price} EGP")
            payment_summary(total_price)
    else:
            print("Your cart is empty.")


def payment_summary(subtotal):
    delivery_fee = 35
    service_fee = 20
    total_amount = subtotal + delivery_fee + service_fee

    print("\nPayment Summary:")
    print(f"Subtotal: {subtotal} EGP")
    print(f"Delivery Fee: {delivery_fee} EGP")
    print(f"Service Fee: {service_fee} EGP")
    print(f"Total Amount: {total_amount} EGP")


def checkout(user_info, restaurant):
    if not cart:
        print("Your cart is empty. Please add items to your cart before proceeding.")
        return

    subtotal = sum(item["price"] * item["quantity"] for item in cart)

    if user_info:
        order_number = random.randint(100, 500)
        order_date = "18 / 12 / 2022"
        user_name = user_info["name"]
        user_phone = user_info["phone"]
        user_address = user_info["address"]

        print("\nCheckout Information:")
        print("Name: " + user_name)
        print("Phone: " + str(user_phone))
        print("Address: " + user_address)

        while True:
            payment_method = input("Please choose a payment method (Visa / Cash): ").lower()
            if payment_method in ['cash']:
                print(f"You selected {payment_method.capitalize()} as your payment method.")
                break
            elif payment_method in ['visa']:
             visa1 = int(input("Please enter the visa number "))
             visa2 = int(input("Please enter the expiration date of visa"))
             visa3 = int(input("Please enter the CVV"))
             print("Checkout successfully")
             break
            else:
             print("Invalid payment method selected. Please choose 'Visa' or 'Cash'. ")

            delivery_fee = 35
            service_fee = 20
            total_amount = subtotal + delivery_fee + service_fee

            print("\nOrder Confirmation:")
            print("Date: " + order_date)
            print("Restaurant: " + restaurant)
            print("Order Number: " + str(order_number))
            print("User Address: " + user_address)
            print("User Phone: " + str(user_phone))
            print("\nOrder Items:")

            for item in cart:
                item_name = item["name"]
                item_price = item["price"]
                item_quantity = item["quantity"]
                item_total = item_price * item_quantity
                print(f"{item_quantity} x {item_name} - {item_price} EGP each, Total: {item_total} EGP ")

            print("\nOrder Subtotal: " + str(subtotal) + " EGP")
            print("Delivery Fee: " + str(delivery_fee) + " EGP")
            print("Service Fee: " + str(service_fee) + " EGP")
            print("Total Amount: " + str(total_amount) + " EGP")
            print("\nPayment Method: " + payment_method.capitalize())
            print("\nThank you for choosing us..")

    else:
      print("Please login or register to proceed with checkout.")

user_info = registration()


while True:
    display_categories()
    user_choice = input("Please choose the category number: ")

    if user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        user_choice = int(user_choice)
        if process_choice(user_choice):
           print("\nWould you like to:")
           print("1. Select another category")
           print("2. View your cart")
           print("3. Update items in your cart")
           print("4. Remove items from your cart")
           print("5. Go to checkout")
           print("6. Cancel")

           user_choice = input("Please enter the number corresponding to your choice: ").lower()
           if user_choice == "1":
               print("You chose to select another category.")
           elif user_choice == "2":
               view_cart()
           elif user_choice == "3":
               update_cart()
           elif user_choice == "4":
               remove_from_cart()
           elif user_choice == "5":
               checkout(user_info, "Bazooka")
               break
           elif user_choice == '6':
               print("Thank you for using our app")
               break
           else:
               print("Please enter a valid number")
    else:
     print("Invalid input. Please choose number from 1 to 4")