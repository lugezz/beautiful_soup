from bs4 import BeautifulSoup


def get_html_content(this_url: str, parser: str = 'lxml') -> str:
    with open(this_url, 'r') as html_file:
        content = html_file.read()

    return content


stud_html = get_html_content('samples/Stud_Book_Argentino.html', 'html.parser')
soup = BeautifulSoup(stud_html, 'lxml')

# find searches just the first element
tag = soup.find('h5')
print(tag)
print('=' * 100)

# find_all searches ALL the results
tags = soup.find_all('h5')
for title in tags:
    print(title.text)

print('=' * 100)

# find_all male horses
print('---- MALE HORSES ----')
tags = soup.find_all('div', class_='wMacho')
for title in tags:
    print(title.text)

print('=' * 100)

# find_all female horses
print('\n---- FEMALE HORSES ----')
tags = soup.find_all('div', class_='wHembra')
for horse in tags:
    print('Puntos:', horse.span.text)
    print('Nombre:', horse.a.text)
    print('Nacimiento:', horse.text[-10:])
    print('Link:', horse.a.get('href'))
    print('-' * 50)

print('=' * 100)

# find_all female horses
print('\n---- FEMALE HORSES - Full element ----')
tags = soup.find_all('div', class_='wHembra')
for horse in tags:
    print('Puntos:', horse.span.text)
    print('Nombre:', horse.a.text)
    print('Nacimiento:', horse.text[-10:])
    print('Link:', horse.a.get('href'))
    print('-' * 50)

print('=' * 100)
