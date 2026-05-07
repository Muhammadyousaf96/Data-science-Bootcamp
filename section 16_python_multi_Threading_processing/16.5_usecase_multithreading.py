import threading 
import requests
from bs4 import BeautifulSoup

urls=[
    'https://www.geeksforgeeks.org/python/generators-in-python/',
    'https://www.w3schools.com/cpp/cpp_intro.asp',
    'https://en.wikipedia.org/wiki/History_of_Python'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fecthed {len(soup.text)} character from {url}")
    
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))    
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join() 
       
print("All web fecheds")             

# output 
# Fecthed 5754 character from https://www.geeksforgeeks.org/python/generators-in-python/
# Fecthed 126 character from https://en.wikipedia.org/wiki/History_of_Python
# Fecthed 40651 character from https://www.w3schools.com/cpp/cpp_intro.asp
# All web fecheds