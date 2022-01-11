import re
### match - метод шукає по заданому pattern на початку str. Якщо не знайдено метод поверне None
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
redot = re.search(r".", "abc")
print(redot)  #<re.Match object; span=(0, 2), match='a'>
print(re.search(r"a.b", "a+b"))  #<re.Match object; span=(0, 3), match='a+b'>
print(re.search(r"a.b", "ab"))  #None
print(re.search(r"a.b.c", "a-b=c"))  #<re.Match object; span=(0, 5), match='a-b=c'>
print(re.search(r"a.b.c", "a-bc"))  #None

### \d - означає одну любу цифру від 0 до 9

print(re.search(r"\d", "a1"))  #<re.Match object; span=(1, 2), match='1'>
print(re.search(r"\d\d", "11a"))  #<re.Match object; span=(0, 2), match='11'>
print(re.search(r"a\d", "a1"))  #<re.Match object; span=(0, 2), match='a1'>
print(re.search(r"a\d", "ab1"))  #None

### \s - пробіл, tab, \n
print(re.search(r"\s", " "))  #<re.Match object; span=(0, 1), match=' '>
print(re.search(r"\s", "1"))  #None

### \w - букви, цифри та _
print(re.search(r"\w", "sadfas"))  #<re.Match object; span=(0, 1), match='s'>
print(re.search(r"\w", "_"))  #<re.Match object; span=(0, 1), match='_'>

### \D - все що завгодно, але не \d(цифра)
print(re.search(r"\D", "@@"))  #<re.Match object; span=(0, 1), match='@'>
print(re.search(r"\D", "1"))  #None

### \S - любий непробельний символ
print(re.search(r"\S", "ава"))  #<re.Match object; span=(0, 1), match='а'>
print(re.search(r"\S", "\t"))  #None
print(re.search(r"\S", " "))  #None

###  \W - все окрім букв, цифр та підкр.
print(re.search(r"\S", "#"))  #<re.Match object; span=(0, 1), match='#'>
print(re.search(r"\W", "1"))  #None
print(re.search(r"\W", "_"))  #None
print(re.search(r"\W", "ю"))  #None
print(re.search(r"\W", "\n"))  #<re.Match object; span=(0, 1), match='\n'>

### ^ - початок рядка
print(re.search(r"^123", "123a"))  #<re.Match object; span=(0, 3), match='123'>
print(re.search(r"^123", "a123a"))  #None

### $ - кінець рядка
print(re.search(r"123$", "a123"))  #<re.Match object; span=(1, 4), match='123'>
print(re.search(r"123$", "a1223"))  #None

### [] - один любий символ із вказаних в скобках, або діапазон
print(re.search(r"[123]", "adfasfa1"))  #<re.Match object; span=(7, 8), match='1'>
print(re.search(r"[123]", "adfasfa123"))  #<re.Match object; span=(7, 8), match='1'>
print(re.search(r"[ ]", "adfasfa123"))  #None
print(re.search(r"[1-5]", "adfasfa193"))  #<re.Match object; span=(7, 8), match='1'>
print(re.search(r"[a-v]", "adfasfa193"))  #<re.Match object; span=(0, 1), match='a'>

### [^abc] - все окрім вказаного в скобках
print(re.search(r"[^abc]", "abba"))  #None
print(re.search(r"[^abc]", "dom"))  #<re.Match object; span=(0, 1), match='d'>

### {} - квантифікатор, кількість повторень; {,5} - кількість повторень від 0 до 5; {4,} - від 4 і більше
print(re.search(r"a{5}", "aaaaa"))  #<re.Match object; span=(0, 5), match='aaaaa'>
print(re.search(r"a{5}", "aaaa"))  #None
print(re.findall(r"\d{4}", "11, 2345, 334455"))  #['2345', '3344']


### * - символ перед * може повторюватися від 0 і більше раз
print(re.search(r"a\d*b", "a5555b"))  #<re.Match object; span=(0, 6), match='a5555b'>
print(re.search(r"a\d*b", "ab"))  #<re.Match object; span=(0, 2), match='ab'>

### + символ перед + може повторюватися 1 і більше разів
print(re.search(r"a\d+b", "a5555b"))  #<re.Match object; span=(0, 6), match='a5555b'>
print(re.search(r"a\d+b", "ab"))  #None

### ? символ перед ? може повторюватися 0 або 1 разів
print(re.search(r"a\d?b", "a5555b"))  #None
print(re.search(r"a\d?b", "ab"))  #<re.Match object; span=(0, 2), match='ab'>
print(re.search(r"a\d?b", "a5b"))  #<re.Match object; span=(0, 3), match='a5b'>

### \b - слово яке заключене між \b
print(re.search(r"\bIvan\b", "Privet Ivan"))  #<re.Match object; span=(7, 11), match='Ivan'>

### () - група символів
print(re.search(r"^4(a|b)", "4ab"))  #<re.Match object; span=(0, 2), match='4a'>
