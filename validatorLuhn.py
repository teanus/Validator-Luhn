def validate(card) -> bool:
    numbers = [int(i) for i in card.replace(" ", "")]
    elements_sum = 0

    for index, number in enumerate(numbers):
        if not index % 2:
            elements_sum += number * 2 if (number * 2) < 10 else (number * 2) - 9
        else:
            elements_sum += number

    return elements_sum % 10 == 0
