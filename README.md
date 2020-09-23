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

<h4>Environment Setup (Only Necessary if You Want to Work on the Project Locally on Your Own Machine)</h4>

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

<p><a href="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" rel="noopener noreferrer" target="_blank"><img alt="" data-canonical-src="https://video.udacity-data.com/topher/2019/August/5d5198a2_screen-shot-2019-08-12-at-9.49.15-am/screen-shot-2019-08-12-at-9.49.15-am.png" src="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" style="width:452px" /></a></p>

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

<h4><span style="color:#95a5a6"><strong>Local Environment</strong></span></h4>

<ul>
    <li>
    <p><span style="color:#95a5a6">Install requirements using&nbsp;<code>./start.sh</code>&nbsp;if you use conda for Python. If you use pip rather than conda, then use&nbsp;<code>pip install -r requirements.txt</code>.</span></p>
    </li>
    <li>
    <p><span style="color:#95a5a6">Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.</span></p>

    <ul>
        <li>
        <pre>
<span style="font-family:Courier New,Courier,monospace"><span style="color:#95a5a6"><code>bin/zookeeper-server-start.sh config/zookeeper.properties
​​​​​bin/kafka-server-start.sh config/server.properties
</code></span></span></pre>
        </li>
    </ul>
    </li>
    <li><span style="color:#95a5a6">You can start the bootstrap server using this Python command:&nbsp;<code>python producer_server.py</code>.</span></li>
</ul>

<h4><strong>Workspace Environment</strong></h4>

<ul>
    <li>Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:
    <pre>
<span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace"><span style="color:#11161a"><span style="background-color:white"><em>/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties
</em></span></span><span style="background-color:white"><em><span style="color:#11161a">/usr/bin/</span></em></span>kafka-server-start /etc/kafka/server.properties</span></span>
</pre>
    </li>
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

<h2>Step 1</h2>

<ul>
    <li>The first step is to build a simple Kafka server.</li>
    <li>Complete the code for the server in&nbsp;<code>producer_server.py</code>&nbsp;and&nbsp;<code>kafka_server.py</code>.</li>
</ul>

<h4><strong><span style="color:#999999">Local Environment</span></strong></h4>

<ul>
    <li><span style="color:#999999">To see if you correctly implemented the server, use the command&nbsp;</span>

    <ul>
        <li><span style="color:#999999">bin/kafka-console-consumer.sh --bootstrap-server localhost:&lt;your-port-number&gt; --topic &lt;your-topic-name&gt; --from-beginning&nbsp;to see your output.</span></li>
    </ul>
    </li>
</ul>

<h4><strong>Workspace Environment</strong></h4>

<ul>
    <li>Check what topics exist use this:&nbsp;
    <ul>
        <li><code><span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace">/usr/bin/kafka-topics --list --zookeeper localhost:2181</span></span></code></li>
    </ul>
    </li>
    <li>To start kafka-consumer-console, use this command
    <ul>
        <li><span style="font-family:Courier New,Courier,monospace"><span style="font-size:12px"><code>/usr/bin/kafka-consumer-console&nbsp;--topic com.sf.police.event.calls --from-beginning</code></span></span></li>
    </ul>
    </li>
</ul>

<p><strong>Take a screenshot of your kafka-consumer-console output. You will need to include this screenshot as part of your project submission.</strong></p>

<p><a href="https://camo.githubusercontent.com/aef6753be130a0dd9e6002030f7c97c5d163c7bb/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531396266635f73637265656e2d73686f742d323031392d30382d31322d61742d31302e30332e34312d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d31302e30332e34312d616d2e706e67" rel="noopener noreferrer" target="_blank"><img alt="" data-canonical-src="https://video.udacity-data.com/topher/2019/August/5d519bfc_screen-shot-2019-08-12-at-10.03.41-am/screen-shot-2019-08-12-at-10.03.41-am.png" src="https://camo.githubusercontent.com/aef6753be130a0dd9e6002030f7c97c5d163c7bb/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531396266635f73637265656e2d73686f742d323031392d30382d31322d61742d31302e30332e34312d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d31302e30332e34312d616d2e706e67" style="width:441px" /></a></p>

<p><strong>Sample Kafka Consumer Console Output</strong></p>

<h2>Step 2</h2>

<ul>
    <li>Apache Spark already has an integration with Kafka brokers, so we would not normally need a separate Kafka consumer. However, we are going to ask you to create one anyway. Why? We&#39;d like you to create the consumer to demonstrate your understanding of creating a complete Kafka Module (producer and consumer) from scratch. In production, you might have to create a dummy producer or consumer to just test out your theory and this will be great practice for that.</li>
    <li>Implement all the TODO items in&nbsp;<code>data_stream.py</code>. You may need to explore the dataset beforehand using a Jupyter Notebook.</li>
    <li>Do a spark-submit using this command:&nbsp;<code>spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py</code>.</li>
    <li>Take a screenshot of your progress reporter after executing a Spark job.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
    <li>Take a screenshot of the Spark Streaming UI as the streaming continues.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
</ul>

<h2>Step 3</h2>

<p>Write the answers to these questions in the README.md doc of your GitHub repo:</p>

<ol>
    <li>
    <p>How did changing values on the SparkSession property parameters affect the throughput and latency of the data?</p>
    </li>
    <li>
    <p>What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?</p>
    </li>
</ol>
