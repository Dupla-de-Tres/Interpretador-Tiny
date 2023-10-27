# Enumeração de todos os tipos de tokens

from enum import Enum

TipoToken = Enum(
  'TipoToken', [
  # Caracteres Especiais
  'UNEXPECTED_EOF',
  'INVALID_TOKEN',
  'END_OF_FILE',

  # Símbolos
  'SEMICOLON',     # ;
  'ASSIGN',        # =

  # Operadores lógicos
  'EQUAL',         # ==
  'NOT_EQUAL',     # !=
  'LOWER',         # <
  'LOWER_EQUAL',   # <=
  'GREATER',       # >
  'GREATER_EQUAL', # >=

  # Operandos aritméticos
  'ADD',           # +
  'SUB',           # -
  'MUL',           # *
  'DIV',           # /
  'MOD',           # %

  # Palavras-Chave
  'PROGRAM',       # program
  'WHILE',         # while
  'DO',            # do
  'DONE',          # done
  'IF',            # if
  'THEN',          # then
  'ELSE',          # else
  'OUTPUT',        # output
  'TRUE',          # true
  'FALSE',         # false
  'READ',          # read
  'NOT',           # not

  # Outros
  'NUMBER',        # number
  'VAR'            # variable
])       