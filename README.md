<h1>Project Overview</h1>

<p>In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you&#39;ve learned in this course to create a Kafka server to produce data and ingest data through Spark Structured Streaming.</p>

<p>You can try to answer the following questions with the dataset:</p>

<ul>
	<li>What are the top types of crimes in San Fransisco?</li>
	<li>What is the crime density by location?</li>
</ul>

<h3>Development Environment</h3>

<p>You may choose to create your project in the workspace we provide here, or if you wish to develop your project locally, you will need to set up your environment properly as described below:</p>

<ul>
	<li>Spark 2.4.3</li>
	<li>Scala 2.11.x</li>
	<li>Java 1.8.x</li>
	<li>Kafka build with Scala 2.11.x</li>
	<li>Python 3.6.x or 3.7.x</li>
</ul>

<h4><strong>Environment Setup (Only Necessary if You Want to Work on the Project Locally on Your Own Machine)</strong></h4>

<h5>For Macs or Linux:</h5>

<ul>
	<li>Download Spark from&nbsp;<a href="https://spark.apache.org/downloads.html" rel="nofollow">https://spark.apache.org/downloads.html</a>. Choose &quot;Prebuilt for Apache Hadoop 2.7 and later.&quot;</li>
	<li>Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).</li>
	<li>Download binary for Kafka from this location&nbsp;<a href="https://kafka.apache.org/downloads" rel="nofollow">https://kafka.apache.org/downloads</a>, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you&rsquo;ll see the scripts to execute in&nbsp;<code>bin</code>&nbsp;folders, and config files under&nbsp;<code>config</code>&nbsp;folder. You&rsquo;ll need to modify&nbsp;<code>zookeeper.properties</code>&nbsp;and&nbsp;<code>server.properties</code>.</li>
	<li>Download Scala from the official site, or for Mac users, you can also use&nbsp;<code>brew install scala</code>, but make sure you download version 2.11.x.</li>
	<li>Run below to verify correct versions:
	<pre>
<code>java -version
scala -version
</code></pre>
	</li>
	<li>Make sure your ~/.bash_profile looks like below (might be different depending on your directory):
	<pre>
<code>export SPARK_HOME=/Users/dev/spark-2.4.3-bin-hadoop2.7
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
export SCALA_HOME=/usr/local/scala/
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH
</code></pre>
	</li>
</ul>

<h5>For Windows:</h5>

<p>Please follow the directions found in this helpful StackOverflow post:&nbsp;<a href="https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows" rel="nofollow">https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows</a></p>

<p><a href="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" rel="nofollow"><img alt="" src="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" width="400" height="300"/></a></p>

<p>SF Crime Data</p>

<h1>Project Directions</h1>

<h2>Starter Code</h2>

<p>You can find three Python files that are starter code, the project dataset, and some other necessary resources in a zip file called &quot;SF Crime Data Project Files&quot; in the Resources tab in the left sidebar of your classroom:</p>

<ul>
	<li><code>producer_server.py</code></li>
	<li><code>kafka_server.py</code></li>
	<li><code>data_stream.py</code></li>
	<li><code>police-department-calls-for-service.json</code></li>
	<li><code>radio_code.json</code></li>
	<li><code>start.sh</code></li>
	<li><code>requirements.txt</code></li>
</ul>

<p>These files are also included in the Project Workspace.</p>

<h2>Files You Need to Edit in Your Project Work</h2>

<p>These starter code files should be edited:</p>

<ul>
	<li><code>producer_server.py</code></li>
	<li><code>data_stream.py</code></li>
	<li><code>kafka_server.py</code></li>
</ul>

<p>The following file should be created separately for you to check if your&nbsp;<code>kafka_server.py</code>&nbsp;is working properly:</p>

<ul>
	<li><code>consumer_server.py</code></li>
</ul>

<h2>Create a GitHub Repository</h2>

