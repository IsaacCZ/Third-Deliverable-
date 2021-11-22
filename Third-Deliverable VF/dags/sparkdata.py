from pyspark.ml import Pipeline
from  pyspark.ml.feature import StopWordsRemover, Tokenizer
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('data_processing').getOrCreate()


tokenizer = Tokenizer(outputCol="list_review").setInputCol("review_str")
remover = StopWordsRemover(outputCol="review_token").setInputCol("list_review")

pipeline.fit(df).transform(df)\
    .withColumn("positive_review", F.when(F.array_contains("review_token", "good"), 1))\
    .fillna({'positive_review':0}).show()

    