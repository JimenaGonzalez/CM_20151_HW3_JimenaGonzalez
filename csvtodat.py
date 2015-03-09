import csv

f= open("Notas.csv",'rt')
g= open("a.dat",'wt')

try:
    reader = csv.reader(f)
    writer = csv.writer(g, quoting=CSV.QUOTE_NONNUMERIC)
    for row in reader:
        print row
        a= row.replace(",","+")
        writer.writerow(a)
finally:
    f.close()
    g.close()
