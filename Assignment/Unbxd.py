import requests
import csv
from time import sleep
from random import randint

def filter(products, keyfilter):
    if keyfilter in products.keys():    
        colorlist= []
        items = products[keyfilter].split(',')
        for item in items:
            color = item.split('::')
            for i in range(0, len(color), 3):
                colorlist.append(color[i])
        products[keyfilter] = ', '.join(map(str, colorlist))

def filterColorMap(products, keyfilter):
    if keyfilter in products.keys():
        colorlist= []
        items = products[keyfilter].split('::')
        for index in range(0, len(items), 2):
            colorlist.append(items[index])
        products[keyfilter] = ', '.join(map(str, colorlist))

def extract(products):
    for key in products.keys():
        if type(products[key]) == list: 
            products[key] = ', '.join(map(str,set(products[key])))

    for key in products.keys():
        if products[key] == 'False' or products[key] == 'false' or products[key] == False:
            products[key] = 'NO'
        elif products[key] == 'True' or products[key] == 'true' or products[key] == True:
            products[key] = 'YES'


    filter(products, keyfilter = "unbxd_color_for_category")
    filter(products, keyfilter = "test_colors")
    filter(products, keyfilter = "colorSwatch")
    filterColorMap(products, keyfilter = "unbxd_color_mapping")
    return products

def main():
    URL = "https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=10&start="
    for page in range(0, 10): 
        page = requests.get(URL + str(page))
        if page:
            data = page.json() 
            products = data['response']['products'][0]
            results = extract(products)

    csv.register_dialect('myDialect', delimiter=',', doublequote=True,
    quoting=csv.QUOTE_NONE)
    with open('Unbxd-2021-interns test_VigneshTS.csv', 'a') as f:  
        writer = csv.writer(f, skipinitialspace = True,  quoting=csv.QUOTE_NONE, escapechar=' ')
        for k, v in results.items():
            writer.writerow([k, v])

if __name__ == "__main__":
    main()
