from pyspark import SparkContext, SparkConf
import re

conf = SparkConf().setMaster('local').setAppName('Word-Count-Regex-sorted')
sc = SparkContext(conf = conf)

def normalize_words(text):
    return re.compile(r"\W+", re.UNICODE).split(text.lower())

lines = sc.textFile("file:///PySpark-Python/book.txt")
words = lines.flatMap(normalize_words)
wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
wordCountSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
print(type(wordCountSorted))
results = wordCountSorted.collect()
print(type(results))

for result in results:
    count = str(result[0])
    cleanWord = result[1].encode('ascii', 'ignore')
    if cleanWord:
        print(cleanWord.decode() + ":\t\t" + count)
