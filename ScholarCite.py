import time
import requests
import functools
import pandas as pd
from bs4 import BeautifulSoup
from Utils import Utils

df = pd.DataFrame(columns=["Title","Cite", "Author", "Year", "Info", "Link"])
df_count = 0

def getAutJurPub(tag):
    info = ["--", "--", "--"]
    start = tag.find("div", class_="gs_a") #Find author, journal, year
    if start!=None:
        s = start.text.split("-")
        if len(s)==3:
            info = s
    return info


def schoolarParser(html):
    global df_count, df

    result = []
    soup = BeautifulSoup(html, "html.parser")
    for element in soup.findAll("div", class_="gs_r gs_or gs_scl"):
        title = None
        link = None
        cites = None
        for h3 in element.findAll("h3", class_="gs_rt"): #Find title and link
            found = False
            for a in h3.findAll("a"): 
                if found == False:
                    title = a.text
                    link = a.get("href")
                    found = True
        for a in element.findAll("a"): #Find cite
                if "Cited by" in a.text:
                    cites = int(a.text[8:])     
        
        info = getAutJurPub(element)
        df.loc[df_count] = [title, cites, info[0], info[1], info[2], link]
        df_count += 1


def start(query, scholar_pages):
    global df
    print("Sort Scholar results by cite")
    url = "https://scholar.google.com/scholar?hl=en&q="+query+"&as_vis=1&as_sdt=1,5"  
        
    results = []
    i = 0
    while i < scholar_pages:
        html = requests.get(url, headers=Utils.HEADERS)
        html = html.text
        
        papers = schoolarParser(html)
        results.append(papers)

        i += 1
        url += "&start=" + str(10*i)
        
    df = df.applymap(lambda x: str(x).replace(","," "))
    df["Cite"] = df["Cite"].astype('int64')
    df = df.sort_values(by=['Cite'], ascending=False)
    df.to_csv("results/scholar_cite.csv",encoding='utf-8-sig', index=False)