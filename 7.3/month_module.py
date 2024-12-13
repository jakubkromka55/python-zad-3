# Funkcja month(n) zwraca nazwę miesiąca na podstawie numeru miesiąca
def month(n):
    # Lista nazw miesięcy, indeksowane od 0 do 11
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    # Sprawdzamy, czy numer miesiąca jest poprawny (od 1 do 12)
    if 1 <= n <= 12:
        return months[n - 1]  # Zwracamy nazwę miesiąca (indeks zaczyna się od 0)
    else:
        return "Invalid month number"  # Zwracamy komunikat, jeśli numer miesiąca jest poza zakresem
