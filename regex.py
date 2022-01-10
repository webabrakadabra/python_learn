import re
### matсh - метод шукає по заданому pattern на початку str. Якщо не знайдено метод поверне None
### r - row(сирий), це означаеє, що в pattern можно використовувати \. Також якщо перед str вказати r"Disk d:\notme.py"
### символ слеш можна не екранувати.
resmatch = re.match(r'Python', 'Python11111 is good')
print(resmatch)  #<re.Match object; span=(0, 6), match='Python'>


### search - метод, який на відміну від match шукає по всьому рядку перше співпадіння з pattern.
### Якщо не знайдено метод поверне None
ressearch = re.search(r"Python", "Me is Python")
print(ressearch)  #<re.Match object; span=(6, 12), match='Python'>


### findall - шукає всі співпадіння в str по вказаному pattern
resfindall = re.findall(r"Python", "My Python is bis Python")
print(resfindall)  #['Python', 'Python']


### split - розділи str по вказаному pattern
ressplit = re.split(r"y", "Analysis")
print(ressplit)  #['Anal', 'sis']


### sub - метод шукає pattern в str та замінює його на substr
ressub = re.sub(r"India", "Ukraine", "India is a big country")
print(ressub)  #Ukraine is a big country


### .  - крапка означає один любий символ
redot = re.search(".", "abc")
print(redot)  #<re.Match object; span=(0, 2), match='a'>
print(re.search("a.b", "a+b"))  #<re.Match object; span=(0, 3), match='a+b'>
print(re.search("a.b", "ab"))  #None
print(re.search("a.b.c", "a-b=c"))  #<re.Match object; span=(0, 5), match='a-b=c'>
print(re.search("a.b.c", "a-bc"))  #None

### \d - означає одну любу цифру від 0 до 9

print(re.search("\d", "a1"))  #<re.Match object; span=(1, 2), match='1'>
print(re.search("\d\d", "11a"))  #<re.Match object; span=(0, 2), match='11'>
print(re.search("a\d", "a1"))  #<re.Match object; span=(0, 2), match='a1'>
print(re.search("a\d", "ab1"))  #None

### \s - пробіл, tab, \n
print(re.search("\s", " "))  #<re.Match object; span=(0, 1), match=' '>
print(re.search("\s", "1"))  #None

### \w - букви та _
print(re.search("\w", "sadfas"))  #<re.Match object; span=(0, 1), match='s'>
print(re.search("\w", "_")  #<re.Match object; span=(0, 1), match='_'>

### \D - все що завгодно, але не \d(цифра)
print(re.search("\D", "@@"))  #<re.Match object; span=(0, 1), match='@'>
print(re.search("\D", "1"))  #None

### \S - любий непробельний символ
print(re.search("\S","ава"))  #<re.Match object; span=(0, 1), match='а'>
print(re.search("\S","\t"))  #None
print(re.search("\S"," "))  #None

###  \W - все окрім букв, цифр та підкр.
print(re.search("\S","#"))  #<re.Match object; span=(0, 1), match='#'>
print(re.search("\W","1"))  #None
print(re.search("\W","_"))  #None
print(re.search("\W","ю"))  #None
print(re.search("\W","\n"))  #<re.Match object; span=(0, 1), match='\n'>


