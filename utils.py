def calculate_home_affordability(house_budget, monthly_payment, interest_rate, loan_term):
    """
    Calculates the maximum home price a user can afford.
    """
    return house_budget + (monthly_payment * (12 * loan_term) * (1 - interest_rate / 100))

def calculate_car_affordability(car_budget, monthly_payment, loan_term):
    """
    Calculates the maximum car price a user can afford.
    """
    return car_budget + (monthly_payment * loan_term * 12)

def calculate_investment_growth(initial_investment, monthly_contribution, interest_rate, years):
    """
    Computes future value of an investment using compound interest formula.
    """
    return initial_investment * ((1 + interest_rate / 100) ** years) + \
           (monthly_contribution * (((1 + interest_rate / 100) ** years - 1) / (interest_rate / 100)))
