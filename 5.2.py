# Funkcja konwertująca metry na centymetry
def m_to_cm(n):
    return n * 100

# Funkcja konwertująca centymetry na metry
def cm_to_m(n):
    return n / 100

# Funkcja konwertująca centymetry na cale
def cm_to_inch(n):
    return n / 2.54

# Funkcja konwertująca stopy i cale na centymetry
def ft_and_inch_to_cm(feet, inches):
    return (feet * 30.48) + (inches * 2.54)

# Testowanie funkcji w tym pliku
if __name__ == "__main__":
    # Testowanie funkcji
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    
    # Nowe testy
    cm_value = 100
    print(f'{cm_value} cm = {cm_to_inch(cm_value)} inches')
    
    feet = 5
    inches = 8
    print(f'{feet} feet and {inches} inches = {ft_and_inch_to_cm(feet, inches)} cm')
