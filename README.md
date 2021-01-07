# EasyBib
EasyBib is a python tool that lets you:
- Generate bibtex given a list of dois. To do so, fill the *resources/doi.txt* with the dois and run 
py main.py -d

- Generate bibtex given a list of citations. To do so, fill the *resources/citations.txt* with the dois and run 
py main.py -c

- Given a query on Google Scholar generate a csv with the metadata of the result. To do so, fill the *resources/url.txt* with the scholar search links and run 
py main.py -s 5 

(where 5 is the number of Scholar pages to inspect)
The results will be available on the *results* folder
