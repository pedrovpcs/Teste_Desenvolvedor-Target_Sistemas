string = "Hello, world!"  # string a ser invertida
string_invertida = ""  # string invertida, inicialmente vazia

# Percorre a string da última posição até a primeira
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[
        i
    ]  # adiciona o caractere atual ao início da string invertida

print(string_invertida)  # imprime a string invertida
