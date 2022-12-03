import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMANOPQRSTUVWXYZ
1234567

Ha Haha

meta characters(needs to be skiped)
. ^ $ * + ? { } [ ] \ \ ( )

coeryms.com

321-555-4321
123.555.1234

Mr.Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'abc')
# # finditer gives object which contain all the matches and index span for the match
# #matches = pattern.finditer(test_to_search)
# for match in matches:
#     print(match)
# # find all gives list of all matching text
# #x = pattern.findall(test_to_search)
# print(x)

#match phone numbers
# pattern = re.compile('\d{3}[-.*]\d{3}[-.*]\d{4}')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#      print(match)

#match all the name with Mr
# pattern = re.compile('Mr\.?\s?[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#       print(match)

#match all the name with the name
# pattern = re.compile(r'M(r|s|rs)\.?\s?[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#       print(match)


# email = '''
# CoreyMschafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# '''
# pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern.finditer(email)
# for match in matches:
#     print(match)


urls = '''
https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?[a-zA-Z]+\.(com|gov)')
matches = pattern.finditer(urls)
for match in matches:
     print(match)