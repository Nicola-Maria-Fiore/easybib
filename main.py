from habanero import Crossref
import requests

cit_file = "resources/citations.txt"
cit_out_file = "results/citations.txt"
cit_out_file_csv = "results/citations.csv"
cr = Crossref()


def getBibtex(DOI):
    try: 
        url_bibtex = "http://api.crossref.org/works/" + DOI + "/transform/application/x-bibtex"
        x = requests.get(url_bibtex)
        return str(x.text)
    except:
        return None


def getDOI(query): 
    try:
        x = cr.works(query=query, sort="relevance", select=["DOI","title"])
        paper = (x["message"]["items"])[0]
        return paper["DOI"]
    except:
        print("Crossref error")
        return None


if __name__ == "__main__":
    citations = []
    with open(cit_file) as file_in:
        for line in file_in:
            citations.append(line.strip())

    bibtex = ""
    csv = "DOI;BIBTEX;CITATION"
    for c in citations:
        doi = getDOI(c)
        if  doi!=None:
            b = getBibtex(doi)
            if b!=None:
                bibtex += "\n"+str(b)
                b = True
        csv += '\n'+str(doi)+";"+str(b)+";"+c.replace(";"," ")

    
    with open(cit_out_file, 'w') as file_out:
        file_out.write(bibtex)
    
    with open(cit_out_file_csv, 'w') as file_out:
        file_out.write(csv)
        
    print("Done!")

    
    