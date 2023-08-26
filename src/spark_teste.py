from pyspark.sql import SparkSession, functions as f

spark = SparkSession\
    .builder\
    .appName("twitter_transformation")\
    .getOrCreate()

df = spark.read.json("/home/daniel/Documents/airflow_dados_twiter/datalake/twitter_datascience")
df.show()
df.printSchema()

tweet_df = df.select(f.explode("data").alias("tweets"))\
.select("tweets.author_id", "tweets.conversation_id",
        "tweets.created_at", "tweets.id",
        "tweets.public_metrics.*", "tweets.text")

user_df = df.select(f.explode("includes.users").alias("tw_users"))\
    .select("tw_users.*")

tweet_df.show()
user_df.show()

tweet_df.coalesce(1).write.mode("overwrite").json('output/tweet')
user_df.coalesce(1).write.mode("overwrite").json('output/user')