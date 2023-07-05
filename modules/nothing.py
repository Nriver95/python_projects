Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
4+5
9
x=4
x+5
9

================================ RESTART: Shell ================================
F= 'nick'
L= 'Rivera'
print('hello {} {}, welcome to python!'.format(F,L) )
hello nick Rivera, welcome to python!
a='Hello, World!'
print(a[1])
e
for x in 'banana':
    print(x)
    ;
    
SyntaxError: incomplete input
for x in 'banana':
    print(x);

    
b
a
n
a
n
a
print(len(a))
13
print("a" in a)
False
print('a' in x)
True
print(upper(x))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(upper(x))
NameError: name 'upper' is not defined. Did you mean: 'super'?
print(x.upper())
A
x
'a'
x=banana
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=banana
NameError: name 'banana' is not defined
x='banana'
print(x.upper())
BANANA
print(x[:3])
ban
b = "Hello, World!"
print(b[-5:-2])
SyntaxError: multiple statements found while compiling a single statement
b = "Hello, World!"
print(b[-5:-2])
orl
myString = "Hi I'm Paul"
newString = list(myString)
print(newString)
['H', 'i', ' ', 'I', "'", 'm', ' ', 'P', 'a', 'u', 'l']

==================================================================================================================== RESTART: Shell ====================================================================================================================
x = 'America'
for i in x:
    print(i)

    
A
m
e
r
i
c
a
x.append('!')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x.append('!')
AttributeError: 'str' object has no attribute 'append'
y = [1,2,3,4,5,6,7,8]
y.append(9)
for i in y:
    print(i)

    
1
2
3
4
5
6
7
8
9
>>> y = list.copy()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    y = list.copy()
TypeError: unbound method list.copy() needs an argument
>>> list = y.copy()
>>> y+list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> reverse(list)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    reverse(list)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> list.reverse()
>>> print(y+list)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> thisSet = ['bulbasaur', 'squirtle', 'charmander']
>>> thisSet.add('pikachu')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    thisSet.add('pikachu')
AttributeError: 'list' object has no attribute 'add'
>>> starter = {'bulbasuar', 'squirtle', 'charmander'}
>>> starter.add('pikachu')
>>> starter
{'squirtle', 'bulbasuar', 'pikachu', 'charmander'}
>>> team = {'pikachu', 'Blastoise', 'Tyranitar', 'Dragonite'}
>>> squad = starter.difference(team)
>>> print(squad)
{'squirtle', 'bulbasuar', 'charmander'}
>>> help> modules
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    help> modules
NameError: name 'modules' is not defined
>>> help>
SyntaxError: incomplete input
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(modules)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    help(modules)
NameError: name 'modules' is not defined
>>> help(module)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    help(module)
NameError: name 'module' is not defined
>>> modules
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    modules
NameError: name 'modules' is not defined
>>> 
==================================================================================================================== RESTART: Shell ====================================================================================================================
>>> import mfm
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    import mfm
ModuleNotFoundError: No module named 'mfm'