<p>Create a new repo that will contain all these files for your project. You will submit a link to this repo as a key part of your project submission. If you complete the project in the classroom workspace here, just download the files you worked on and add them to your repo.</p>

<h2>Beginning the Project</h2>

<p>This project requires creating topics, starting Zookeeper and Kafka servers, and your Kafka bootstrap server. You&rsquo;ll need to choose a port number (e.g., 9092, 9093..) for your Kafka topic, and come up with a Kafka topic name and modify the zookeeper.properties and server.properties appropriately.</p>

<h4><strong>Local Environment</strong></h4>

<ul>
	<li>
	<p>Install requirements using&nbsp;<code>./start.sh</code>&nbsp;if you use conda for Python. If you use pip rather than conda, then use&nbsp;<code>pip install -r requirements.txt</code>.</p>
	</li>
	<li>
	<p>Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.</p>
	</li>
</ul>

<pre style="margin-left:40px">
<code>bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
</code></pre>

<ul>
	<li>You can start the bootstrap server using this Python command:&nbsp;<code>python producer_server.py</code>.</li>
</ul>

<h4><strong>Workspace Environment</strong></h4>

<ul>
	<li>Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:
	<pre>
<code>
/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties
kafka-server-start /etc/kafka/server.properties
</code></pre>
	</li>
</ul>

<ul>
	<li>
	<p>You&rsquo;ll need to open up two terminal tabs to execute each command.</p>
	</li>
	<li>
	<p>Install requirements using the provided&nbsp;<code>./start.sh</code>&nbsp;script.&nbsp;<strong>This needs to be done every time you re-open the workspace, or anytime after you&#39;ve refreshed, or woken up, or reset data, or used the &quot;Get New Content&quot; button in this workspace.</strong></p>
	</li>
	<li>
	<p>In the terminal, to install other packages that you think are necessary to complete the project, use&nbsp;<code>conda install &lt;package_name&gt;</code>. You may need to reinstall these packages every time you re-open the workspace, or anytime after you&#39;ve refreshed, or woken up, or reset data, or used the &quot;Get New Content&quot; button in this workspace.</p>
	</li>
</ul>

