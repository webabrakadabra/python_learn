import re

# matсh - метод шукає по заданому pattern на початку str. Якщо не знайдено метод поверне None
# r - row(сирий), це означаеє, що в pattern можно використовувати \. Також якщо перед str вказати r"Disk d:\notme.py"
# символ слеш можна не екранувати.

resmatch = re.match(r'Python', 'Python11111 is good')
print(resmatch)

# search - метод, який на відміну від mathc шукає по всьому рядку. Якщо не знайдено метод поверне None

ressearch = re.search(r"Python", "Me is Python")
print(ressearch)