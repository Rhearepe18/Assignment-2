
from flask import Flask
import requests
from bs4 import BeautifulSoup   #The Beautiful Soup package is used to extract data from html files. 
from urllib.request import urlopen  #The urllib.request module is used to open URLs. 
import re 
from requests import get

#After importing necessary modules, 
#specify the URL containing the dataset and pass it to urlopen() to get the html of the page.

url = "https://theyfightcrime.org/"
html = urlopen(url)
   

text_html = requests.get('https://theyfightcrime.org/')   #Make request

#Make a request to “theyfightcrime.org”   

print(text_html.text)   #Print the HTML code

soup = BeautifulSoup(text_html.text, 'lxml')

#Remove all style and font elements

for script in soup(["script", "style"]):
    script.extract() 

text = soup.get_text()
print(text)  #Prints only text on website
type(text)


#We want to generate two files.
#Save the male characters in one text file and save the female characters in another text file.

#Repeat 50 times (once done above)

def ws(url):       #Define a function 
    male = open("Male.txt","w+")      #The open() function opens a file, and returns it as a file object                     
    female = open("Female.txt","w+")    #"w" - Write - will overwrite any existing content                    
    for i in range(0,50):
        get_request = get(url)        #get request as above. Repeat 50 times.  
        
        soup = BeautifulSoup(get_request.text, "html.parser")  
        link = soup.select("center p")                #html
        text = link[0].get_text()                     #select text    
        s = text.split("She")                #extract She   
        male.write(s[0][:-1]+"\n")            #Previous sentence split                
        split=('She'+ s[1]).split("They fight crime!")     #Remove the They fight crime part for She sentences
        female.write(split[0] + "\n")                

    male.close()  
    female.close()                                        


ws("https://theyfightcrime.org/")

