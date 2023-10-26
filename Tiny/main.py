# Para testar o programa, é necessario mudar o nome do arquivo contido na variável name,
# podendo ser, por exemplo, Exemplos/if.tiny

from Analisadores.Parser import Parser

def main ():
    Int = Parser()
    name = 'Exemplos/if.tiny'
    Executar = Int.inicio(name)
    Executar.executar()

main()