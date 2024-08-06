# Credit Card Validator

This Python module provides a function to validate credit card numbers using the Luhn algorithm.

## Installation

No installation is required. Simply copy the `validator.py` file into your project.

## Usage

Import the `validate` function from the module and use it to check if a credit card number is valid.

### Example

```python
from validator import validate

# Example credit card numbers
card_number1 = "4539 1488 0343 6467"  # Valid Visa card number
card_number2 = "8273 1232 7352 0569"  # Invalid card number

# Validate the card numbers
is_valid1 = validate(card_number1)
is_valid2 = validate(card_number2)

print(f"Card number {card_number1} is valid: {is_valid1}")
print(f"Card number {card_number2} is valid: {is_valid2}")
