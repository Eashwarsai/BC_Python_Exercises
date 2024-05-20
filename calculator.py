from functools import wraps

# Decorator for logging
def log_result(func):
    """
    Decorator function for logging the result of the calculation.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that calls the decorated function and logs the result.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            Any: Result of the decorated function.
        """
        result = func(*args, **kwargs)
        print(f"Result of calculation is {result}")
        return result
    return wrapper

# Decorator for retry
def retry(max_retries):
    """
    Decorator factory function for retrying a function multiple times.

    Args:
        max_retries (int): Maximum number of retry attempts.

    Returns:
        function: Decorator function for retrying.
    """
    def decorator_retry(func):
        """
        Decorator function for retrying a function.

        Args:
            func (function): The function to be decorated.

        Returns:
            function: The decorated function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that retries the decorated function multiple times.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                Any: Result of the decorated function.

            Raises:
                ValueError: If maximum retry attempts exceeded.
            """
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    print(f"Retry attempt {attempts + 1}")
                    attempts += 1
            else:
                raise ValueError("Max retry attempts exceeded")
        return wrapper
    return decorator_retry

@log_result
@retry(max_retries=3)
def calculate():
    """
    Function to perform a calculation based on user input.

    Returns:
        float: Result of the calculation.

    Raises:
        ValueError: If invalid operator or division by zero occurs, or if operands are not numeric.
    """
    operand1 = float(input("Enter the first operand: "))
    operator = input("Enter the operator (+, -, *, /): ")
    operand2 = float(input("Enter the second operand: "))
    
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator")
    
    if operator == '/' and operand2 == 0:
        raise ValueError("Division by zero is not allowed")
    
    if not (isinstance(operand1, (int, float)) and isinstance(operand2, (int, float))):
        raise ValueError("Operands must be numeric")
    
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Test the calculator function
try:
    calculate()
except Exception as e:
    print(e)
