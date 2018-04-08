# substitution cypher
cipherString = 'qwertyuiopasdfghjklzxcvbnm'
cipherUpper = cipherString.upper()
alphaString = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = alphaString.upper()


def encrypt(inputString):
  newString = ''
  for ch in inputString:

      if ch in alphaString:

        oldCh = alphaString.index(ch)

        newCh = cipherString[oldCh]

        newString += newCh

      elif ch in alphaUpper:

        oldCh = alphaUpper.index(ch)

        newCh = cipherUpper[oldCh]

        newString += newCh

      elif ch not in alphaString:

        newString += ' '

  return newString

print(encrypt('Know your enemy'))
