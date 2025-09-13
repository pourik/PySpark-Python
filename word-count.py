from pyspark import SparkContext, SparkConf
import collections

conf = SparkConf().setMaster("local").setAppName("Word-Count")
sc = SparkContext(conf=conf)

lines = sc.textFile("file:///PySpark-Python/book.txt")
words = lines.flatMap(lambda x: x.split())
wordCounts = words.countByValue()
print(type(wordCounts))

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + " " + str(count))