def f(detector):
    people_in_room = 0  # Zmienna śledząca liczbę osób w pokoju
    
    for action in detector:
        if action == '+':
            people_in_room += 1
        elif action == '-':
            people_in_room -= 1
        
        # Sprawdzamy, czy w pokoju jest co najmniej 3 osoby
        if people_in_room >= 3:
            return True
    
    return False

# Testowanie funkcji
print(f("+-+++-+---"))  # Oczekiwany wynik: True
print(f("+-+-+-+-"))    # Oczekiwany wynik: False
print(f("+-++-+--"))    # Oczekiwany wynik: False
print(f("+-++-++-+---")) # Oczekiwany wynik: True
