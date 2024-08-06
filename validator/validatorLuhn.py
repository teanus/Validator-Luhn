def validate(card: str) -> bool:
    """
    Validate a credit card number using the Luhn algorithm.

    Args:
        card (str): The credit card number as a string, which may contain spaces.

    Returns:
        bool: True if the card number is valid according to the Luhn algorithm, False otherwise.
    """

    # Remove any spaces from the card number and convert each digit to an integer
    numbers: list[int] = [int(i) for i in card.replace(" ", "")]
    elements_sum: int = 0

    # Iterate through the digits in the card number
    for index, number in enumerate(numbers):
        # Double every second digit from the right (Luhn algorithm step)
        if not index % 2:
            doubled = number * 2
            # If doubling the number results in a number greater than 9, subtract 9 from it
            elements_sum += doubled if doubled < 10 else doubled - 9
        else:
            elements_sum += number

    # The card number is valid if the sum of the digits is a multiple of 10
    return elements_sum % 10 == 0
