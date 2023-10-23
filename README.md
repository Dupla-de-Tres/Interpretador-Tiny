# Interpretador-Tiny

<h2>Introdução</h2>

O objetivo deste projeto é desenvolver um interpretador para a linguagem Tiny, uma linguagem de programação com sintaxe e semântica simples. Este trabalho acadêmico foi proposto pelos professores Andrei Rimsa e Diego Ascanio, do CEFET/MG. Ele foi desenvolvido em Python, utilizando orientação a objetos, com o objetivo de compreender os princípios fundamentais de interpretação de linguagens de programação. O projeto contém a implementação de um interpretador para a linguagem Tiny. Essa linguagem é simples e é utilizada para exercitar os conceitos necessários para a disciplina de linguagens de programação do CEFET/MG. A implementação pode ser usada como referência para o desenvolvimento do primeiro trabalho prático dessa disciplina.

<h2>Implementação da Linguagem</h2>

Tiny é uma linguagem de programação simples, interpretada, que é usada para aprender os conceitos básicos de programação.

``` Comandos: ```

<p>A linguagem possui quatro tipos de comandos:</p>

- Comando condicional (if): testa uma condição e executa um bloco de comandos se a condição for verdadeira.
- Comando de repetição (while): executa um bloco de comandos enquanto uma condição for verdadeira.
- Comando de atribuição (id = expr): atribui o valor da expressão à variável id.
- Comando de saída (output expr): imprime o valor da expressão na saída padrão.

``` Blocos de comandos: ```

Os comandos podem ser combinados para formar blocos de comandos. Um programa em Tiny começa com a palavra-chave program seguida de um bloco de comandos.

``` Identificadores: ```

Os identificadores (variáveis) começam com uma letra ou sublinhado () e podem ser seguidos de letras, dígitos e sublinhados (). Os identificadores em Tiny armazenam apenas números inteiros.

``` Expressões lógicas: ```

A linguagem permite a avaliação de expressões lógicas simples em comandos condicionais e de repetição.

As expressões lógicas suportadas são:

- Igual (==): testa se duas expressões têm o mesmo valor.
- Diferente (!=): testa se duas expressões não têm o mesmo valor.
- Menor (<): testa se uma expressão é menor que outra.
- Maior (>): testa se uma expressão é maior que outra.
- Menor igual (<=): testa se uma expressão é menor ou igual que outra.
- Maior igual (>=): testa se uma expressão é maior ou igual que outra.

``` Expressões aritméticas: ```

A linguagem suporta constantes numéricas inteiras e a leitura de um valor numérico inteiro do teclado (read).

As expressões aritméticas suportadas são:

- Adição (+): soma duas expressões.
- Subtração (-): subtrai duas expressões.
- Multiplicação (*): multiplica duas expressões.
- Divisão (/): divide duas expressões.
- Resto da divisão (%): calcula o resto da divisão de duas expressões.

A linguagem possui comentários de uma linha a partir do símbolo #.


<h2>Execução</h2>

Para executar o programa, é necessário inserir os seguintes comandos:

- ``` cd Tiny ```
- ``` python3 main.py ```

Exemplo de saída utilizando somatorio.tiny:

4
8
15
16
23
42
0
108

Vale ressaltar que, para executar cada exemplo, é necessário mudar o nome do arquivo de exemplo na variável("name"), contida dentro do arquivo main.py.

Por fim, a linguagem Tiny mostrou-se eficiente para a implementação de um interpretador. O interpretador é capaz de interpretar programas Tiny simples e complexos de forma rápida e precisa.

<h2>Referências</h2>

<p>(1) ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: interpretador Tiny Incompleto - Disponível em: https://github.com/DiegoAscanio/interpretador-tiny-incompleto. Acessado em 20 de Outubro de 2023.</p>

<p>(2) ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: Analizador Lexico Exemplo - Disponível em: https://github.com/DiegoAscanio/analisador-lexico-exemplo. Acessado em 20 de Outubro de 2023.</p>

<p>(3) RIMSA, ANDREI - Repositório GitHub, @rimsa: tiny - Disponível em: https://github.com/rimsa/tiny. Acessado em 20 de Outubro de 2023.</p>


