import random
import os
import asyncio

numSorteado = random.randint(0, 100)
numPlayer = 101
tentativas = 0


async def loop():
    global tentativas
    global numSorteado
    global numPlayer

    while numPlayer != numSorteado:
        os.system('cls')

        numPlayer = int(input('Qual numero foi sorteado? '))

        if numPlayer > numSorteado:
            print('erro: o numero digitado é maior que o numero sorteado.')
            print('tente novamente.')
            tentativas += 1
        elif numPlayer < numSorteado:
            print('erro: o numero digitado é menor que o numero sorteado.')
            print('tente novamente.')
            tentativas += 1

        await asyncio.sleep(4)

asyncio.run(loop())

print('bingo!! resposta correta, o valor era {}'.format(numPlayer))
print('tentativas: {}'.format(tentativas))
