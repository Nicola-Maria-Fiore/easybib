from habanero import Crossref
from Utils import Utils
from cit2bib import getBibtex

def start():
    print("DOI -> BIBTEX")
    dois = Utils.readFileLines(Utils.doi_file)

    bibtex = ""
    csv = "DOI;BIBTEX"
    for i,doi in enumerate(dois):
        print("Processing {}/{}".format(str(i),str(len(dois))))
        b = getBibtex(doi)
        if  b!=False:
            bibtex += "\n"+str(b)
            b = True
        csv += '\n'+str(doi)+";"+str(b)

    Utils.writeFile(Utils.doi_out_file, bibtex)
    Utils.writeFile(Utils.doi_out_file_csv, csv)