# Funkcja obliczająca ocenę końcową na podstawie liczby punktów
def pts_to_grade(points):
    grade = ''
    
    # Sprawdzamy liczbę punktów i przypisujemy odpowiednią ocenę
    if points >= 18:
        grade = 'Bardzo dobry'
    elif points >= 14:
        grade = 'Dobry'
    elif points >= 10:
        grade = 'Dostateczny'
    else:
        grade = 'Niedostateczny'
    
    return grade

# Przykładowy wynik testu
test_result = 15

# Obliczenie oceny końcowej
final_grade = pts_to_grade(test_result)

# Wypisanie wyniku
print(f'Uzyskałeś {test_result} punkty na teście. Twoja ocena końcowa to {final_grade}.')
