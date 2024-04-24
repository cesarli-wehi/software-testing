def calculate_mortgage_payment(principal, annualInterestRate, termInYears):
    if principal < 0:
        raise ValueError("Principal must be a positive number")
    if principal > 1000000000:
        raise ValueError("Principal must be less than a billion")
    if annualInterestRate < 0:
        raise ValueError("Annual interest rate must be a positive number")
    if annualInterestRate > 25:
        raise ValueError("Rate must be between 0 and 25")
    if termInYears <= 0:
        raise ValueError("Term in years must be a positive number greater than zero")
    if termInYears > 40:
        raise ValueError("Term in years must be less than 40 years")

    monthlyInterestRate = annualInterestRate / (12 * 100)
    numberOfPayments = termInYears * 12

    if monthlyInterestRate == 0:  # Handle the case where interest rate is 0
        monthlyPayment = principal / numberOfPayments
    else:
        monthlyPayment = (
            principal
            * monthlyInterestRate
            * (1 + monthlyInterestRate) ** numberOfPayments
            / ((1 + monthlyInterestRate) ** numberOfPayments - 1)
        )

    return monthlyPayment
        


def affordability_calculator( 
    house_price, yearly_salary, deposit, interest_rate, term_in_years
):
    if house_price < 0:
        raise ValueError("house price is too low")
    if house_price > 1000000000:
        raise ValueError("house price is too high")
    if yearly_salary < 0:
        raise ValueError("yearly salary must be a positive number")
    if yearly_salary > 1000000:
        raise ValueError("yearly salary is too high")
    if deposit < 0:
        raise ValueError("deposit must be a positive number")
    if deposit > 1000000:
        raise ValueError("deposit is too high")
    if interest_rate < 0:
        raise ValueError("Annual interest rate must be a positive number")
    if interest_rate > 25:
        raise ValueError("Rate must be between 0 and 25")
    if term_in_years <= 0:
        raise ValueError("Term in years must be a positive number greater than zero")
    if term_in_years > 40:
        raise ValueError("Term in years must be less than 40 years")
    # Define the affordability thresholds
    affordable_threshold = 0.3  # 30% of yearly salary
    barely_affordable_threshold = 0.4  # 40% of yearly salary

    # Define ranges for house price, salary, deposit, and interest rates
    house_price_ranges = [
        (0, 300000),
        (300001, 600000),
        (600001, 900000),
        (900001, 1000000000),
    ]
    salary_ranges = [
        (0, 50000),
        (50001, 100000),
        (100001, 150000),
        (150001, 1000000),
    ]
    deposit_ranges = [
        (0, 50000),
        (50001, 100000),
        (100001, 150000),
        (150001, 1000000),
    ]
    interest_rate_ranges = [(0, 3), (3.01, 5), (5.01, 7), (7.01, 25)]

    # Adjust affordability thresholds based on ranges
    for range in house_price_ranges:
        if range[0] <= house_price <= range[1]:
            affordable_threshold += 0.05 * house_price_ranges.index(range)
            barely_affordable_threshold += 0.05 * house_price_ranges.index(range)
            break

    for range in salary_ranges:
        if range[0] <= yearly_salary <= range[1]:
            affordable_threshold -= 0.05 * salary_ranges.index(range)
            barely_affordable_threshold -= 0.05 * salary_ranges.index(range)
            break

    for range in deposit_ranges:
        if range[0] <= deposit <= range[1]:
            affordable_threshold -= 0.02 * deposit_ranges.index(range)
            barely_affordable_threshold -= 0.02 * deposit_ranges.index(range)
            break

    for range in interest_rate_ranges:
        if range[0] <= interest_rate <= range[1]:
            affordable_threshold += 0.02 * interest_rate_ranges.index(range)
            barely_affordable_threshold += 0.02 * interest_rate_ranges.index(range)
            break

    # Calculate the loan amount
    loan_amount = house_price - deposit

    # Calculate the monthly payment using the annuity formula
    monthly_payment = calculate_mortgage_payment(
        loan_amount, interest_rate, term_in_years
    )

    # Calculate the yearly payment
    yearly_payment = monthly_payment * 12

    # Determine affordability
    if yearly_payment <= affordable_threshold * yearly_salary:
        return "Affordable"
    elif yearly_payment <= barely_affordable_threshold * yearly_salary:
        return "Barely Affordable"
    else:
        return "Unaffordable"