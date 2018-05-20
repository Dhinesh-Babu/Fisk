from amzsear import AmzSear
import re
from lxml import html  
import csv,os,json
import requests
from time import sleep
import pandas as pd


#Function to Scrap Category given URL of Product with Amazon Id search.
#note if direct product url is passed it gives a search result in place of catagory.
def AmzonParser(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'

 
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
 
            #If product in Amazon Pantry.
            if CATEGORY == None:   
                XPATH_CATEGORY = '//span[@class="zg_hrsr_ladder"]//text()'
                RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
                CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
           
            if page.status_code!=200:
                return "Captcha"
            print(CATEGORY)
            return CATEGORY
        except Exception as e:
            print(e)

#Using Pandas to Read Excel Sheet for Products stored in Coloum            
df = pd.read_excel('Products.xlsx',index=None)
SearchList=df.iloc[: , 0]#get only first Coloum

#List of Category
Extracted_Data = []


#Finding Amazon ID
for Item in SearchList:
    Result=AmzSear(Item,region='IN')
    Product=Result.rget(1)
    

    #If Product is not found on Amazon, Set Catagory as NONE and continue
    if(Product==None):
        print("NotAvailable")
        Extracted_Data.append("NotAvailable")
        continue
    print("\nFound "+Product.title)



    #get Product Amazon Id
    Tag='/dp/'
    Before_Tag,Tag,After_Tag=Product.product_url.partition(Tag)
    After_Tag=After_Tag.split('/')
    Azid=After_Tag[0]



    #Scrap for Category
    url = "http://www.amazon.in/dp/"+Azid
    print("Processing: "+url)
    Extracted_Data.append(AmzonParser(url))
    if Extracted_Data[-1] == "captcha":
        break
    sleep(1)



#Storign Category in Excel
df=pd.DataFrame({'Categories': Extracted_Data})
df.to_excel('category.xlsx',header=False,index=False)






    


    

    
