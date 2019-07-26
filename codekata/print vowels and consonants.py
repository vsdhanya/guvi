given_alpha=input()
vowels=['a','A','e','E','i','I','o','O','u','U']
consonants=['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z']
for i in given_alpha:
  if i in vowels:
    print(i,end="")
for i in given_alpha:
  if i in consonants:
    print(i,end="")
