# Higher order function (returns a fucntion type 2)
def translator(language):
  translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
  def translate_word(word):
    if word.lower() in translations[language]:
      return translations[language][word.lower()]
    else:
      return "Translation not available"
  
  return translate_word

translate = translator('spanish')
print(translate('hello'))

# Higher order function (pass a fucntion as an argument type 1)
def loud(number):
  a = 5
  return number ** a

def quiet(number):
  b = 2
  return number ** b

def math(lol):
    num = lol(3)
    print(num)

math(loud)
math(quiet)

