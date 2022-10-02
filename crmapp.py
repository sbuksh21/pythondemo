import os

# declare variables
customers=[]
Tax_Rate=3

# Functions
# ===========================================
def get_salary_after_tax(salary,tax_rate):
    return salary-(salary*(tax_rate/100))

while True:
    # Build CRM Menu
    os.system("clear")
    print("***************************")
    print("1- Add Customer")
    print("2- List All Customers")
    print("3- Delete Customer")
    print("4- Calculate Salary After Tax")
    print("5- Exit")
    print("***************************")
    choice=int( input("Select an option: ") )
    if choice==1:
        customerName=input("Please type customer name: ")
        customerSalary=float(input("Please type customer Salary: "))
        customers.append([customerName,customerSalary])
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
            if cust[0]==custName: # Customer Found
                isFound==True
                
         
        # Check if the customer name exist in customer list or not
            userConfirmation = input(f"Customer found, Are you sure you want to delete {cust} (Y/N)")
            if userConfirmation=="Y":
                # Remove customer from list
                customers.remove(cust)
                print(f"Customer has been deleted {cust}")
                isFound=True #If customer is found 
                break
            else: #if customer not found
                break;
        if isFound==False:
            print("Customer is not deleted")
        input("Press Enter To continue ...")
        
    elif choice==4:
        # Calculate Salary after apply the tax rate
        # ask the user for customer name that need to be deleted
        custName=input("Please type the customer name: ")
        
        # search for a customer using above collected value
        isFound=False
        
        
        
        for cust in customers:
            
            # check if customer exist inside the list of customers or not
            if cust[0]==custName: # Customer Found
                #change the isFound flag to true
                isFound=True
                
                # calculate the salary after tax deduction
                currentSalary=cust[1]
                salaryAfterTax=get_salary_after_tax(currentSalary,Tax_Rate)
                print(f"Current Salary: {currentSalary} - Salary Ater Tax: {salaryAfterTax}")
                
    
        if isFound==False:
            print("Sorry, Customer Not Found, Please type another name")        
        
        input("Press Enter To continue ...")
    
        
    elif choice==5:
        print("Thank you for using CRMApp .. Good Bye")
        input("Press Enter To continue ...")
        break # stop the while loop
    else:
        print("Sorry, You can select between number between 1 and 4")
        input("Press Enter To continue ...")