# Assignment-6
# Hadoop Streaming API for Dataset Analysis <br/>
<br/>
The following commands are required to run the analysis after cloning the python files into CS Cloud <br/>
<br/>
* Basic MapReduce Recipe (Python) cmdline:

hadoop jar  /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/nyc/nyc-traffic.csv -output /users-cloud-16fs/kaneca(your username)/output/job1-out(any file name) -mapper ~/mapper.py -reducer ~/reducer.py -file ~/{mapper,reducer}.py
<br/> <br/>
* To view the output file: <br/>
hdfs dfs -cat /users-cloud-16fs/kaneca(your username)/output/job1-out(same file name as above)/part-00000
