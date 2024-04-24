# Setting up pytest

Pytest is the tool we will use to run our tests in this course. 
It is a slightly more complete testing environment that what ships with pyton and it will allow us to do all we need for this course to a professional level.

- It is very easy to install and we can do it by typing this into the terminal:
```bash
pip install pytest
```
    remember for mac you might have to write `pip3`

-  we will also need another package for later so might as well install it now
```bash
pip install pytest-cov
```
- next you can look at this folder for code examples, but for now i'll put the basic code here as well if you want to follow step by step.
- In the `main.py` you will find the code you'll be testing, you don't necessary need to ever look at it, but it is a useful exercise to understand what the code does and what it is useful for. 
- the `test_main.py` will contain our testing functions
- pytest automagically considers any file that starts with `test_` is a testing file. So if you ever find yourself writing some tests you will have to put them in a file starting with test.
- to run our tests we can just type `pytest` in the terminal.
- although another way and maybe a better way to run tests is to use the testing functionality of vs code
    - to access it you can click on the beaker on the sidebar 
    - it will run similar to the debugger and it will help you run your tests and find any problems with them
    - let's give it a go

## an example
- let's say our team is working on a personal finance calculator and after gathering the requirements and completed all the other stages, we finally have a function developed and ready to test
- the function calculates the future value of an investment by calculating the compound interest over a period of time
- it takes the following inputs 
    - `principal`, a number bigger than 0 representing the initial investment but smaller than a billion
    - `rate`, a positive number that represent the expected interest rate over the period of time in percentage
    - `time`, a positive number that represents the length of the investment
- and produces the following outputs:
    - the total value of the investment plus the compounded interest after the time has elapsed
    - ValueError("Principal must be a positive number") if the principal is not a valid
    - - ValueError("Principal must be a less than a billion") if the principal is more than a billion
    - ValueError("Rate must be a positive number") if the rate is not a valid input
    - ValueError("TTime must be a positive number and at least one year") if the time is not a valid input
    - ValueError("Time must be less than 100 years") if the time in years is bigger than 100 years
- the function will look like this 
    ```python
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
    ```
- to start testing this function we need to create a `test_main.py` and write our test suite
- then we can inport the packages we need
    ```python
    import pytest
    import main
    ```
- then we need to write our test function
    ```python
    # we create a test function with the same parameters as the function we are testing 
    # plus we need  to add a parameter for the expected results
    def test_calculate_interest(principal, rate, time, expected):
        # we can then calculate the interest by calling the function from our main file
        actual_interest = main.calculate_interest(principal, rate, time)
        # then we use the special keyword assert to say we expect the result to be the same as the expected result from our test suite
        # we also use approx to avoid having test fail just on rounding errors
        assert pytest.approx(actual_interest, 0.01) == expected
    ```
- the next step is to write the test suite, to do that we can use a handy feature of `pytest` that allow us to parametrise our function and write it once and run it against all our test cases.
- this can save a lot of time.
- first thing first is to write down our test cases and of course we will derive our test cases doing BVA
- the formula to calculate compound interest is `Future Value=Principal×(1+Rate/100)^Time`
- just as a reminder we will need at least 5 values per input if we use a weak normal which implies a single fault assumption, and do the cartesian product
    | Test      | principal     | rate  | time  | expected result   |
    | :-----    | :------       | :---- |:----- | :---------        |
    | minP      |   0           | 2.5   | 10    | 0.0               |          
    | minPlusP  |   1           | 2.5   | 10    | 1.28              |
    | nomP      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusP |   999999999   | 2.5   | 10    | 1280084542.92     |
    | maxP      |   1000000000  | 2.5   | 10    | 1280084544.19     |
    | minR      |   5000        | 0     | 10    | 5000.0            |          
    | minPlusR  |   5000        | 0.1   | 10    | 5005.00           |
    | nomR      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusR |   5000        | 99    | 10    | 4869683.87        |
    | maxR      |   5000        | 100   | 10    | 5120000.0         | 
    | minT      |   5000        | 2.5   | 1     | 5125.0            |          
    | minPlusT  |   5000        | 2.5   | 2     | 5253.13           |
    | nomT      |   5000        | 2.5   | 10    | 6400.42           |
    | maxMinusT |   5000        | 2.5   | 99    | 57627.89          |
    | maxT      |   5000        | 2.5   | 100   | 59068.58          | 

- the next task is to convert this test suite into parameters for pytest
    ```python
    @pytest.mark.parametrize(
        "principal, rate, time, expected",
        [
            (0, 2.5, 10, 0.0),  # Test minP
            (1, 2.5, 10, 1.28),  # Test minPlusP
            (5000, 2.5, 10, 6400.42),  # Test nomP
            (999999999, 2.5, 10, 1280084542.92),  # Test maxMinusP
            (1000000000, 2.5, 10, 2748960625.44),  # Test maxP
            (5000, 0, 10, 5000.0),  # Test minR
            (5000, 0.1, 10, 5005.00),  # Test minPlusR
            (5000, 2.5, 10, 6400.42),  # Test nomR
            (5000, 99, 10, 4869683.87),  # Test maxMinusR
            (5000, 100, 10, 5120000.0),  # Test maxR
            (5000, 2.5, 1, 5125.0),  # Test minT
            (5000, 2.5, 2, 5253.13),  # Test minPlusT
            (5000, 2.5, 10, 6400.42),  # Test nomT
            (5000, 2.5, 99, 57627.89),  # Test maxMinusT
            (5000, 2.5, 100, 59068.58),  # Test maxT
        ],
    )
    ```

- now we can run the tests using pytest in the terminal or by running them in the testing section in vs code 
- hopefully they will all pass :)


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
    ```