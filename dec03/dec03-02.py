with open('diagnostic.txt') as d:
    diagnostic_codes = d.readlines()

diagnostic_codes = [i.strip('\n') for i in diagnostic_codes]