<div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
<div class="">
<div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
<div class="repository-content ">
<div class="gutter-condensed gutter-lg flex-column flex-md-row d-flex">
<div class="flex-shrink-0 col-12 col-md-9 mb-4 mb-md-0">
<div id="readme" class="Box md js-code-block-container Box--responsive">
<div class="Box-body px-5 pb-5">
<article class="markdown-body entry-content container-lg">
<p>&nbsp;</p>
<h1><a id="user-content-step-1" class="anchor" href="https://github.com/fogofortitude/SF-Crime-Statistics-with-Spark#step-1" aria-hidden="true"></a>Step 1</h1>
<ul>
<li>The first step is to build a simple Kafka server.</li>
<li>Complete the code for the server in&nbsp;<code>producer_server.py</code>&nbsp;and&nbsp;<code>kafka_server.py</code>.</li>
</ul>
<p><span style="color: #808080;"><strong>Local Environment<br /></strong>To see if you correctly implemented the server, use the command below to see your output&nbsp;<code>
</code></span></p>
<blockquote>
<p><span style="color: #808080;"><code>bin/kafka-console-consumer.sh --bootstrap-server localhost:&lt;your-port-number&gt; --topic &lt;your-topic-name&gt; --from-beginning&nbsp;</code></span></p>
</blockquote>
<h4><a id="user-content-workspace-environment-1" class="anchor" href="https://github.com/fogofortitude/SF-Crime-Statistics-with-Spark#workspace-environment-1" aria-hidden="true"></a><strong>Workspace Environment</strong></h4>
<ul>
<li>setup the Udacity Workspace
<blockquote>./start.sh</blockquote>
</li>
<li>started the zookeeper server
<blockquote>/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties</blockquote>
</li>
<li>start the kafka server<br />
<blockquote>kafka-server-start /etc/kafka/server.properties</blockquote>
</li>
<li>Create Topic <br />
<blockquote><code>kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic com.sf.police.event.calls</code></blockquote>
</li>
<li>Checked the topic "com.sf.police.event.calls" now exists<br />
<blockquote>/usr/bin/kafka-topics --list --zookeeper localhost:2181</blockquote>
</li>
<li>Run kafka-console-producer with Dummy JSON values<br />
<blockquote>kafka-console-producer --broker-list localhost:9092 --topic com.sf.police.event.calls</blockquote>
<blockquote>
<p><em>{ "crime_id": "183653763", "original_crime_type_name": "Traffic Stop", "report_date": "2018-12-31T00:00:00.000","call_date": "2018-12-31T00:00:00.000","offense_date": "2018-12-31T00:00:00.000","call_time": "23:57","call_date_time": "2018-12-31T23:57:00.000","disposition": "ADM","address": "Geary Bl/divisadero St","city": "San Francisco","state": "CA","agency_id": "1","address_type": "Intersection","common_location": "" }</em></p>
<p><em>{"crime_id":"183653745","original_crime_type_name":"Audible Alarm","report_date":"2018-12-31T00:00:00.000","call_date":"2018-12-31T00:00:00.000","offense_date":"2018-12-31T00:00:00.000","call_time":"23:47","call_date_time":"2018-12-31T23:47:00.000","disposition":"PAS","address":"1900 Block Of 18th Av","city":"San Francisco","state":"CA","agency_id":"1","address_type":"Premise Address","common_location":""}</em></p>
 <p><em>{"crime_id":"183653706","original_crime_type_name":"Passing Call","report_date":"2018-12-31T00:00:00.000","call_date":"2018-12-31T00:00:00.000","offense_date":"2018-12-31T00:00:00.000","call_time":"23:34","call_date_time":"2018-12-31T23:34:00.000","disposition":"Not recorded","address":"1500 Block Of Haight St","city":"San Francisco","state":"CA","agency_id":"1","address_type":"Common Location","common_location":"Haight St Corridor, Sf"}
   </em></p>
  </blockquote>
<li><span style="background-color: #ccffcc;"><span style="color: #008000;"><strong>TIP:</strong> use this to tool to convert multiline JSON layout to single line</span> https://tools.knowledgewalls.com/online-multiline-to-single-line-converter</span></li>
<li>Run kafka-console-consumer
<blockquote><code>kafka-console-consumer --bootstrap-server localhost:9092 --topic com.sf.police.event.calls --from-beginning</code></blockquote>
</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>

<p><strong>Sample Kafka Consumer Console Output (Screenshot)</strong></p>
	<p><img src="https://github.com/fogofortitude/SF-Crime-Statistics-with-Spark/blob/master/STEP-1-Output/step1-kafka-console-producer-results.PNG" alt="file" width="500" height="300" />&nbsp;</p>
<code></code></article>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer container-xl width-full p-responsive" role="contentinfo">
<div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">&nbsp;</div>
<div class="d-flex flex-justify-center pb-6">&nbsp;</div>
</div>


<h2>Step 2</h2>

<ul>
	<li>Apache Spark already has an integration with Kafka brokers, so we would not normally need a separate Kafka consumer. However, we are going to ask you to create one anyway. Why? We&#39;d like you to create the consumer to demonstrate your understanding of creating a complete Kafka Module (producer and consumer) from scratch. In production, you might have to create a dummy producer or consumer to just test out your theory and this will be great practice for that.</li>
	<li>Implement all the TODO items in&nbsp;<code>data_stream.py</code>. You may need to explore the dataset beforehand using a Jupyter Notebook.</li>
	<li>Do a spark-submit using this command:&nbsp;<code>spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py</code>.</li>
	<li>Take a screenshot of your progress reporter after executing a Spark job.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
	<li>Take a screenshot of the Spark Streaming UI as the streaming continues.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
	Run the following to view Spark UI
	<blockquote> wget "http://localhost:3000" </blockquote>
