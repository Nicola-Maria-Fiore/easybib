# EasyBib

pip install -r requirements.txt

from a list of DOIs generate bibtex. Fill *resources/doi.txt* with the DOIs and run 
py main.py -d

From a list of citations generate bibtex. Fill *resources/citations.txt* with the citations and run 
py main.py -c

From a query on Google Scholar generate a csv with the metadata of the result. To do so, fill the *resources/url.txt* with the scholar search links and run 
py main.py -s 5 

(where 5 is the number of Scholar pages to inspect).

Results are available on the *results* folder

