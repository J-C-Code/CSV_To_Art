import sys
from tabulate import tabulate
import csv


def printFile(files):
    items = []
    try:
        with open(files) as file:
            reader = csv.reader(file)
            for row in reader:
                items.append(row)
            return(tabulate(items[1:], headers=items[0], tablefmt='grid'))
    except FileNotFoundError:
        return('File does not exist')

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too little arguments")
    elif not sys.argv[-1][-4:] == ".csv":
        sys.exit("Wrong file type.")
    else:
        userFile = sys.argv[-1]
        printFile(userFile)

if __name__ == "__main__":
    main()
