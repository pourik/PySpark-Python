from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local').setAppName('Word-Count-Regex')
sc = SparkContext(conf = conf)

def extractingRequiredFields(line):
    fields = line.split(",")
    return (int(fields[0]), float(fields[2]))

input = sc.textFile("customer-orders.csv")
mappedInput = input.map(extractingRequiredFields)
totalByCustomer = mappedInput.reduceByKey(lambda x, y: x + y)


flipped = totalByCustomer.map(lambda x: (x[1], x[0])) #or map(lambda (x, y): (y, x))
sortedTotalByCustomer = flipped.sortByKey()
flippedBack = sortedTotalByCustomer.map(lambda x: (x[1], x[0]))
finalSortedTotalByCustomer = flippedBack.sortByKey()

results = finalSortedTotalByCustomer.collect()
for result in results:
    print(result)