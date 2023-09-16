from validatorLuhn import validate

print(validate("2200 8373 8276 4455"))  # Указан неверный номер карты, вернет False
print(validate("4276 8070 1492 79 48"))  # Указан верный номер карты, вернет True

