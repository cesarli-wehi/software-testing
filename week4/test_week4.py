import pytest
import week4

@pytest.mark.parametrize(
    "principal, annualInterestRate, termInYears, expected",
    [
        pytest.param(-1, 4.5, 30, "Principal must be a positive number", id='minMinusP'),
        pytest.param(0, 4.5, 30, 0.0, id='minP'),
        pytest.param(1, 4.5, 30, 0.0, id='minPlusP'),
        pytest.param(250000, 4.5, 30, 1248.29, id='nomP'),
        pytest.param(999999999, 4.5, 30, 4993168.03, id='maxMinusP'),
        pytest.param(1000000000, 4.5, 30, 4993168.04, id='maxP'),
        pytest.param(1000000001, 4.5, 30, "Principal must be less than a billion", id='maxPlusP'),
        pytest.param(250000, -1, 30, "Annual interest rate must be a positive number", id='minMinusR'),
        pytest.param(250000, 0, 30, 684.93, id='minR'),
        pytest.param(250000, 0.1, 30, 685.04, id='minPlusR'),
        pytest.param(250000, 4.5, 30, 1248.29, id='nomR'),
        pytest.param(250000, 24, 30, 4935.20, id='maxMinusR'),
        pytest.param(250000, 25, 30, 5139.84, id='maxR'),
        pytest.param(250000, 26, 30, "Rate must be between 0 and 25", id='maxPlusR'),
        pytest.param(250000, 4.5, 0, "Term in years must be a positive number greater than zero", id='minMinusT'),
        pytest.param(250000, 4.5, 1, 21015.01, id='minT'),
        pytest.param(250000, 4.5, 2, 10743.87, id='minPlusT'),
        pytest.param(250000, 4.5, 30, 1248.29, id='nomT'),
        pytest.param(250000, 4.5, 39, 1117.99, id='maxMinusT'),
        pytest.param(250000, 4.5, 40, 1107.80, id='maxT'),
        pytest.param(250000, 4.5, 41, "Term in years must be less than 40 years", id='maxPlusT'),
    ]
)

def test_calculate_mortgage_payment(
    principal, annualInterestRate, termInYears, expected
):
    try:
        actual_payment = week4.calculate_mortgage_payment(
            principal, annualInterestRate, termInYears
        )
        assert pytest.approx(actual_payment, 1) == expected
    except ValueError as e:
        assert str(e) == expected

@pytest.mark.parametrize(
    "house_price, yearly_salary, deposit, interest_rate, term_in_years, expected",
    [
        pytest.param(200000, 45000, 20000, 1.5, 15, "Affordable", id="eq1"),
        pytest.param(550000, 75000, 50000, 4, 30, "Barely Affordable", id="eq2"),
        pytest.param(950000, 120000, 70000, 9, 35, "Unaffordable", id="eq3"),
        pytest.param(-10, 30000, 100000, 3, 25, "house price is too low", id="eq4"),
        pytest.param(2000000000, 30000, 100000, 3, 35, "house price is too high", id="eq5"),
        pytest.param(250000, -10, 100000, 3, 35, "yearly salary must be a positive number", id="eq6"),
        pytest.param(250000, 33000000, 100000, 3, 35, "yearly salary is too high", id="eq7"),
        pytest.param(250000, 30000, -111, 3, 35, "deposit must be a positive number", id="eq8"),
        pytest.param(250000, 30000, 10000000, 3, 35, "deposit is too high", id="eq9"),
        pytest.param(250000, 30000, 100000, -2, 35, "Annual interest rate must be a positive number", id="eq10"),
        pytest.param(250000, 30000, 100000, 35, 35, "Rate must be between 0 and 25", id="eq11"),
        pytest.param(250000, 30000, 100000, 3, 0, "Term in years must be a positive number greater than zero", id="eq12"),
        pytest.param(250000, 30000, 100000, 3, 85, "Term in years must be less than 40 years", id="eq13"),
    ],
)
def test_affordability_calculator(
    house_price, yearly_salary, deposit, interest_rate, term_in_years, expected
):
    try :
        assert (
            week4.affordability_calculator(
                house_price, yearly_salary, deposit, interest_rate, term_in_years
            )
            == expected
        )
    except ValueError as e:
        assert str(e) == expected
