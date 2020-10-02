from bs4 import BeautifulSoup
import requests, re, xlrd, xlwt, openpyxl
from urllib.request import urlopen
workbook = xlwt.Workbook()
# openpyxl.load_workbook(filename = 'Парсинг.xls')
worksheet = workbook.add_sheet('Товары')


html = urlopen("https://beru.ru/catalog/produkty/76022?hid=91307").read().decode('utf-8')
s=str(html)
soup = BeautifulSoup(s, "lxml")

names = []
prices = []

spans_name = soup.findAll ('span', class_= '_3l-uEDOaBN _20Jv_9PW6N _3HJsMt3YC_ QDV8hKAp1G')
# spans_name = soup.findAll ('div', class_= 'ZA6gBYE-kC')

                          
for span in spans_name:
    for i in re.findall(r'(?<=data-tid=\"52906e8d\" data-tid-prop=\"52906e8d\"\>).*?(?=\<\/span\>)', str(span)):
    # for i in re.findall(r'(?<=img alt=\").*?(?=\" class)', str(span)):
    # for i in re.findall(r'(?<=title=\').*?(?=\'\/\>\<\/div\>)', str(span)):
        names.append(i)

spans_price = soup.findAll ('div', class_= '_1u3j_pk1db') 
spans_price2 = soup.findAll ('span', class_= '1pTV0mQZJz _37FeBjfnZk _3LMhEMfZeH _brandTheme_default')                                            
                                                                                        
# for span in spans_name:
for span in spans_price:
    for i in re.findall(r'(?<=span data-tid=\"c3eaad93\"\>).*?(?=\<\/span\>)', str(span)):
        if not None:
            prices.append(i)
        else:
            prices.append(0)


for i in range(len(names)):
    worksheet.write(i + 1, 0, names[i])
  
for i in range(len(prices)):
    worksheet.write(i + 1, 1, prices[i])  

workbook.save('Парсинг.xls')

print(spans_name)
    
# with open(input()) as f:
    # text = f.w(spans_name)
    
    
# worksheet.write (0,0, spans_name)
# for name in names:
    # print (name)

# for price in prices:
    # print (price)
    
    
    
    
# for i in soup.findAll('div', class_='_3JBXGbvG3w.BwiWCn5vjp'):
        # if news[i].find('span', class_='time2 time3') is not None:
        # new_news.append(news[i].text)

# span = soup.find ('span', attrs = {'class': '_3l-uEDOaBN _20Jv_9PW6N _3HJsMt3YC_ QDV8hKAp1G'})
# name = name_box.text.strip () # strip () используется для удаления стартового и конечного


# получить индексную цену
# price_box = soup.find ('div', attrs = {'class': 'price'})
# price = price_box.text










input()