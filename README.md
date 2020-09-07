<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="project-overview">Project Overview</h2>
<p>In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data and ingest data through Spark Structured Streaming.</p>
<p>You can try to answer the following questions with the dataset:</p>
<ul>
<li>What are the top types of crimes in San Fransisco?</li>
<li>What is the crime density by location?</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h3 id="development-environment">Development Environment</h3>
<p>You may choose to create your project in the workspace we provide here, or if you wish to develop your project locally, you will need to set up your environment properly as described below:</p>
<ul>
<li>Spark 2.4.3</li>
<li>Scala 2.11.x</li>
<li>Java 1.8.x</li>
<li>Kafka build with Scala 2.11.x</li>
<li>Python 3.6.x or 3.7.x</li>
</ul>
<h4 id="environment-setup-only-necessary-if-you-want-to-work-on-the-project-locally-on-your-own-machine-">Environment Setup (Only Necessary if You Want to Work on the Project Locally on Your Own Machine)</h4>
<h5 id="for-macs-or-linux-">For Macs or Linux:</h5>
<ul>
<li>Download Spark from&nbsp;<a href="https://spark.apache.org/downloads.html" target="_blank" rel="noopener">https://spark.apache.org/downloads.html</a>. Choose "Prebuilt for Apache Hadoop 2.7 and later."</li>
<li>Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).</li>
<li>Download binary for Kafka from this location&nbsp;<a href="https://kafka.apache.org/downloads" target="_blank" rel="noopener">https://kafka.apache.org/downloads</a>, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you&rsquo;ll see the scripts to execute in&nbsp;<code>bin</code>&nbsp;folders, and config files under&nbsp;<code>config</code>&nbsp;folder. You&rsquo;ll need to modify&nbsp;<code>zookeeper.properties</code>&nbsp;and&nbsp;<code>server.properties</code>.</li>
<li>Download Scala from the official site, or for Mac users, you can also use&nbsp;<code>brew install scala</code>, but make sure you download version 2.11.x.</li>
<li>Run below to verify correct versions:
<pre><code>java -<span class="hljs-property">version</span>
scala -<span class="hljs-property">version</span>
</code></pre>
</li>
<li>Make sure your ~/.bash_profile looks like below (might be different depending on your directory):
<pre><code><span class="hljs-built_in">export</span> SPARK_HOME=/Users/dev/spark-<span class="hljs-number">2.4</span>.<span class="hljs-number">3</span>-bin-hadoop2.<span class="hljs-number">7</span>
<span class="hljs-built_in">export</span> JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.<span class="hljs-number">8.0</span>_181.jdk/Contents/Home
<span class="hljs-built_in">export</span> SCALA_HOME=/usr/<span class="hljs-built_in">local</span>/scala/
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$JAVA_HOME</span>/bin:<span class="hljs-variable">$SPARK_HOME</span>/bin:<span class="hljs-variable">$SCALA_HOME</span>/bin:<span class="hljs-variable">$PATH</span>
</code></pre>
</li>
</ul>
<h5 id="for-windows-">For Windows:</h5>
<p>Please follow the directions found in this helpful StackOverflow post:&nbsp;<a href="https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows" target="_blank" rel="noopener">https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows</a></p>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div>
<div class="image-atom--image-atom--1XDdu" tabindex="0" role="button" aria-label="Show Image Fullscreen">
<div class="image-atom-content--CDPca">
<div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/August/5d5198a2_screen-shot-2019-08-12-at-9.49.15-am/screen-shot-2019-08-12-at-9.49.15-am.png" alt="" width="452px" /></div>
<div class="caption--2IK-Y">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<p>SF Crime Data</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="starter-code">Starter Code</h2>
<p>You can find three Python files that are starter code, the project dataset, and some other necessary resources in a zip file called "SF Crime Data Project Files" in the Resources tab in the left sidebar of your classroom:</p>
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
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="files-you-need-to-edit-in-your-project-work">Files You Need to Edit in Your Project Work</h2>
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
<h2 id="create-a-github-repository">Create a GitHub Repository</h2>
<p>Create a new repo that will contain all these files for your project. You will submit a link to this repo as a key part of your project submission. If you complete the project in the classroom workspace here, just download the files you worked on and add them to your repo.</p>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="beginning-the-project">Beginning the Project</h2>
<p>This project requires creating topics, starting Zookeeper and Kafka servers, and your Kafka bootstrap server. You&rsquo;ll need to choose a port number (e.g., 9092, 9093..) for your Kafka topic, and come up with a Kafka topic name and modify the zookeeper.properties and server.properties appropriately.</p>
<h4 id="local-environment">Local Environment</h4>
<ul>
<li>
<p>Install requirements using&nbsp;<code>./start.sh</code>&nbsp;if you use conda for Python. If you use pip rather than conda, then use&nbsp;<code>pip install -r requirements.txt</code>.</p>
</li>
<li>
<p>Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.</p>
<pre><code>bin/zookeeper-server-<span class="hljs-operator"><span class="hljs-keyword">start</span>.sh config/zookeeper.properties
<span class="hljs-keyword">bin</span>/kafka-<span class="hljs-keyword">server</span>-<span class="hljs-keyword">start</span>.sh config/<span class="hljs-keyword">server</span>.properties</span>
</code></pre>
</li>
<li>You can start the bootstrap server using this Python command:&nbsp;<code>python producer_server.py</code>.</li>
</ul>
<h4 id="workspace-environment">Workspace Environment</h4>
<ul>
<li>Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:
<pre><code>/usr/bin/zookeeper-server-<span class="hljs-operator"><span class="hljs-keyword">start</span> zookeeper.properties
/usr/<span class="hljs-keyword">bin</span>/kafka-<span class="hljs-keyword">server</span>-<span class="hljs-keyword">start</span> producer.properties</span>
</code></pre>
</li>
<li>
<p>You&rsquo;ll need to open up two terminal tabs to execute each command.</p>
</li>
<li>
<p>Install requirements using the provided&nbsp;<code>./start.sh</code>&nbsp;script.&nbsp;<strong>This needs to be done every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.</strong></p>
</li>
<li>
<p>In the terminal, to install other packages that you think are necessary to complete the project, use&nbsp;<code>conda install &lt;package_name&gt;</code>. You may need to reinstall these packages every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.</p>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="step-1">Step 1</h2>
<ul>
<li>The first step is to build a simple Kafka server.</li>
<li>Complete the code for the server in&nbsp;<code>producer_server.py</code>&nbsp;and&nbsp;<code>kafka_server.py</code>.</li>
</ul>
<h4 id="local-environment">Local Environment</h4>
<ul>
<li>To see if you correctly implemented the server, use the command&nbsp;<code>bin/kafka-console-consumer.sh --bootstrap-server localhost:&lt;your-port-number&gt; --topic &lt;your-topic-name&gt; --from-beginning</code>&nbsp;to see your output.</li>
</ul>
<h4 id="workspace-environment">Workspace Environment</h4>
<ul>
<li>To start kafka-consumer-console, use the command&nbsp;<code>/usr/bin/kafka-consumer-console</code>.</li>
</ul>
<p><strong>Take a screenshot of your kafka-consumer-console output. You will need to include this screenshot as part of your project submission.</strong></p>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div>
<div class="image-atom--image-atom--1XDdu" tabindex="0" role="button" aria-label="Show Image Fullscreen">
<div class="image-atom-content--CDPca">
<div class="image-and-annotations-container--1U01s"><img class="image--26lOQ" src="https://video.udacity-data.com/topher/2019/August/5d519bfc_screen-shot-2019-08-12-at-10.03.41-am/screen-shot-2019-08-12-at-10.03.41-am.png" alt="" width="441px" /></div>
<div class="caption--2IK-Y">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<p><strong>Sample Kafka Consumer Console Output</strong></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="step-2">Step 2</h2>
<ul>
<li>Apache Spark already has an integration with Kafka brokers, so we would not normally need a separate Kafka consumer. However, we are going to ask you to create one anyway. Why? We'd like you to create the consumer to demonstrate your understanding of creating a complete Kafka Module (producer and consumer) from scratch. In production, you might have to create a dummy producer or consumer to just test out your theory and this will be great practice for that.</li>
<li>Implement all the TODO items in&nbsp;<code>data_stream.py</code>. You may need to explore the dataset beforehand using a Jupyter Notebook.</li>
<li>Do a spark-submit using this command:&nbsp;<code>spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py</code>.</li>
<li>Take a screenshot of your progress reporter after executing a Spark job.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
<li>Take a screenshot of the Spark Streaming UI as the streaming continues.&nbsp;<strong>You will need to include this screenshot as part of your project submission.</strong></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="step-3">Step 3</h2>
<p>Write the answers to these questions in the README.md doc of your GitHub repo:</p>
<ol>
<li>
<p>How did changing values on the SparkSession property parameters affect the throughput and latency of the data?</p>
</li>
<li>
<p>What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?</p>
</li>
</ol>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h3 id="project-submission">Project Submission</h3>
<p>You will submit a link to your GitHub repo, with the files you've created:&nbsp;<code>producer_server.py</code>,&nbsp;<code>kafka_server.py</code>,&nbsp;<code>data_stream.py</code>, and&nbsp;<code>consumer_server.py</code>. The README.md doc in your GitHub repo should contain your responses to the two questions from Step 3.</p>
<p>Your project submission should also include a zip file containing the three screenshots you've taken.</p>
</div>
</div>
</div>
</div>
</div>
