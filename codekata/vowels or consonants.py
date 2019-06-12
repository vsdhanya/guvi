given_alpha=input()
vowels=['a','A','e','E','i','I','o','O','u','U']
consonants=['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z']
if given_alpha in vowels:
  print("Vowel")
elif given_alpha in consonants:
  print("Consonant")
else:
  print("invalid")
