Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''what is string?'''
'what is string?'

'''what is string?'''
'what is string?'
'''    '''
'    '

'''string is collection of characters and it return sequence of ordered. '''
'string is collection of characters and it return sequence of ordered. '
#string is umutable
s='python'
s
'python'
id(s)
2381879688336
s='programming'
s
'programming'
id(s)
2381924251184
a = 'shadow'
b ='master'
id(a)
2381924138368
id(b)
2381884035824
c = a+b
c
'shadowmaster'
id(c)
2381880079408
id(a+b)
2381923893424
c
'shadowmaster'
#repeation
s=a*3
s
'shadowshadowshadow'
#indexing
s[2]
'a'
#slicing
k = 'The hacker want hacking systems but not truth.They want rule the world.'
k[::1]
'The hacker want hacking systems but not truth.They want rule the world.'
k[::-1]
'.dlrow eht elur tnaw yehT.hturt ton tub smetsys gnikcah tnaw rekcah ehT'
#membership :
filpkart = ['bags','belts','shoes','toys']
filpkart
['bags', 'belts', 'shoes', 'toys']
belts in filpkart
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    belts in filpkart
NameError: name 'belts' is not defined
filpkart = 'bags belts shoes toys'
belts in filpkart
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    belts in filpkart
NameError: name 'belts' is not defined
'belts' in filpkart
True
'gloves' in flipkart
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    'gloves' in flipkart
NameError: name 'flipkart' is not defined. Did you mean: 'filpkart'?
'gloves' in filpkart
False
'gloves' not in filpkart
True
# min max
c
'shadowmaster'
min(c)
'a'
max(a)
'w'
c
'shadowmaster'
sorted(c)
['a', 'a', 'd', 'e', 'h', 'm', 'o', 'r', 's', 's', 't', 'w']
c
'shadowmaster'
c.upper()
'SHADOWMASTER'
c.lower()
'shadowmaster'
a = 'MASTER Shadow'
a.swapcase()
'master sHADOW'
a = giri prasad
SyntaxError: invalid syntax
a = 'giri prasad'
a.title()
'Giri Prasad'
a = 'iam the webdevwlopwr  khfkjshfkshfkhs'
a.capitalize()
'Iam the webdevwlopwr  khfkjshfkshfkhs'
a = 'MASTER Shadow'
a
'MASTER Shadow'
a.center(5,"")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.center(5,"")
TypeError: The fill character must be exactly one character long
a.center(5," ")
'MASTER Shadow'
a.center(5,"_")
'MASTER Shadow'
a.center(5, "_")
'MASTER Shadow'
a.center(5, "-")
'MASTER Shadow'
a.center(5)
'MASTER Shadow'
a = 'giri prasad'
a
'giri prasad'
a.center(5)
'giri prasad'
a.center(9)
'giri prasad'
a.ljust(9,'*')
'giri prasad'
a
'giri prasad'
b = 125
b.zfill(5)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b.zfill(5)
AttributeError: 'int' object has no attribute 'zfill'
b = '125'
b.zfill(5)
'00125'
a.rjust(5,"*")
'giri prasad'
product = "Bag"
product.ljust(8, "-")
'Bag-----'
f = 'banana'
f.ljust(5, "*")
'banana'
f = "banana"
f
'banana'
f.ljust(8, "-")
'banana--'
f.ljust(5, "-")
'banana'
f.ljust(10, "-")
'banana----'
f.rjust(10, "_")
'____banana'
text = 'the master bruce wayne is a Batman. Batman is a not bruce wayne.'
text
'the master bruce wayne is a Batman. Batman is a not bruce wayne.'
text.find('b')
11
text.find('bruce')
11
text.find('in')
-1
text.rfind('b')
52
text.index('b')
11
text.index('z')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.index('in')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    text.index('in')
ValueError: substring not found
>>> text.rindex('b')
52
>>> text.count('b')
2
>>> text.count('Batman')
2
>>> text.count('the')
1
>>> 
>>> 
>>> 
>>> text='  hello  '
>>> text.strip()
'hello'
>>> text.strip('l')
'  hello  '
>>> text1 = '   hello world      '
>>> text1.strip('world')
'   hello world      '
>>> text.strip().strip('l')
'hello'
>>> text.strip().strip('o')
'hell'
>>> text1.strip().strip('world')
'hello '
>>> text2 ='world hello world'
>>> text2.strip('world')
' hello '
>>> text.rstrip()
'  hello'
>>> text.lstrip()
'hello  '
>>> text = 'master'
>>> text.replace(a,*)
SyntaxError: invalid syntax
>>> text.replace('a','*')
'm*ster'
>>> text1 = 'jackjones'
>>> text.replace('j','$',1)
'master'
>>> text1.replace('j','$',1)
'$ackjones'
>>> text1.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> text1.translate(text1.maketrans('aeiou','12345'))
'j1ckj4n2s'
