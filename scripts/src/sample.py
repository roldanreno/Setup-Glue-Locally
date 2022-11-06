import sys
from operator import add
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

# Create Spark Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Print word and count letters
data = sc.parallelize(list("Hello World"))
counts = data.map(lambda x: 
	(x, 1)).reduceByKey(add).sortBy(lambda x: x[1],
	 ascending=False).collect()

palabra = "Hello World"
print("--------------------------------------------- Script Start ---------------------------------------------")
print(palabra)
print(palabra[::-1])

for (word, count) in counts:
    print("{}: {}".format(word, count))

print("--------------------------------------------- Script End ---------------------------------------------")
