import requests
import csv

def filter(products, keyfilter):
     for key in products.keys():
        collist= []
        if key == keyfilter:
            colors = products[key].split(',')
            for col in colors:
                color = col.split('::')
                for i in range(0, len(color), 3):
                    collist.append(color[i])
            products[key] = ', '.join(map(str, collist))

def extract(products):
    for key in products.keys():
        if products[key] == 'False' or products[key] == 'false' or products[key] == False:
            products[key] = 'NO'
        elif products[key] == 'True' or products[key] == 'true' or products[key] == True:
            products[key] = 'YES'

    for key in products.keys():
        if type(products[key]) == list: 
            products[key] = ', '.join(map(str,products[key]))
    filter(products, keyfilter = "unbxd_color_for_category")
    filter(products, keyfilter = "test_colors")
    filter(products, keyfilter = "colorSwatch")
    return products

def main():
    URL = "https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=10&start=0"
    r = requests.get(url = URL) 
    start = 0
    data = r.json() 
    products = data['response']['products'][0]
    results = extract(products)
    with open('Unbxd-2021-interns test_VigneshTS.csv', 'w') as f:  
        writer = csv.writer(f)
        for k, v in results.items():
            writer.writerow([k, v])
    if r:
        extract(products)
        with open('Unbxd-2021-interns test_VigneshTS.csv', 'a') as f:  
            writer = csv.writer(f)
            for k, v in results.items():
                writer.writerow([k, v])
        start += 0
        URL = "https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=10&start="+str(start)
        r = requests.get(url = URL) 
        data = r.json() 
        products = data['response']['products'][0]


    
if __name__ == "__main__":
    main()
