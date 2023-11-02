palavra = "emma"

#variavel de contagem 
letras_usuario = []

#variavel de chances
chances = 6

#o usuario "começa perdendo" por isso o "false"
ganhou = False

#usamos o while para um looping infinito, fechamos ele com o break 
while True:

    # criar a nossa logica

    for letra in palavra:

        #lower.() é paara letras minusculas

        if letra.lower() in letras_usuario:

            print(letra, end=" ")

        else:

            print("_", end=" ")

    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")

    #usamos o "append para adicionar caaracteres e coisas a alguma outra coisa"
    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():

        chances -= 1

    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras_usuario:

            ganhou = False

    if chances == 0 or ganhou:

        break

if ganhou:

    print(f"Parabéns, você ganhou. A palavra era: {palavra}")

else:

    print(f"Você perdeu! A palavra era: {palavra}")