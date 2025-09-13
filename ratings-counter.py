from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()
print(type(result))

sortedResults = collections.OrderedDict(sorted(result.items()))
print(type(sortedResults))
print(sortedResults)
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
