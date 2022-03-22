# Programa para dizer se a letra que o usuário digitou é uma vogal ou não

vogal = input('Digite uma letra: ')

if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u' or \
        vogal == 'A' or vogal == 'E' or vogal == 'I' or vogal == 'O' or vogal == 'U':
    print("Você digitou uma vogal: " + vogal)
else:
    print("Você digitou uma Consoante: " + vogal)
