from bs4 import BeautifulSoup

from utils import get_html_content

stud_html = get_html_content('samples/Stud_Book_Argentino.html', 'html.parser')
soup = BeautifulSoup(stud_html, 'html.parser')

full_table = soup.find('table', id="table-pedigree")
print(full_table)
print("=" * 100)

print(full_table.tbody.find('tr').find('td').a.text)
print(full_table.tbody.find_all('tr')[-1].find('td').a.text)

print("=" * 100)

temp_item = soup.find('p', class_="text-center").text.replace('\n', '')
print(temp_item)
