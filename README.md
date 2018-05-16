# Tagger
This software is a Basic Amazon Scrapper with Tagger that tags the products found in the Product.xlsx excel by looking for said product on amazon and get the category of it and stores it in Category.xlsx.

## Working
The Product excel sheet is read and a python list is generated with the help of Pandas library.

The amazonID of the Products found in the product list is generated with the help of [amzSear](https://github.com/asherAgs/amzSear)

Once we get the amazonID , we preform basic website scrapping with the help of [ScrapeHero's](https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python/) basic function as a base and modified a bit to exectue on python 3.6 and to get a desired result.

Then the list of categories are dumped into Category.xlsx.

## Installation
Programs that need to be installed.

-[Python 3.XX](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

-[PIP](https://docs.python.org/3/installing/)

Once we have the required software, we need to import the requred python libraries.
Hence in Command Prompt with PIP active type in the following.

>$ pip install requests lxml

>$ pip install amzsear

>$ pip install pandas

Now just run the Python program with the products.xlsx and category.xlsx in the same folder.

(an active internet connection is required for program to provide results.)

## Known issues and solutions

1.Product not found on Amazon.in

  -If a product is not found on Amazon.in it will tag the category as None.
   this include products found in Amazon pantry or any other subcategory from the main site.
   
  *Solution*
  
   -Scrapping from diffrent sites take diffrent meathods
   
2.Captcha Error

  -This error occurs if a purticalr ip constantly visits the website, the website asks for a Captcha to prove it is a human thus halting
   the whole program.

  *Solution*
  
   -Use amazon's official API to bypass this. But to get the offical API you need to register yourself and get a amazon app id from         amazon 
