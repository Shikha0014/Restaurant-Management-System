# Importing neccessary libraries
import pandas as pd 
from tabulate import tabulate
import sys
import warnings 
warnings.filterwarnings("ignore")   # Using "warnings" library to supress unwanted warnings in terminal

MENU = pd.read_csv("./new_age_indian_cafe_menu.csv")     # Reading the menu csv file using pandas (Global variable)
ORDER = []                                               # Creating empty list to store future order information (Global variable)

def view_menu():                                
    # This function is used to print the menu of the restaurant in a tabular form on the terminal.
    # Tabulate library is used in this function to print the dataframe in a tabular format.
    
    print("NEW AGE INDIAN CAFE MENU")           
    print(tabulate(MENU,headers='keys',tablefmt='psql'))

def order():
    # This function is used to handle the order logic of the restaurant by taking input from the user.
    while True:
        item = input("Please enter the name of the item.").strip()      # Taking the input from the user 

        if item.lower() not in MENU['Item Name'].str.lower().values:   # Doing input validation of the user input using string methods
            print("Sorry, that item is not on the menu. Please try again.")
            continue

        quantity = input(f"How many servings of {item} would you like? ").strip()   # Taking the input from the user 


        if not quantity.isdigit() or int(quantity)<=0:        # Doing input validation of the user input using integer comparisons  
            print("Invalid quantity. Please enter a positive number.")
            continue
        
        ORDER.append((item, int(quantity)))         # Appending the order informaton in the ORDER list

        while True:
            # Taking input from the user and validating it for ordering mutiple items

            more = input("Would you like to order another item? (yes/no): ").strip().lower()

            if more in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if more == "no":
            calculate_bill()        # Calculating bill after user has finished ordering
            break

def calculate_bill():
    # Calculating the total bill of the order and presenting the order summary in a table format
    total = 0
    print("\nYour Order Summary:")
    print(f"{'Item':<30}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)

    for item_name, quantity in ORDER:
        price = MENU.loc[MENU["Item Name"] == item_name, "Unit Price"].values[0]
        total_price = price*quantity
        print(f"{item_name:<30}{quantity:<10}{total_price:<10}")
        total += total_price

    gst = round(0.05 * total,2)
    tax = round(0.06 * total,2)
    print("-" * 50)
    print(f"{'Bill':<30}{total:<10}")
    total = gst+tax+total
    print(f"{'GST ':<30}{gst:<10}")
    print(f"{'Service Tax ':<30}{tax:<10}")
    print("-" * 50)
    print(f"{'Total Amount':<30}{total:<10}")
    print("Thanks for your order.")    

    
def main():
    # This function handles the main logic of the ordering system by acting as a initial entering point in the code
    print("Hi! Welcome to the New Age Indian Cafe")
    while True:
        ans = input("Would you like to order? (Yes/No)").strip().lower()
        if ans == "yes":
            view_menu()
            order()
            break
        elif ans == "no":
            print("Bye!")
            sys.exit()
        else:
            print("Invalid Input! Please try again.")

if __name__ == "__main__":      # This is the entry point of the python script while running it into the terminal
    main()

