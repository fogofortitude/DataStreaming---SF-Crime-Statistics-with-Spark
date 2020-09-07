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
