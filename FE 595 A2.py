
# coding: utf-8

# In[173]:


from flask import Flask
import requests
from bs4 import BeautifulSoup   #The Beautiful Soup package is used to extract data from html files. 
from urllib.request import urlopen  #The urllib.request module is used to open URLs. 
import re 
from requests import get


# In[174]:


#After importing necessary modules, 
#specify the URL containing the dataset and pass it to urlopen() to get the html of the page.

url = "https://theyfightcrime.org/"
html = urlopen(url)
        
    

text_html = requests.get('https://theyfightcrime.org/')   #Make request


# In[175]:


#Make a request to “theyfightcrime.org”   


print(text_html.text)   #Print the HTML code


# In[176]:




soup = BeautifulSoup(text_html.text, 'lxml')


# In[177]:


#Remove all style and font elements

for script in soup(["script", "style"]):
    script.extract() 


# In[178]:


text = soup.get_text()
print(text)  #Prints only text on website
type(text)


# In[179]:


#We want to generate two files.
#Save the male characters in one text file and save the female characters in another text file.

#Repeat 50 times (once done above)


# In[182]:



def web_scraper(url):       #Define a function 
    Male = open("Male.txt","w+")      #The open() function opens a file, and returns it as a file object                     
    Female = open("Female.txt","w+")    #"w" - Write - will overwrite any existing content                    
    for i in range(0,50):
        get_request = get(url)        #get request as above. Repeat 50 times.  
        
        soup = BeautifulSoup(get_request.text, "html.parser")  
        link = soup.select("center p")                #html
        text = link[0].get_text()                     #select text    
        list_split = text.split("She")                #extract She   
        Male.write(list_split[0][:-1]+"\n")            #Previous sentence split                
        Female_split=('She'+list_split[1]).split("They fight crime!")     #Remove the They fight crime part for She sentences
        Female.write(Female_split[0]+"\n")                

    Male.close()  
    Female.close()                                        


if __name__=="__main__":
    web_scraper("https://theyfightcrime.org/")
    
    


# In[156]:


##I have used various sources for the above code like datacamp.com(first part). 
#The last part to write files and extracting the words was looked up on google and github (never used beautifulSoup before)

