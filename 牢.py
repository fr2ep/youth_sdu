import requests,re
from bs4 import BeautifulSoup
import xlwings as xw
import pandas as pd
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
server="https://www.youth.sdu.edu.cn/"
def get_content(target):
    response=requests.get(url=target,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    texts=soup.find("div",attrs={"class":"art-main"})
    content=texts.text
    return content
if __name__=="__main__":
    target=server
    response=requests.get(url=target,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    h2=soup.find_all("h2",limit=3)
    pretitle=soup.find_all("div",attrs={"class":"gg-tit"},limit=3)
    for h in h2:
        print(h.text.strip())
        print(server+h.a.get("href"))
    for t in pretitle:
        title=t.find_next_sibling()
        titlea=title.find_all("a")
        for onepiece in titlea:
            print(onepiece.text.replace(" ",""))
            print(server+onepiece.get("href"))
            print(get_content(server+onepiece.get("href")))
