import unicodedata

def remover_acentos(texto):
    # Decompor os caracteres acentuados em caracteres base e marcas de acento
    texto = unicodedata.normalize('NFD', texto)
    # Filtrar e remover os caracteres de marca de acento
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def contar_letra_a(string):
    # Normaliza a string para remover acentos
    string = remover_acentos(string).lower()
    
    # Conta o número de ocorrências da letra 'a'
    quantidade_a = string.count('a')
    
    # Verifica se a letra 'a' foi encontrada
    if quantidade_a > 0:
        print(f"A letra 'a' (ou 'A') aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' (ou 'A') não aparece na string.")

# Exemplo de uso
entrada = input("Digite uma string: ")
contar_letra_a(entrada)
