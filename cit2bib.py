from habanero import Crossref
from Utils import Utils
import requests

cr = Crossref()

def getBibtex(DOI):
    try: 
        url_bibtex = "http://api.crossref.org/works/" + DOI + "/transform/application/x-bibtex"
        x = requests.get(url_bibtex, headers=Utils.HEADERS)
        x = str(x.text)
        start_au = x.find("author = {")
        if start_au>=0:
            end_au = x.find("}",start_au)
            subs = (x[start_au+1:end_au]).split()
            i = 0
            print(subs)
            while i<len(subs):
                subs[i] = subs[i].lower()
                name = subs[i]
                name[0] = name[0].upper()
                subs[i] = name
                i += 1
            x = x[:start_au] + " ".join(subs) + x[end_au:]
        return x
    except  Exception as e:
        print(e)
        return False


def getDOI(query): 
    try:
        x = cr.works(query=query, sort="relevance", select=["DOI","title"])
        paper = (x["message"]["items"])[0]
        return paper["DOI"]
    except:
        return False

def start():
    print("CITATIONS -> BIBTEX")
    citations = Utils.readFileLines(Utils.cit_file)

    bibtex = ""
    csv = "DOI;BIBTEX;CITATION"
    for i, c in enumerate(citations):
        print("Processing {}/{}".format(str(i),str(len(citations))))
        doi = getDOI(c)
        b = False
        if  doi!=False:
            b = getBibtex(doi)
            if b!=False:
                bibtex += "\n"+str(b)
                b = True
        csv += '\n'+str(doi)+";"+str(b)+";"+c.replace(";"," ")

    Utils.writeFile(Utils.cit_out_file, bibtex)
    Utils.writeFile(Utils.cit_out_file_csv, csv)