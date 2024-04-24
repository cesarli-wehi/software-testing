def calculate_interest(principal, rate, time):
        if principal < 0:
            raise ValueError("Principal must be a positive number")
        if principal > 1000000000:
            raise ValueError("Principal must be less than a billion")
        if rate < 0:
            raise ValueError("Rate must be a positive number")
        if rate > 100:
            raise ValueError("Rate must be between 0 and 100")
        if time <= 0:
            raise ValueError("Time must be a positive number and at least one year")
        if time > 100:
            raise ValueError("Time must be less than 100 years")

        return principal * (1 + rate / 100) ** time

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
        raise ValueError(
            "Term in years must be a positive number greater than zero"
        )
    if termInYears > 40:
        raise ValueError(
            "Term in years must be less than 40 years"
        )

    # Convert annual interest rate to monthly and decimal format
    dailyInterestRate = annualInterestRate / (100 * 365)
    # Convert term from years to months
    termInDays = termInYears * 365

    # Calculate monthly payment
    if dailyInterestRate == 0:
        return principal / termInDays * 30
    else:
        return (
            principal
            * dailyInterestRate
            * (1 + dailyInterestRate) ** termInDays
            / ((1 + dailyInterestRate) ** termInDays - 1)
        ) * 30