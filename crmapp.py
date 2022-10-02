import os

# declare variables
customers=[]

while True:
    # Build CRM Menu
    os.system("clear")
    print("***************************")
    print("1- Add Customer")
    print("2- List All Customers")
    print("3- Delete Customer")
    print("4- Exit")
    print("***************************")
    choice=int( input("Select an option: ") )
    if choice==1:
        customerName=input("Please type customer name: ")
        customers.append(customerName)
        print("Done Adding the new customer")
        input("Press Enter To continue ...")
    elif choice==2:
        print(customers)
        #for cust in customers:
            #print(cust)
        input("Press Enter To continue ...")
    elif choice==3:
        # Ask the User for customer name that need to be deleted
        custName = input("Please type customer name: ")
        # Search for a customer name 
        isFound=False #To check if customer not found and break the loop
        for cust in customers:
            # Checking customer found or no
            if cust==custName: # Customer Found
                isFound==True
         
        # Check if the customer name exist in customer list or not
            userConfirmation = input(f"Customer found, Are you sure you want to delete {cust} (Y/N)")
            if userConfirmation=="Y":
                # Remove customer from list
                customers.remove(custName)
                print(f"Customer has been deleted {cust}")
                isFound=True #If customer is found 
                break
            else: #if customer not found
                break;
        if isFound==False:
            print("Customer is not deleted")
        input("Press Enter To continue ...")
        
    elif choice==4:
        print("Thank you for using CRMApp .. Good Bye")
        input("Press Enter To continue ...")
        break # stop the while loop
    else:
        print("Sorry, You can select between number between 1 and 4")
        input("Press Enter To continue ...")
    



