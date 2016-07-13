"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

    Salesperson's name, total $ of order & total number of melons sold.

    Anna Parker|1881.91|13


"""

sales_data = {}

# salespeople = []                 # creating empty lists to add the info fr:
# melons_sold = []                 # txt file, salesperson name & # sold

f = open("sales-report.txt")     # opens the sales report file
for line in f:
    line = line.rstrip()         # formatting - removes extra whitespace
    line = line.split("|")    # creating a list out of each line in file
    salesperson, order_amount, melons_sold = line

print line
                                 # it doesn't currently use the amount sold.
                                 # It's easy to add, I'll add it to my queue.

#     if salesperson in salespeople:         # if the salesperson's name is
#         position = salespeople.index(salesperson)  # already in the list, add
#         melons_sold[position] += melons          # to # of melons sold.
#     else:
#         salespeople.append(salesperson)    # if salesperson is not already in
#         melons_sold.append(melons)         # the list, add name # # of melons


# for i in range(len(salespeople)):
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])

                                # prints report of entire list
