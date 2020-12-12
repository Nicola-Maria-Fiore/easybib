class Utils:
    #Files fot task citation -> bibtex
    cit_file = "resources/citations.txt"
    cit_out_file = "results/citations.txt"
    cit_out_file_csv = "results/citations.csv"

    #Files fot task doi -> bibtex
    doi_file = "resources/dois.txt"
    doi_out_file = "results/dois.txt"
    doi_out_file_csv = "results/dois.csv"

    def readFileLines(name):
        lines = []
        with open(name, encoding="utf-8") as file_in:
            for line in file_in:
                lines.append(line.strip())
        return lines

    def writeFile(name,content):
        with open(name, 'w', encoding="utf-8") as file_out:
            file_out.write(content)