</ul>

<h2>Step 3</h2>
<ol>
<li>
<p><strong> did changing values on the SparkSession property parameters affect the throughput and latency of the data?</strong></p>
<ul>
<li>Yes, altering them impacted Time it Tooks to Complete Jobs / Tasks</li>
<li>Altering the number of cores used ie master("local[*]") had the most significant impact. It seemed that by reducing the number of cores reduced the processing of the 200 Tasks I had it process. This I believe may have been the result of reduced Shuffle Read and Shuffle Write.&nbsp;</li>
<li>Altering maxRatePerPartition and&nbsp;maxOffsetsPerTrigger also seemed to affect throughput and latency.&nbsp;</li>
</ul>
</li>
<li>
<p><strong>What were the 2-3 most efficient SparkSession property key/value pairs?&nbsp;</strong><strong>Through testing multiple variations on values, how can you tell these were the most optimal?</strong></p>
<table style="width: 275.333px;">
<tbody>
<tr>
<td style="width: 151px;"><strong>Property</strong></td>
<td style="width: 27px;"><strong>Value</strong></td>
<td style="width: 85.3333px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 151px;">maxRatePerPartition</td>
<td style="width: 27px;">10</td>
<td style="width: 85.3333px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 151px;">maxOffsetsPerTrigger</td>
<td style="width: 27px;">100</td>
<td style="width: 85.3333px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 151px;">master</td>
<td style="width: 27px;">local[1]</td>
<td style="width: 85.3333px;">&nbsp;</td>
</tr>
</tbody>
</table>
</li>
</ol>
<p style="padding-left: 30px;">From looking at Sparks Web UI - Executors Tab it was evident from looking at the following columns:&nbsp;</p>
<table style="width: 205px; margin-left: 30px;">
<tbody style="padding-left: 30px;">
<tr style="padding-left: 30px;">
<td style="width: 153px; padding-left: 30px;"><strong>Column</strong></td>
</tr>
<tr style="padding-left: 30px;">
<td style="width: 153px; padding-left: 30px;">Task Time</td>
</tr>
<tr style="padding-left: 30px;">
<td style="width: 153px; padding-left: 30px;">Shuffle Read</td>
</tr>
<tr style="padding-left: 30px;">
<td style="width: 153px; padding-left: 30px;">Shuffle Write</td>
</tr>
</tbody>
</table>
<p style="padding-left: 30px;">The screenshots show the differences in performance between two separate Spark Session configurations</p>
<p style="padding-left: 30px;">&nbsp;<strong>Screenshot 2 - Spark Session Properties</strong></p>
<table style="margin-left: 30px;">
<tbody>
<tr>
<td><strong>Property</strong></td>
<td><strong>Value</strong></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>maxRatePerPartition</td>
<td>100</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>maxOffsetsPerTrigger</td>
<td>200</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>master</td>
<td>local[*]</td>
<td style="padding-left: 30px;">&nbsp;</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

<p><img src="https://github.com/fogofortitude/SF-Crime-Statistics-with-Spark/blob/master/STEP-2-Output/Config_v1/less_optimal.png" alt="file" width="500" height="300" />&nbsp;</p>

<p style="padding-left: 30px;">&nbsp;<strong>Screenshot 2 - Spark Session Properties</strong></p>
<table style="margin-left: 30px;">
<tbody>
<tr>
<td><strong>Property</strong></td>
<td><strong>Value</strong></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>maxRatePerPartition</td>
<td>10</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>maxOffsetsPerTrigger</td>
<td>100</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>master</td>
<td>local[1]</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>

<p><img src="https://github.com/fogofortitude/SF-Crime-Statistics-with-Spark/blob/master/STEP-2-Output/config_v2/more_optimal.png" alt="file" width="500" height="300" />&nbsp;</p>

<p style="padding-left: 30px;">&nbsp;</p>
<p style="padding-left: 30px;">&nbsp;</p>
