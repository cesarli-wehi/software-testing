import pytest
import math
import main


@pytest.mark.parametrize(
    "principal, rate, time, expected",
    [
        pytest.param(-1, 2.5, 10, "Principal must be a positive number", id='minMinusP'),
        pytest.param(0, 2.5, 10, 0.0, id='minP'),
        pytest.param(1, 2.5, 10, 1.28, id='minPlusP'),
        pytest.param(5000, 2.5, 10, 6400.42, id='nomP'),
        pytest.param(999999999, 2.5, 10, 1280084542.92, id='maxMinusP'),
        pytest.param(1000000000, 2.5, 10, 1280084544.19, id='maxP'),
        pytest.param(1000000001, 2.5, 10, "Principal must be less than a billion", id='maxPlusP'),
        pytest.param(5000, -1, 10, "Rate must be a positive number", id='minMinusR'),
        pytest.param(5000, 0, 10, 5000.0, id='minR'),
        pytest.param(5000, 0.1, 10, 5005.00, id='minPlusR'),
        pytest.param(5000, 2.5, 10, 6400.42, id='nomR'),
        pytest.param(5000, 99, 10, 4869683.87, id='maxMinusR'),
        pytest.param(5000, 100, 10, 5120000.0, id='maxR'),
        pytest.param(5000, 101, 10, "Rate must be between 0 and 100", id='maxPlusR'),
        pytest.param(5000, 2.5, 0, "Time must be a positive number and at least one year", id='minMinusT'),
        pytest.param(5000, 2.5, 1, 5125.0, id='minT'),
        pytest.param(5000, 2.5, 2, 5253.13, id='minPlusT'),
        pytest.param(5000, 2.5, 10, 6400.42, id='nomT'),
        pytest.param(5000, 2.5, 99, 57627.89, id='maxMinusT'),
        pytest.param(5000, 2.5, 100, 59068.58, id='maxT'),
        pytest.param(5000, 2.5, 101, "Time must be less than 100 years", id='maxPlusT'),
        ]
)
def test_calculate_interest(principal, rate, time, expected):
    try:
        actual_interest = main.calculate_interest(principal, rate, time)
        assert pytest.approx(actual_interest, 0.01) == expected
    except ValueError as e:
        assert str(e) == expected



def test_calculate_mortgage_payment(
    principal, annualInterestRate, termInYears, expected
):
    try:
        actual_payment = main.calculate_mortgage_payment(
            principal, annualInterestRate, termInYears
        )
        assert pytest.approx(actual_payment, 1) == expected
    except ValueError as e:
        assert str(e) == expected