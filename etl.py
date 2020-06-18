#import dependencies
import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, hour, dayofmonth, weekofyear, date_format

#declare config variable with the ConfigParser() funtion from the configparser class
config = configparser.ConfigParser()
config.read('dl.cfg') #read in the dl configuration file

# set aws credential global variables by calling objects in the dl config file
os.environ['AWS_ACCESS_KEY_ID'] = config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_KEY'] = config['AWS_SECRET_KEY']

#function to create spark session

def create_spark_session():
    spark = SparkSession \
        .builder \
        .appName('Data lake') \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:2.7.0') \
        .getOrCreate()




def process_song_data(input, output)