# Quiz

## Question 1
Given the function `calculate_mortgage_payment` which takes the following inputs

- principal
  - a positive number from 
- annualInterestRate
  - a positive number
- termInYears
  - a positive number

and the following outputs:
- the mortgage payment as a number
- ValueError("Principal must be a positive number")
  - if the principal is not a valid input
- ValueError("Principal must be less than a billion")
    - if the principal is larger than a billion
- ValueError("Annual interest rate must be a positive number")
  - if the annualInterestRate is not a valid
- ValueError("Rate must be between 0 and 25")
    - if the annualInterestRate is more than 25
- ValueError("Term in years must be a positive number greater than zero")
  - if the termInYears is not a valid input
- ValueError("Term in years must be less than 40 years")
  - if the termInYears is more than 40 years

And this test function written for you and in the `test_main.py file`
```python
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
```
write the test suite using pytest and parametrise it for a robust weak normal.


### answer
the nominal value is up to the student this is just an example, but a point should be reserved for sensible values

- the test table
    | Test      | principal     | rate  | time  | expected result   |
    | :-----    | :------       | :---- |:----- | :---------        |
    | minMinusP |   -1          | 4.5   | 30    | error             | 
    | minP      |   0           | 4.5   | 30    | 0.0               |          
    | minPlusP  |   1           | 4.5   | 30    | 0.0              |
    | nomP      |   250000      | 4.5   | 30    | 1248.29           |
    | maxMinusP |   999999999   | 4.5   | 30    | 4993168.03        |
    | maxP      |   1000000000  | 4.5   | 30    | 4993168.04        |
    | maxPlusP  |   1000000001  | 4.5   | 30    | error             |
    | minMinusR |   250000      | -1    | 30    | error             |
    | minR      |   250000      | 0     | 30    | 684.93            |          
    | minPlusR  |   250000      | 0.1   | 30    | 685.04            |
    | nomR      |   250000      | 4.5   | 30    | 1248.29           |
    | maxMinusR |   250000      | 24    | 30    | 4935.20           |
    | maxR      |   250000      | 25    | 30    | 5139.84           | 
    | maxPlusR  |   250000      | 26    | 30    | error             |
    | minMinusT |   250000      | 4.5   | 0     | error             |
    | minT      |   250000      | 4.5   | 1     | 21015.01          |          
    | minPlusT  |   250000      | 4.5   | 2     | 10743.87          |
    | nomT      |   250000      | 4.5   | 30    | 1248.29           |
    | maxMinusT |   250000      | 4.5   | 39    | 1117.99           |
    | maxT      |   250000      | 4.5   | 40    | 1107.80           | 
    | maxPlusT  |   250000      | 4.5   | 11    | error             |


- the parametrised test suite
```python
@pytest.mark.parametrize(
    "principal, rate, time, expected",
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
```