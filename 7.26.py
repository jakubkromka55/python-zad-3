def f(text):
    return "-".join(text)

# Testy
print(f("Univesity"))  # Oczekiwany wynik: "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))         # Oczekiwany wynik: "U-E"
print(f("x"))          # Oczekiwany wynik: "x"
print(f(""))           # Oczekiwany wynik: ""
