# Quiz

## Question 1
Given the function `est_affordability_calculator` which takes the following inputs

- it takes the following input 
    - `house_price`, a number bigger than 0 representing the hose price but smaller than a billion
    - `yearly_salary`, a positive number that represent the  yearly salary capped at one million
    - `deposit`, a positive number that represents the deposit on the house capped at one million
    - `interest_rate`, a number between 0 and 25 representing the interest percentage
    - `term_in_years`, a number between 0 and 40 representing the length of the mortgage
  
- this function works by assigning an affordability threshold that varies based on the house price, deposit and salary and then checks if the monthly payments fall below or above this affordability score.
- the affordability starts at `30%` and the barely affordable at `40%`. they both go up or down by the same amounts as described below
- houses can be in these thresholds:
    - `0 to 300,000 `and the affordability range is stays the same
    - `300,001 to 600,000` the affordability range goes up by `5%`
    - `600.001 to  900,000` the affordability range goes up by `10%`
    - `900,001 to a billion` the affordability range goes up by `15%`
- salary can be in these thresholds:
    - `0 to 50,000` and the affordability range is stays the same
    - `50,001 to 100,000` the affordability range goes down by `5%`
    - `100.001 to  150,000` the affordability range goes down by `10%`
    - `150,001 to a million` the affordability range goes down by `15%`
- deposit can be in these thresholds:
    - `0 to 50,000` and the affordability range is stays the same
    - `50,001 to 100,000` the affordability range goes down by `2%`
    - `100.001 to  150,000` the affordability range goes down by `4%`
    - `150,001 to a million` the affordability range goes down by `6%`
- interest can be in these thresholds:
    - `0 to 3` and the affordability range is stays the same
    - `3.01 to 5` the affordability range goes up by `2%`
    - `5.01 to 7` the affordability range goes up by `4%`
    - `7.01 to 25` the affordability range goes up by `6%`

- and produces the following outputs:
    - `affordable` if the yearly payments are less or equal to the affordability threshold, which is 30% of yearly salary
    - `barely affordable` if the  yearly payments are less or equal to the barely affordable threshold which is 40% of yearly salary
    - `unaffordable` otherwise
    - `ValueError("house price is too low")` if the `house_price` is below `0`
    - `ValueError("house price is too high")` if the `house_price` is more than `a billion`
    - `ValueError("yearly salary must be a positive number")` if the `yearly_salary` is below `0`
    - `ValueError("yearly salary is too high")` if the `yearly_salary` is above `a million`
    - `ValueError("deposit must be a positive number")` if the `deposit` is below `0`
    - `ValueError("deposit is too high")` if the `deposit` is above `a milliom`
    - `ValueError("Annual interest rate must be a positive number")` if the `interest_rate` is below `0`
    - `ValueError("Rate must be between 0 and 25")` if the `interest_rate` is above `25`
    - `ValueError("Term in years must be a positive number greater than zero")` if the `term_in_years` is less than `0`
    - `ValueError("Term in years must be less than 40 years")` if the `term_in_years` is bigger than `40`

And this test function written for you and in the `test_main.py file`
```python
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
```
write the test suite using pytest and parametrise it for a  strong normal using equivalence class testing basing your partitions on the inputs and choosing sensible partitions for this problem.
- given the large number of inputs limit yourself to two partitions per input
- show the partitions for each input


### answer
the nominal value is up to the student this is just an example, but a point should be reserved for sensible values

- 0 to 600000 and 600001 to 1000000000 for house price
- 0 to 100000 and 100001 to 1000000 for yearly salary
- 0 to 100000 and 100001 to 1000000  for deposit 
- 0 to 5 and 5.01 to 25 for rate
- 10 to 25 and 26 to 40 for the term

