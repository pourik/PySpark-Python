from pyspark import SparkContext, SparkConf
import re

conf = SparkConf().setMaster('local').setAppName('Word-Count-Regex')
sc = SparkContext(conf = conf)

def normalize_words(text):
    return re.compile(r"\W+", re.UNICODE).split(text.lower())

lines = sc.textFile("file:///PySpark-Python/book.txt")
words = lines.flatMap(normalize_words)
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if(cleanWord):
        print(cleanWord.decode() + " " + str(count))