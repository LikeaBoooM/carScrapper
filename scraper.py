from bs4 import BeautifulSoup
import requests


class Car :
    def __init__(self,name,ref,prize):
        self.name = name
        self.ref = ref
        self.prize = prize
        super().__init__()



BASE_URL = "https://www.olx.pl/motoryzacja/samochody/"
FILTER_URL = "?search%5Bfilter_float_price%3Afrom%5D={}&search%5Bfilter_float_price%3Ato%5D={}&search%5Bfilter_enum_petrol%5D%5B0%5D={}&search%5Bfilter_enum_transmission%5D%5B0%5D={}"
BRAND = "audi"
MODEL = "a6"
MODEL_URL = "{}/{}/".format(BRAND,MODEL)
PRICE_FROM = 2000 
PRICE_TO =  25000
PETROL = "diesel"
SHIFT = "manual"

URL = BASE_URL + MODEL_URL + FILTER_URL.format(PRICE_FROM,PRICE_TO,PETROL,SHIFT)
FINAL_URL = URL.lower()
##print((FINAL_URL).lower())
response = requests.get(FINAL_URL)
data_cars = response.text

soup = BeautifulSoup(data_cars, features='html.parser')
cars_listings = soup.find_all('td',{'class':'offer'})


car_list = []

for cars in cars_listings:
    if cars.find('img', {'class':'fleft'}) is None:
        print("www.olx.pl")
    else:
        #print(cars.find('img', {'class':'fleft'}).get('alt'))
        car_name = cars.find('img', {'class':'fleft'}).get('alt')

    if cars.find('img',{'class':'fleft'}) is None:
        print("www.olx.pl")
    else:
        #print(cars.find('img',{'class':'fleft'}).get('src'))
        car_img = cars.find('img',{'class':'fleft'}).get('src')

    if cars.find(class_='space inlblk rel') is None:
        print("www.olx.pl")
    else:
        #print(cars.find(class_='space inlblk rel').find(class_='price').text)
        car_price = cars.find(class_='space inlblk rel').find(class_='price').text

    if cars.find('td') is None:
        car_url = "www.olx.pl"
    elif cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}) is None : 
        car_url = "www.olx.pl"
    else :
        #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
        car_url = cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href')
        #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
    car_list.append((car_name,car_price,car_url, car_img))


print(car_list)

##DZIALA
#car_name = cars_listings[i].find('h3', {'class':'lheight22 margintop5'}).find('strong').text
#car_url = cars_listings[i].find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href')
#car_price =cars_listings[i].find(class_='space inlblk rel').find(class_='price').text
#car_img = cars_listings[0].find('img',{'class':'fleft'}).get('src')
#print(car_img)




#for cars in cars_listings:
    #if cars.find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href') != None:
        #car_name = cars.find('h3', {'class':'lheight22 margintop5'}).find('strong').text
        #car_url = cars.find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href')
        #car_price =cars.find(class_='space inlblk rel').find(class_='price').text
        #print(car_name)
        #print(car_url)
        #print(car_price)
    #else : 
        #car_name = cars.find('h3', {'class':'lheight22 margintop5'}).find('strong').text
        #car_url = "www.olx.pl"
        #car_price =cars.find(class_='space inlblk rel').find(class_='price').text

        #car_list.append((car_name,car_price))
#car_names = soup.find('h3', {'class':'lheight22 margintop5'}).text
#car_price = cars_listings[0].find(class_='space inlblk rel').find(class_='price').text
#car_name = cars_listings[0].find('h3', {'class':'lheight22 margintop5'}).find('strong').text
#print(cars_listings)
#car_url = soup.find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).find('a').find('href')
#print(car_url)
#if car_url is not None :
#    print("MATII")
#else : 
#    print(car_url)
#car_list = []


#for cars in cars_listings[:-1]:
    #car_name = cars.find('h3', {'class':'lheight22 margintop5'}).find('strong').text
    #car_price =cars.find(class_='space inlblk rel').find(class_='price').text
    #car_url = cars.find('a',{'class':'marginright5 link linkWithHash'}).get('href')
    #print(car_name)
    #print(car_price)
    #car_url = cars.find('a',{'class':'marginright5 link linkWithHash'}).get('href')
    
    #car_list.append((car_name,car_price))
    
    #car_url = cars.find('a',{'class':'marginright5 link linkWithHash detailsLinkPromoted'}).get('href')
    
    



