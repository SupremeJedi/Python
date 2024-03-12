import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ha HaHa

MetaCharecters(Need to be escaped) :
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr. Smith
Ms. David
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to  an end'

pattern = re.compile(r'coreyms\.com')# use '\' for searching ny special charecters. for eg . coreyms.com = coreyms\.com

  #___\A-	Matches if the string begins with the given character
  #___\b-	Matches if the word begins or ends with the given character. 
  #___\B-	It is the opposite of the \b i.e. the string should not start or end with the given regex.
  #___\d-	Matches any decimal digit, this is equivalent to the set class
  #___\D-	Matches any non-digit character, this is equivalent to the set class 
  #___\s-	Matches any whitespace character.	
  #___\S-	Matches any non-whitespace character
  #___\w-	Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_]
  #___\W-	Matches any non-alphanumeric character.	\W	>$
  #___\Z-	Matches if the string ends with the given regex


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

d = text_to_search(131,142)
print(d)