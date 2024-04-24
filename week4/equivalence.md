# Equivalence class testing example

Continuing on from last week, this week we'll look at performing equivalence class testing

## an example
- now we're working on a mortgage affordability calculator, wh
- the function calculates the future value of an investment by calculating the compound interest over a period of time
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
- the function will look like this 
    ```python
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
        house_price_ranges = [(0, 300000),(300001, 600000),(600001, 900000),(900001, 1000000000)]
        salary_ranges = [(0, 50000),(50001, 100000),(100001, 150000),(150001, 1000000)]
        deposit_ranges = [(0, 50000),(50001, 100000),(100001, 150000),(150001, 1000000)]
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
    ```
- to start testing this function we need to create a `test_main.py` and write our test suite
- then we can inport the packages we need as we did before
    ```python
    import pytest
    import main
    ```
- then we need to write our test function
    ```python
    def test_affordability_calculator(
        house_price, yearly_salary, deposit, interest_rate, term_in_years, expected
    ):
        assert (
            main.affordability_calculator(
                house_price, yearly_salary, deposit, interest_rate, term_in_years
            )
            == expected
        )
    ```
- the next step is to write the test suite.
- to do that we first have to decide if we want to test based on input or output and from there derive our test classes
- the valid inputs are:
    - we have the `house_price` input which is `0 < house_price < 1000000000`
    - we have then the `yearly_salary` input which is `0 < yearly_salary <= 100`
    - the `deposit` input can be expressed as `0 < deposit < 1000000`
    - the `interest_rate` input is going to be `0 < interest_rate < 25`
    - the `term_in_years` input is expressed as `1 < term_in_years < 25`
- the valid outputs are going to be:
    - `Affordable`
    - `Barely Affordable`
    - `Unaffordable`
- now the formula to calculate a mortgage payment is a bit complex so to figure it out you can use and online one or assume the one in the `week4.py` is correct, it is also the one our affordability test uses. once you have the mortgage payment just calculate it as a percentage of the yearly salary (with the right modifiers applied) and see how it should come out.
- so for instance for a house price of `200000`, a deposit of `20000`, a rate of `1.5` and a term of `15` years the payment should be `1117` pounds a month or `13404` a year
- with these numbers and a salary of `45000` the modifiers stay at `0` so the affordability would be at `30%` of the salary and barely affordable at `40%` 
- so `13404` of `45000` is about `29%` so it is affordable!
- in this example I will split the equivalence classes on the outputs
    | Test      | house_price       | yearly_salary     | deposit   | interest_rate     | term_in_years     | expected result       |
    | :-----    | :------           | :----             |:-----     | :---------        | :---------        | :---------            |
    | eq1       | 200000            | 45000             | 20000     | 1.5               | 15                | "Affordable"          |
    | eq2       | 550000            | 75000             | 50000     | 4                 | 30                | "Barely Affordable"   |
    | eq3       | 950000            | 120000            | 70000     | 9                 | 35                | "Unaffordable"        |

- the next task is to convert this test suite into parameters for pytest
    ```python
    @pytest.mark.parametrize(
        "house_price, yearly_salary, deposit, interest_rate, term_in_years, expected",
        [
            pytest.param(200000, 45000, 20000, 1.5, 15, "Affordable", id='eq1'),
            pytest.param(550000, 75000, 50000, 4, 30, "Barely Affordable", id='eq2'),
            pytest.param(950000, 120000, 70000, 9, 35, "Unaffordable", id='eq3'),
        ]
    )
    ```

- now we can run the tests using pytest in the terminal or by running them in the testing section in vs code  as we did before
- hopefully they will all pass :)

## making this test suite more robust

- now that we have done a weak normal equivalence class test, it would onl make sense to try and improve it to make it more robust.
- to make it robust we will have to take values from invalid classes from each of our inputs so we will have:
    - 2 invalid for `house_price` one below 0 and one above a billion
    - 2 invalid for `yearly_salary` one below 0 and one above a million
    - 2 invalid for `deposit` one below 0 and one above a million
    - 2 invalid for `interest_rate` one below 0 and one above 25
    - 2 invalid for `term_in_years` one below 1 and one above 40
- putting it all together we have
    | Test      | house_price       | yearly_salary     | deposit   | interest_rate     | term_in_years     | expected result                                               |
    | :-----    | :------           | :----             |:-----     | :---------        | :---------        | :----------------------------------------------------------   |
    | eq1       | 200000            | 45000             | 20000     | 1.5               | 15                | "Affordable"                                                  |
    | eq2       | 550000            | 75000             | 50000     | 4                 | 30                | "Barely Affordable"                                           |
    | eq3       | 950000            | 120000            | 70000     | 9                 | 35                | "Unaffordable"                                                |
    | eq4       | -10               | 30000             | 100000    | 3                 | 25                | "house price is too low"                                      |
    | eq5       | 2000000000        | 30000             | 100000    | 3                 | 35                | "house price is too high"                                     |
    | eq6       | 250000            | -10               | 100000    | 3                 | 35                | "yearly salary must be a positive number"                     |
    | eq7       | 250000            | 33000000          | 100000    | 3                 | 35                | "yearly salary is too high"                                   |
    | eq8       | 250000            | 30000             | -111      | 3                 | 35                | "deposit must be a positive number"                           |
    | eq9       | 250000            | 30000             | 10000000  | 3                 | 35                | "deposit is too high"                                         |
    | eq10      | 250000            | 30000             | 100000    | -2                | 35                | "Annual interest rate must be a positive number"              |
    | eq11      | 250000            | 30000             | 100000    | 35                | 35                | "Rate must be between 0 and 25"                               |
    | eq12      | 250000            | 30000             | 100000    | 3                 | 0                 | "Term in years must be a positive number greater than zero"   |
    | eq13      | 250000            | 30000             | 100000    | 3                 | 85                | "Term in years must be less than 40 years"                     |


- turning these into pytests we get
    ```python
        @pytest.mark.parametrize(
        "house_price, yearly_salary, deposit, interest_rate, term_in_years, expected",
        [
            pytest.param(200000,    45000,      20000,      1.5,    15, "Affordable", id='eq1'),
            pytest.param(550000,    75000,      50000,      4,      30, "Barely Affordable", id='eq2'),
            pytest.param(950000,    120000,     70000,      9,      35, "Unaffordable", id='eq3'),
            pytest.param(-10,       30000,      100000,     3,      25, "house price is too low", id='eq4'),
            pytest.param(2000000000,30000,      100000,     3,      35, "house price is too high", id='eq5'),
            pytest.param(250000,    -10,        100000,     3,      35, "yearly salary must be a positive number", id='eq6'),
            pytest.param(250000,    33000000,   100000,     3,      35, "yearly salary is too high", id='eq7'),
            pytest.param(250000,    30000,      -111,       3,      35, "deposit must be a positive number", id='eq8'),
            pytest.param(250000,    30000,      10000000,   3,      35, "deposit is too high", id='eq9'),
            pytest.param(250000,    30000,      100000,     -2,     35, "Annual interest rate must be a positive number", id='eq10'),
            pytest.param(250000,    30000,      100000,     35,     35, "Rate must be between 0 and 25", id='eq11'),
            pytest.param(250000,    30000,      100000,     3,      0, "Term in years must be a positive number greater than zero", id='eq12'),
            pytest.param(250000,    30000,      100000,     3,      85, "Term in years must be less than 40 years", id='eq13'),
        ]
    )
    ```

- now that we have our tests we need to change our method to return the value error like so:
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