"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

    Salesperson's name, total $ of order & total number of melons sold.

    Anna Parker|1881.91|13


"""

salespeople = []                 # creating empty lists to add the info fr:
melons_sold = []                 # txt file, salesperson name & # sold

f = open("sales-report.txt")     # opens the sales report file
for line in f:                   
    line = line.rstrip()         # formatting - removes extra whitespace
    entries = line.split("|")    # creating a list out of each line in file
    salesperson = entries[0]     # grabs the salespersons' name on each line
    melons = int(entries[2])     # grabs their respective # of melons sold

    if salesperson in salespeople:      
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
