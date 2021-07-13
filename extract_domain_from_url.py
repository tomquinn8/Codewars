#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

import re

def domain_name(url):
    return re.findall('(?:https?://|www\.)*([\w-]*).*$', url)[0]

print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
print(domain_name("https://www.youtube.com"), "youtube")
print(domain_name("xakep.ru"), "xakep")
print(domain_name("https://www.you-tube.com"), "you-tube")
