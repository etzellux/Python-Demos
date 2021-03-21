# -*- coding: utf-8 -*-

### REGEX ###

# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

import re
string = "359-678-123 334.123.753"

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d\d\d')

matches = pattern.finditer(string)

for match in matches:
    print(match)

#%%

text = """Ad Soyad: Atilla Bora Semerci
            Ad Soyad: Mehmet Yıldırım"""
            
pattern = re.compile(r'\bAd Soyad: \w* \w*')

matches = pattern.finditer(text)

for match in matches:
    print(match)
    
#%%

text = """https://www.google.com
http://youtube.com
https://facebook.com"""
            
pattern = re.compile(r'https?:/+(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3',text)
print(subbed_urls)