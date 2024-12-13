# Importowanie funkcji month z modułu month_module
from month_module import month

# Pobieranie numeru miesiąca od użytkownika
month_number = int(input("Enter month number: "))

# Wywołanie funkcji month() i wydrukowanie wyniku
month_name = month(month_number)
print(f"The name of month {month_number} is {month_name}")
