# Simple Financial Calculator
# A beginner-friendly Python program for basic financial calculations

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("      SIMPLE FINANCIAL CALCULATOR")
    print("="*40)
    print("1. Simple Interest Calculator")
    print("2. Compound Interest Calculator")
    print("3. Loan EMI Calculator")
    print("4. Savings Goal Calculator")
    print("5. Currency Converter")
    print("6. Exit")
    print("="*40)

def simple_interest():
    """Calculate simple interest"""
    print("\n--- Simple Interest Calculator ---")
    
    try:
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
        
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        
        print(f"\nResults:")
        print(f"Principal: ${principal:.2f}")
        print(f"Interest Rate: {rate}%")
        print(f"Time: {time} years")
        print(f"Simple Interest: ${interest:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def compound_interest():
    """Calculate compound interest"""
    print("\n--- Compound Interest Calculator ---")
    
    try:
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
        compounds = int(input("Number of times interest compounds per year: "))
        
        rate_decimal = rate / 100
        amount = principal * (1 + rate_decimal/compounds) ** (compounds * time)
        interest = amount - principal
        
        print(f"\nResults:")
        print(f"Principal: ${principal:.2f}")
        print(f"Interest Rate: {rate}%")
        print(f"Time: {time} years")
        print(f"Compounding: {compounds} times per year")
        print(f"Compound Interest: ${interest:.2f}")
        print(f"Total Amount: ${amount:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def loan_emi():
    """Calculate loan EMI (Equated Monthly Installment)"""
    print("\n--- Loan EMI Calculator ---")
    
    try:
        loan_amount = float(input("Enter loan amount: $"))
        annual_rate = float(input("Enter annual interest rate (%): "))
        loan_term = float(input("Enter loan term (years): "))
        
        monthly_rate = (annual_rate / 100) / 12
        months = loan_term * 12
        
        # EMI formula: [P x R x (1+R)^N]/[(1+R)^N-1]
        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        total_payment = emi * months
        total_interest = total_payment - loan_amount
        
        print(f"\nResults:")
        print(f"Loan Amount: ${loan_amount:.2f}")
        print(f"Annual Interest Rate: {annual_rate}%")
        print(f"Loan Term: {loan_term} years ({months} months)")
        print(f"Monthly EMI: ${emi:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def savings_goal():
    """Calculate how much to save regularly to reach a goal"""
    print("\n--- Savings Goal Calculator ---")
    
    try:
        goal_amount = float(input("Enter your savings goal: $"))
        annual_rate = float(input("Enter expected annual return (%): "))
        years = float(input("Enter number of years to save: "))
        
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12
        
        # Monthly savings needed formula
        monthly_savings = goal_amount * monthly_rate / ((1 + monthly_rate) ** months - 1)
        total_savings = monthly_savings * months
        total_earned = goal_amount - total_savings
        
        print(f"\nResults:")
        print(f"Savings Goal: ${goal_amount:.2f}")
        print(f"Expected Return: {annual_rate}% per year")
        print(f"Time Period: {years} years")
        print(f"Monthly Savings Needed: ${monthly_savings:.2f}")
        print(f"Total Amount Saved: ${total_savings:.2f}")
        print(f"Interest Earned: ${total_earned:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def currency_converter():
    """Simple currency converter using fixed exchange rates"""
    print("\n--- Currency Converter ---")
    
    # Fixed exchange rates (for demonstration)
    exchange_rates = {
        'USD': 1.0,      # US Dollar (base)
        'EUR': 0.85,     # Euro
        'GBP': 0.73,     # British Pound
        'INR': 74.5,     # Indian Rupee
        'JPY': 110.0,    # Japanese Yen
        'CAD': 1.25,     # Canadian Dollar
        'AUD': 1.35      # Australian Dollar
    }
    
    print("Available currencies: USD, EUR, GBP, INR, JPY, CAD, AUD")
    
    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("From currency: ").upper()
        to_currency = input("To currency: ").upper()
        
        if from_currency in exchange_rates and to_currency in exchange_rates:
            # Convert to USD first, then to target currency
            usd_amount = amount / exchange_rates[from_currency]
            converted_amount = usd_amount * exchange_rates[to_currency]
            
            print(f"\nConversion Result:")
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print("Error: Invalid currency code!")
            
    except ValueError:
        print("Error: Please enter valid numbers!")

def financial_tips():
    """Display some basic financial tips"""
    print("\n--- Financial Tips ---")
    tips = [
        "Save at least 20% of your income",
        "Create a budget and track your expenses",
        "Pay off high-interest debt first",
        "Start investing early for compound growth",
        "Build an emergency fund (3-6 months of expenses)",
        "Diversify your investments",
        "Avoid unnecessary fees and charges"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")

def main():
    """Main function to run the financial calculator"""
    print("Welcome to the Simple Financial Calculator!")
    print("This calculator helps with basic financial calculations.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                simple_interest()
            elif choice == '2':
                compound_interest()
            elif choice == '3':
                loan_emi()
            elif choice == '4':
                savings_goal()
            elif choice == '5':
                currency_converter()
            elif choice == '6':
                print("\nThank you for using the Financial Calculator!")
                print("Here are some financial tips for you:")
                financial_tips()
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")
                
            # Ask if user wants to continue
            if choice != '6':
                continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower()
                if continue_calc != 'y':
                    print("\nThank you for using the Financial Calculator!")
                    financial_tips()
                    break
                    
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
