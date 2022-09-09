def compare(firstNumber: float, secondNumber : float) -> str:
    """Compare two numbers.

    Args:
        firstNumber (float): The first number.
        secondNumber (float): The second number.

    Returns:
        str: A string which compare twos input numbers.
    """
    if firstNumber < secondNumber:
        return f"{firstNumber} is less than {secondNumber}"
    elif firstNumber == secondNumber:
        return f"{firstNumber} is equal to {secondNumber}"
    else:
        return f"{firstNumber} is greater than {secondNumber}"
    
if __name__ == '__main__':
    print(compare(1, 2.2))  # 1 is less than 2.2
    print(compare.__doc__)
    # Compare two numbers.

    #     Args:
    #         firstNumber (float): The first number.
    #         secondNumber (float): The second number.

    #     Returns:
    #         str: A string which compare twos input numbers.