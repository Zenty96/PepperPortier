import csv, sys

class CSVReader(object):
    def __init__(self):
        pass

    def readCSV(self):
        filename = 'Ressourcen/Raumliste.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                liste = []
                for row in reader:
                    liste += row
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            return liste
