def encrypt(inputString):

  cipherString = 'qwertyuiopasdfghjklzxcvbnm'
  cipherUpper = cipherString.upper()
  alphaString = 'abcdefghijklmnopqrstuvwxyz'
  alphaUpper = alphaString.upper()
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

# RESULT
# Afgv ngxk tftdn

def decrypt(inputString):

  cipherString = 'qwertyuiopasdfghjklzxcvbnm'
  cipherUpper = cipherString.upper()
  alphaString = 'abcdefghijklmnopqrstuvwxyz'
  alphaUpper = alphaString.upper()
  newString = ''

  for ch in inputString:

      if ch in cipherString:

        oldCh = cipherString.index(ch)

        newCh = alphaString[oldCh]

        newString += newCh

      elif ch in cipherUpper:

        oldCh = cipherUpper.index(ch)

        newCh = alphaUpper[oldCh]

        newString += newCh

      elif ch not in cipherString:

        newString += ' '

  return newString

print(decrypt('Afgv ngxk tftdn'))
