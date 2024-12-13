# Funkcja zwracająca pełną nazwę dnia tygodnia na podstawie numeru dnia
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        result = 'Invalid day number'  # Obsługuje przypadek, gdy numer dnia jest poza zakresem
    
    return result

# Użycie funkcji
print('The name of day 5 in the week is', day_name(5))  # Friday
print('The name of day 3 in the week is', day_name(3))  # Wednesday
print('The name of day 7 in the week is', day_name(7))  # Sunday
