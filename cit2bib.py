from habanero import Crossref
from Utils import Utils
import requests

cr = Crossref()

def getBibtex(DOI):
    try: 
        url_bibtex = "http://api.crossref.org/works/" + DOI + "/transform/application/x-bibtex"
        x = requests.get(url_bibtex, headers=Utils.HEADERS)
        x = str(x.text)
        if x[0]!="@":
            return False
        start_au = x.find("author = {")
        if start_au>=0:
            end_au = x.find("}",start_au)
            subs = (x[start_au:end_au]).split()
            i = 1
            while i<len(subs):
                subs[i] = subs[i].lower()
                if subs[i] != "and":
                    name = list(subs[i])
                    k = 0
                    if name[0] in ["{","("]:
                        k = 1
                    name[k] = name[k].upper()
                    subs[i] = "".join(name)
                i += 1
            x = x[:start_au] + " ".join(subs) + x[end_au:]
        return x
    except  Exception as e:
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
    csv = '"DOI","CITATION","BIBTEX"'
    for i, c in enumerate(citations):
        print("Processing {}/{}".format(str(i),str(len(citations))))
        doi = getDOI(c)
        b = False
        if  doi!=False:
            b = getBibtex(doi)
            if b!=False:
                bibtex += "\n"+str(b)
        csv += '\n"'+str(doi)+'","'+c+'","'+str(b).replace("\n","")+'"'

    Utils.writeFile(Utils.cit_out_file, bibtex)
    Utils.writeFile(Utils.cit_out_file_csv, csv)