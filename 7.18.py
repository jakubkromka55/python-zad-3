def f(sentence):
    # Usunięcie wszystkich spacji w zdaniu
    return sentence.replace(" ", "")

# Testowanie funkcji
print(f("integrated development environment"))  
# Oczekiwany wynik: "integrateddevelopmentenvironment"

print(f("A programming language is a system of notation for writing computer programs"))  
# Oczekiwany wynik: "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
