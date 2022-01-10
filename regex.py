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
