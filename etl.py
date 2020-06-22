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
os.environ['AWS_ACCESS_KEY_ID'] = config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_KEY'] = config['AWS']['AWS_SECRET_KEY']

#function to create spark session
def create_spark_session():
    spark = SparkSession \
        .builder \
        .appName('Data lake') \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:2.7.0') \
        .getOrCreate()

#this function will take song data input, process it and store it to the lake
def process_song_data(spark, input_data, output_data):

    # get file path of song_data 
    # input_data = 's3a://udacity-dend/'  os.join.path concatenates the file paths
    # song data path ex. /song_data/A/A/A/TRAAAAK128F9318786 <- Key
    song_data = os.join.path(input_data, '/song_data/*/*/*/*.json')

    # read in the song data
    df = spark.read.json(song_data)

    # create song table by extracting song data columns from df
    #song_table = df[]



def process_log_data(spark, input_data, output_data):

    # get file path for the log data
    # log data path ex. log_data/2018/11/2018-11-01-events <- key 
    log_data = os.path.join(input_data, 'log_data/*/*/*.json')

    # read in log data 
    df = spark.read.json(log_data)

# main function that runs the file with all functions, variables and data
def main():

    # run the process functions, define spark, input_data, output_data parameters

    spark = create_spark_session()
    input_data = 's3a://udacity-dend/'
    output_data = 'results'

    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)

if __name__ == "__main__":
    main()