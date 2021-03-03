import requests
import json
import pandas
from time import sleep

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
    URL = "https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=20&start="
    results = []
    for page in range(0, 25): 
        r = requests.get(URL + str(page), timeout=5)
        if r.ok:
            data = r.json() 
            products = data['response']['products'][0]
            results.append(extract(products))
            sleep(r.elapsed.total_seconds())
            print(f"Took {r.elapsed.total_seconds()} seconds")
    with open('unbxd.json', 'w') as f:
        json.dump(results, f, indent=2) 
    with open('unbxd.json') as f:
        data = pandas.read_json('unbxd.json')
        data.to_csv('Unbxd-2021-interns test_VigneshTS.csv', index=False)

if __name__ == "__main__":
    main()
