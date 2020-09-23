
Search
 
 
HTML CSS JavaScript jQuery PHP Bootstrap Google MySQL Image
HTML
Rainbow Text Generator
Select List Menu Generator
Select Option List Generator
Table Generator
Marquee Generator
Typing Animation Typewriter
Image SlideShow Generator
Website Copyright Generator
Show Hide Element Generator
Popup Window Generator
Page Redirect Generator
Mouseover Image Generator
iFrame Code Generator
Meta Tag Generator
Alert Message Generator
History Back Forward Button
Link Code Generator
HTML Code Decompressor
HTML Code Compressor
HTML Editor With Preview
HTML Online Editor
HTML To Javascript
HTML To Text
HTML Code Encryptor Decryptor
Color Code Color Names
Right Click,Text Select Disable code
HTML Codes
Country names Drop Down List
Currency name Drop Down List
Languages name Drop Down List
Year month date Drop Down List

 

 
HTML online editor
HTML online editor

3 Comments


 
  
Donate with PayPal button
3 comments
Leave a Reply
Name *
Email (will not be published) *
Website
Comment *
submit
HTML Editor
HTML Editor With Preview
HTML Online Editor
Tools
URL Decoder Encoder
HTML Code Decompressor
HTML Code Compressor
CSS Code Decompressor
CSS Code Compressor
JavaScript Code Compressor
JavaScript Code Decompressor

 
Converter
HTML To Javascript
HTML To Text
Letter Case Converter
Image To Data URI
Byte Converter
Web Tools
URL Extractor
Calculator
Online Age Calculator
Home | About | Contact | Terms of Use | Privacy Policy
Copyright © 2016 - 2020 www.html-code-generator.com

Formatting applied
Code ×
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

<h5><span style="color:#7f8c8d">For Macs or Linux:</span></h5>

<ul>
    <li><span style="color:#7f8c8d">Download Spark from&nbsp;</span><a href="https://spark.apache.org/downloads.html" rel="nofollow"><span style="color:#7f8c8d">https://spark.apache.org/downloads.html</span></a><span style="color:#7f8c8d">. Choose &quot;Prebuilt for Apache Hadoop 2.7 and later.&quot;</span></li>
    <li><span style="color:#7f8c8d">Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).</span></li>
    <li><span style="color:#7f8c8d">Download binary for Kafka from this location&nbsp;</span><a href="https://kafka.apache.org/downloads" rel="nofollow"><span style="color:#7f8c8d">https://kafka.apache.org/downloads</span></a><span style="color:#7f8c8d">, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you&rsquo;ll see the scripts to execute in&nbsp;<code>bin</code>&nbsp;folders, and config files under&nbsp;<code>config</code>&nbsp;folder. You&rsquo;ll need to modify&nbsp;<code>zookeeper.properties</code>&nbsp;and&nbsp;<code>server.properties</code>.</span></li>
    <li><span style="color:#7f8c8d">Download Scala from the official site, or for Mac users, you can also use&nbsp;<code>brew install scala</code>, but make sure you download version 2.11.x.</span></li>
    <li><span style="color:#7f8c8d">Run below to verify correct versions:</span>
    <pre>
<span style="color:#7f8c8d"><code>java -version
scala -version
</code></span></pre>
    </li>
    <li><span style="color:#7f8c8d">Make sure your ~/.bash_profile looks like below (might be different depending on your directory):</span>
    <pre>
<span style="color:#7f8c8d"><code>export SPARK_HOME=/Users/dev/spark-2.4.3-bin-hadoop2.7
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
export SCALA_HOME=/usr/local/scala/
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH
</code></span></pre>
    </li>
</ul>

<h5><span style="color:#7f8c8d">For Windows:</span></h5>

<p><span style="color:#7f8c8d">Please follow the directions found in this helpful StackOverflow post:&nbsp;</span><a href="https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows" rel="nofollow"><span style="color:#7f8c8d">https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows</span></a></p>

<p><a href="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" rel="noopener noreferrer" target="_blank"><span style="color:#7f8c8d"><img alt="" data-canonical-src="https://video.udacity-data.com/topher/2019/August/5d5198a2_screen-shot-2019-08-12-at-9.49.15-am/screen-shot-2019-08-12-at-9.49.15-am.png" src="https://camo.githubusercontent.com/8ee26710f6cf010112264f40b4e3e98c1e975ed1/68747470733a2f2f766964656f2e756461636974792d646174612e636f6d2f746f706865722f323031392f4175677573742f35643531393861325f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2f73637265656e2d73686f742d323031392d30382d31322d61742d392e34392e31352d616d2e706e67" style="width:452px" /></span></a></p>

<p><span style="color:#7f8c8d">SF Crime Data</span></p>

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

<h4><span style="color:#7f8c8d"><strong>Local Environment</strong></span></h4>

<ul>
    <li>
    <p><span style="color:#7f8c8d">Install requirements using&nbsp;<code>./start.sh</code>&nbsp;if you use conda for Python. If you use pip rather than conda, then use&nbsp;<code>pip install -r requirements.txt</code>.</span></p>
    </li>
    <li>
    <p><span style="color:#7f8c8d">Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.</span></p>
    </li>
</ul>

<p style="margin-left:80px"><span><span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace"><span style="color:#11161a"><span style="background-color:white">bin/zookeeper-server-start.sh config/zookeeper.properties</span></span></span></span></span></p>

<p style="margin-left:80px"><span><span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace"><span style="color:#11161a"><span style="background-color:white"><code>​​​​​bin/kafka-server-start.sh config/server.properties </code></span></span></span></span></span></p>

<ul>
    <li><span style="color:#7f8c8d">You can start the bootstrap server using this Python command:&nbsp;<code>python producer_server.py</code>.</span></li>
</ul>

<h4><strong>Workspace Environment</strong></h4>

<ul>
    <li>Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:
    <pre>
<span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace"><span style="color:#11161a"><span style="background-color:white">/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties
</span></span><span style="background-color:white"><em><span style="color:#11161a">/usr/bin/</span></em></span>kafka-server-start /etc/kafka/server.properties</span></span>
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

<p><span style="color:#7f8c8d"><strong>Local Environment</strong></span></p>

<ul>
    <li>
    <p><span style="color:#7f8c8d">To see if you correctly implemented the server, use the command&nbsp;</span></p>
    <span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace">bin/kafka-console-consumer.sh --bootstrap-server localhost:&lt;your-port-number&gt; --topic &lt;your-topic-name&gt; --from-beginning&nbsp;to see your output.</span></span></li>
</ul>

<h4><strong>Workspace Environment</strong></h4>

<ul>
    <li>Check what topics exist use this:&nbsp;</li>
</ul>

<p style="margin-left:80px"><code><span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace">/usr/bin/kafka-topics --list --zookeeper localhost:2181</span></span></code></p>

<ul>
    <li>To start kafka-consumer-console, use this command</li>
</ul>

<p><span style="margin-left:80px"><span style="font-size:12px"><span style="font-family:Courier New,Courier,monospace">kafka-console-consumer --bootstrap-server localhost:9092&nbsp;--topic com.sf.police.event.calls --from-beginning</span></span></span></p>

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
