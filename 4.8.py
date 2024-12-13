def time_string(hours, minutes, time_format):
    # Jeśli format to 24-godzinny
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    
    # Jeśli format to 12-godzinny
    elif time_format == '12':
        # Określamy am/pm
        if hours == 0:
            return f"12:{minutes:02}am"
        elif hours == 12:
            return f"12:{minutes:02}pm"
        elif hours > 12:
            return f"{hours - 12}:{minutes:02}pm"
        else:
            return f"{hours}:{minutes:02}am"
    else:
        return "Invalid time format"

# Przykłady użycia funkcji
print(time_string(15, 38, '24'))  # '15:38'
print(time_string(8, 3, '24'))    # '08:03'
print(time_string(0, 5, '24'))    # '00:05'
print(time_string(11, 15, '12'))  # '11:15am'
print(time_string(0, 7, '12'))    # '12:07am'
print(time_string(7, 30, '12'))   # '7:30am'
print(time_string(12, 46, '12'))  # '12:46pm'
print(time_string(13, 10, '12'))  # '1:10pm'
print(time_string(19, 2, '12'))   # '7:02pm'
