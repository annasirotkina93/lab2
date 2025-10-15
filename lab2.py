import csv, random
import xml.etree.ElementTree as ET

#csv read
with open('books.csv', encoding='cp1251') as f:
    rows = list(csv.DictReader(f, delimiter=';'))

title_key = 'Название'
author_key = 'Автор'
price_key = 'Цена поступления'
data_key = 'Дата поступления'

#задание 1
count = sum(len(r[title_key]) > 30 for r in rows)
print("Ответ 1:", count)

#задание 2
author = input("Автор: ")
filtered = []
for r in rows:
    try:
        price = int(r[price_key].split('.')[-1].split()[0])
        if author in r[author_key] and price <= 200:
            filtered.append(r)
    except:
        pass

print('Ответ 2:', len(filtered))
for r in filtered[:3]:
    print(r[author_key], r[title_key], r[price_key])


#задание 3
bibs = random.sample(rows, 20)
with open('bibliography.txt', 'w', encoding='utf-8') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[author_key]}. {b[title_key]} - {b[data_key]}\n")

# xml
tree = ET.parse('currency.xml')
root = tree.getroot()
currency_dict = {}

for valute in root.findall('Valute'):
    num_code = valute.find('NumCode').text
    char_code = valute.find('CharCode').text
    currency_dict[num_code] = char_code
print(currency_dict)