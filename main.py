import sys
import cit2bib
import doi2bib
import ScholarCite


if __name__ == "__main__":
    if sys.argv[1]=="-c":
        cit2bib.start()
    elif sys.argv[1]=="-d":
        doi2bib.start()
    elif sys.argv[1]=="-s":
        ScholarCite.start(int(sys.argv[2]))
    else:
        print("Argument error")
        sys.exit()
        
    print("Done!")

    
    