- the test table
    | Test      | house_price       | yearly_salary     | deposit   | interest_rate     | term_in_years     | expected result      |
    | :-----    | :------           | :----             |:-----     | :---------        | :---------        | :-----------------   |
    | eq1       | 300000            | 50000             | 50000     | 2.5               | 15                | "Affordable"  |
    | eq2       | 700000            | 50000             | 50000     | 2.5               | 15                | "Affordable"  |
    | eq3       | 300000            | 150000            | 50000     | 2.5               | 15                | "Affordable"  |
    | eq4       | 700000            | 150000            | 50000     | 2.5               | 15                | "Affordable"  |
    | eq5       | 300000            | 50000             | 150000    | 2.5               | 15                | "Affordable"  |
    | eq6       | 700000            | 50000             | 150000    | 2.5               | 15                | "Affordable"  |
    | eq7       | 300000            | 150000            | 150000    | 2.5               | 15                | "Affordable"  |
    | eq8       | 700000            | 150000            | 150000    | 2.5               | 15                | "Affordable"  |
    | eq9       | 300000            | 50000             | 50000     | 7.5               | 15                | "Affordable"  |
    | eq10      | 700000            | 50000             | 50000     | 7.5               | 15                | "Affordable"  |
    | eq11      | 300000            | 150000            | 50000     | 7.5               | 15                | "Affordable"  |
    | eq12      | 700000            | 150000            | 50000     | 7.5               | 15                | "Affordable"  |
    | eq13      | 300000            | 50000             | 150000    | 7.5               | 15                | "Affordable"  |
    | eq14      | 700000            | 50000             | 150000    | 7.5               | 15                | "Affordable"  |
    | eq15      | 300000            | 150000            | 150000    | 7.5               | 15                | "Affordable"  |
    | eq16      | 700000            | 150000            | 150000    | 7.5               | 15                | "Affordable"  |
    | eq17      | 300000            | 50000             | 50000     | 2.5               | 30                | "Affordable"  |
    | eq18      | 700000            | 50000             | 50000     | 2.5               | 30                | "Affordable"  |
    | eq19      | 300000            | 150000            | 50000     | 2.5               | 30                | "Affordable"  |
    | eq20      | 700000            | 150000            | 50000     | 2.5               | 30                | "Affordable"  |
    | eq21      | 300000            | 50000             | 150000    | 2.5               | 30                | "Affordable"  |
    | eq22      | 700000            | 50000             | 150000    | 2.5               | 30                | "Affordable"  |
    | eq23      | 300000            | 150000            | 150000    | 2.5               | 30                | "Affordable"  |
    | eq24      | 700000            | 150000            | 150000    | 2.5               | 30                | "Affordable"  |
    | eq25      | 300000            | 50000             | 50000     | 7.5               | 30                | "Affordable"  |
    | eq26      | 700000            | 50000             | 50000     | 7.5               | 30                | "Affordable"  |
    | eq27      | 300000            | 150000            | 50000     | 7.5               | 30                | "Affordable"  |
    | eq28      | 700000            | 150000            | 50000     | 7.5               | 30                | "Affordable"  |
    | eq29      | 300000            | 50000             | 150000    | 7.5               | 30                | "Affordable"  |
    | eq30      | 700000            | 50000             | 150000    | 7.5               | 30                | "Affordable"  |
    | eq31      | 300000            | 150000            | 150000    | 7.5               | 30                | "Affordable"  |
    | eq32      | 700000            | 150000            | 150000    | 7.5               | 30                | "Affordable"  |



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



## making it a bit more robust
- an important thing to do is to make the test suite robust at the very least
- errors in code happen often and we need to make sure the errors are handled
- in our specification the developers have put in the outputs value errors returns if the inputs are invalid, so in theory they've done a good job
- we still need to test it though
- let's add a min- and a max + to all of our inputs
    | Test      | principal     | rate  | time  | expected result   |
    | :-----    | :------       | :---- |:----- | :---------        |
    | minMinusP |   -1          | 2.5   | 10    | error             | 
    | minP      |   0           | 2.5   | 10    | 0.0               |          
    | minPlusP  |   1           | 2.5   | 10    | 1.28              |
    | nomP      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusP |   999999999   | 2.5   | 10    | 1280084542.92     |
    | maxP      |   1000000000  | 2.5   | 10    | 1280084544.19     |
    | maxPlusP  |   1000000001  | 2.5   | 10    | error             |
    | minMinusR |   5000        | -1    | 10    | error             |
    | minR      |   5000        | 0     | 10    | 5000.0            |          
    | minPlusR  |   5000        | 0.1   | 10    | 5005.00           |
    | nomR      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusR |   5000        | 99    | 10    | 4869683.87        |
    | maxR      |   5000        | 100   | 10    | 5120000.0         | 
    | maxPlusR  |   5000        | 101   | 10    | error             |
    | minMinusT |   5000        | 2.5   | 0     | error             |
    | minT      |   5000        | 2.5   | 1     | 5125.0            |          
    | minPlusT  |   5000        | 2.5   | 2     | 5253.13           |
    | nomT      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusT |   5000        | 2.5   | 99    | 57627.89          |
    | maxT      |   5000        | 2.5   | 100   | 59068.58          | 
    | maxPlusT  |   5000        | 2.5   | 101   | error             |

- ok now we have our table with all the errors as well, assuming single fault, and we can turn it into parameters.
- in our spec though we had some error outputs so what we should do is test if the errors are handled correctly, after all if they are the test shouldn't fail, the sut is behaving as intended.
- we will also add `ids` to our tests to make them easier to identify, they'll now show on your testing panel in vs code instead of the parameters
    ```python
    @pytest.mark.parametrize(
        "principal, rate, time, expected",
        [
            pytest.param(-1, 2.5, 10, "Principal must be a positive number", id='minMinusP'),
            pytest.param(0, 2.5, 10, 0.0, id='minP'),
            pytest.param(1, 2.5, 10, 1.28, id='minPlusP'),
            pytest.param(5000, 2.5, 10, 6400.42, id='nomP'),
            pytest.param(999999999, 2.5, 10, 1280084542.92, id='maxMinusP'),
            pytest.param(1000000000, 2.5, 10, 1280084544.19, id='maxP'),
            pytest.param(1000000001, 2.5, 10, "Principal must be a positive number", id='maxPlusP'),
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
    ```
- to run this test suite we'll have to also modify our test function like so:
    ```python
    def test_calculate_interest(principal, rate, time, expected):
        try:
            actual_interest = main.calculate_interest(principal, rate, time)
            assert pytest.approx(actual_interest, 0.01) == expected
        except ValueError as e:
            assert str(e) == expected