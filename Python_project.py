import pyttsx3 
 
 
Menu = { 
                  "A1" : { 
                  "name"  : "Hot Coffee", 
                  'Quantity': 1, 
                  "price" : '1.20$' 
          }, 
                  "A2" : { 
                  "name"  : "Ice Americano", 
                'Quantity' : 1, 
                  "price" : '1.20$' 
          }, 
                  "A3" : { 
                  "name"  : "Ice Latte", 
                  'Quantity' : 1, 
                  "price" : '1.50$' 
          }, 
                  "A3" : { 
                  "name"  : "Ice Latte", 
                  'Quantity' : 1, 
                  "price" : '1.50$' 
          }, 
                  "A4" : { 
                  "name":"Ice Cappucino ", 
                  "Quantity":1, 
                  "price" :"1.50$" 
          }, 
                  "A5" : { 
                  "name"  : "Ice Mocha ", 
                  'Quantity' : 1, 
                  "price" : '1.80$' 
          }, 
                  "A6" : { 
                  "name"  : "Caramel Frappe", 
                  'Quantity' : 1, 
                  "price" : '2.00$' 
                  }
        }

def dic():
        print('>>. Show all drink information: ')
        print('-' * 100)

        for item in ['Drinks ID', 'Drink Name', 'Quantity', 'Price']:
                print(item, end = '\t')
        print('')
        print('-'* 100)

        for drink in Menu.items():
                print(f"{drink[0]} \t\t{drink[1]['name']}  \t\t{drink[1]['Quantity']} \t\t{drink[1]['price']}")

        print('-'*100)
dic()
 
def Admin_AskForChoice(): 
 
        print(''' 
                  Choose what you want to do: 
                  1. Add drinks to menu (Name or price) 
                  2. Change Price of any drinks 
                  3. Delete drinks from menu 
                  4. View Transaction history
        ''') 
        choice = int(input('Your choice: ')) 
        return choice 
def Admin_Add_Drinks(): 
          
        
        code = input('Enter the code of the drinks:') 
        Menu[code] = {}
        
        Name = input('Enter the name: ') 
        qty = input('Enter the qty: ') 
        price = input('Enter the price: ') 
        Menu[code]['name']= Name 
        Menu[code]['Quantity'] = qty 
        Menu[code]['price'] = price  

        dic() 

def Admin_Change_info():

        code = input('Enter the code of the drinks:')
        new_price = input('Enter the new price: ')
        Menu[code]['price'] = new_price
        print(Menu)
        dic()
def Admin_Delete_Drinks():

        code = input('Enter the code of the drinks that you want to delete:')
        Menu[code]
        x = Menu.pop(code)
        print(x)

        print(Menu)
        dic()
def Customer_Require_input():

        qty = int(input('How many drinks you want:')) 
        size = str(input('Choose the size you want :')) 
        sugar = int(input('How much sugar you want:')) 
        ice = int (input('How much ice you want:')) 
        take = str(input('You want to take a way or stay in:')) 
        suggestion = str(input('Make a suggestion:'))
        return qty, size, sugar, ice, take, suggestion

def Customer_AskForChoice():

        dic()
        choice1 = int(input('Enter the drink that you want to order: '))


def Customer_Making_Order():
        dic()
        choice1 = Customer_AskForChoice
        qty, size, sugar, ice, take, suggestion = Customer_Require_input() 

        if (choice1 == 1): 
                  print(f'You bought {qty} Hot Coffee. Total price {qty * 1.20}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.')
        elif (choice1 == 2):  
                  print(f'You bought {qty}  Ice Americano. Total price {qty * 1.50}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.')  
        elif (choice1 == 3): 
                  print( 'You bought {qty} Ice Latte. Total price {qty * 1.50}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.') 
        elif (choice1 == 4): 
                  print(f'You bought {qty} Ice Cappucino . Total price {qty * 1.80}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.') 
        elif (choice1 == 5): 
                  print(f"You bought {qty} Ice Mocha. Total price {qty * 1.00}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.") 
        elif (choice1 == 6): 
                  print(f'You bought {qty} Caramel Frappe. Total price {qty * 2.00}$ Size {size} Sugar {sugar}% Ice {ice}% Take {take} Suggestion {suggestion}.')
        else:
                print("Invaild Input!")

def Admin_Command():
          
        
        choice = Admin_AskForChoice()
         
        if choice == 1:
                   Admin_Add_Drinks()
        elif choice == 2:
                  Admin_Change_info()
        elif choice == 3:
                  Admin_Delete_Drinks()
        else:
                  print('Invaild Input!')
def Customer_Command():
         
        engine = pyttsx3.init()
        engine.say('Welcome to our EYC Cafe shop!!!. This is a self-order assistant , what can i do for you ?')
        engine.runAndWait()
        print('''
                  1. Show all drinks information 
                  2. Buy drinks and display information
                  3. Search any drinks specifically
        ''')
         
        choose_command = int(input('Choose the number of sevice: '))
         
        if choose_command == 1:
                dic()
        elif choose_command == 2:

                Customer_Making_Order()
        else:    
                ('Invaild Input!')

def Choose_Status():

        print('''*** Chosse you Status ***'
                1. Admin
                2. Customer
        ''')
        choice = int(input('Enter you status: '))
        if (choice == 1):
                Admin_Command()
        elif (choice == 2):
                Customer_Command()
                   
        else:
                print('Invaild Input!')
Choose_Status()

# if __name__ == '__main__':

