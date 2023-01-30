def loan_calculator(principal, rate, term):
    """
    Calculates the monthly payment and total payment for a loan
    """
    monthly_rate = rate / 12
    num_payments = term * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-num_payments)
    total_payment = monthly_payment * num_payments
    
    return monthly_payment, total_payment

# Prompt user to enter loan data
principal = float(input("Enter the loan principal: "))
rate = float(input("Enter the annual interest rate: "))
term = float(input("Enter the loan term in years: "))

# Calculate loan payments
monthly_payment, total_payment = loan_calculator(principal, rate, term)

# Display results
print("Monthly Payment: ", monthly_payment)
print("Total Payment: ", total_payment)
