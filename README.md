# Setup-Glue-Locally
Developing AWS Glue ETL jobs locally

# Concepts
## AWS Glue
AWS Glue  is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue provides all the capabilities needed for data integration so that you can start analyzing your data and put it to use in minutes instead of months. AWS Glue provides both visual and code-based interfaces to make data integration easier. Users can easily find and access data using the AWS Glue Data Catalog. Data engineers and ETL (extract, transform, and load) developers can visually create, run, and monitor ETL workflows with a few clicks in AWS Glue Studio. Data analysts and data scientists can use AWS Glue DataBrew to visually enrich, clean, and normalize data without writing code. With AWS Glue Elastic Views, application developers can use familiar Structured Query Language (SQL) to combine and replicate data across different data stores.

AWS Glue consists of a Data Catalog which is a central metadata repository; an ETL engine that can automatically generate Scala or Python code; a flexible scheduler that handles dependency resolution, job monitoring, and retries; AWS Glue DataBrew for cleaning and normalizing data with a visual interface; and AWS Glue Elastic Views, for combining and replicating data across multiple data stores. Together, these automate much of the undifferentiated heavy lifting involved with discovering, categorizing, cleaning, enriching, and moving data, so you can spend more time analyzing your data.

Learn more here [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)

# How do I develop on AWS Glue

When you develop and test your AWS Glue job scripts, there are multiple available options:

AWS Glue Studio console

- Visual editor
- Script editor
- AWS Glue Studio notebook

Interactive sessions

- Jupyter notebook

Docker image

- Local development
- Remote development

AWS Glue Studio ETL library
- Local development

You can choose any of the above options based on your requirements.

If you prefer no code or less code experience, the AWS Glue Studio visual editor is a good choice.

If you prefer an interactive notebook experience, AWS Glue Studio notebook is a good choice. For more information, see Using Notebooks with AWS Glue Studio and AWS Glue. If you want to use your own local environment, interactive sessions is a good choice. For more information, see Using Interactive Sessions with AWS Glue.

If you prefer local/remote development experience, the Docker image is a good choice. This helps you to develop and test Glue job script anywhere you prefer without incurring AWS Glue cost.

If you prefer local development without Docker, installing the AWS Glue ETL library directory locally is a good choice.

# How to Start?

Make sure that Docker is installed and the Docker daemon is running. For installation instructions, see the Docker documentation for Mac, Windows, or Linux. The machine running the Docker hosts the AWS Glue container. Also make sure that you have at least 7 GB of disk space for the image on the host running the Docker.

For more information about restrictions when developing AWS Glue code locally, see Local Development Restrictions.

There are the following Docker images available for AWS Glue on Docker Hub.

- For AWS Glue version 3.0: amazon/aws-glue-libs:glue_libs_3.0.0_image_01
- For AWS Glue version 2.0: amazon/aws-glue-libs:glue_libs_2.0.0_image_01

These images are for x86_64.

## Container Setup

1. Pull the image from Docker Hub

```python
docker pull amazon/aws-glue-libs:glue_libs_3.0.0_image_01
```
## Run your container

2. Run the container

The general format of the run command is:

```docker
docker run -itd -p <port_on_host>:<port_on_container_either_8888_or_8080> -p 4040:4040 <credential_setup_to_access_AWS_resources> --name <container_name> amazon/aws-glue-libs:glue_libs_3.0.0_image_01 <command_to_start_notebook_server>
```

The code includes the following information:

<port_on_host> – The local port of your host that is mapped to the port of the container. For our use case, the container port is either 8888 (for a Jupyter notebook) or 8080 (for a Zeppelin notebook). To keep things simple, we use the same port number as the notebook server ports on the container in the following examples.

<port_on_container_either_8888_or_8080> – The port of the notebook server on the container. The default port of Jupyter is 8888; the default port of Zeppelin is 8080.
4040:4040 – This is required for SparkUI. 4040 is the default port for SparkUI. For more information, see Web Interfaces.

<credential_setup_to_access_AWS_resources> – In this section, we go with the typical case of mounting the host’s directory, containing the credentials. We assume that your host has the credentials configured using aws configure. The flow chart in the Appendix section explains various ways to set the credentials if the assumption doesn’t hold for your environment.

<container_name> – The name of the container. You can use any text here.
amazon/aws-glue-libs:glue_libs_1.0.0_image_01 – The name of the image that we pulled in the previous step.

<command_to_start_notebook_server> – We run /home/zeppelin/bin/zeppelin.sh for a Zeppelin notebook and /home/jupyter/jupyter_start.sh for a Jupyter notebook. If you want to run your code against the CLI interpreter, you don’t need a notebook server and can leave this argument blank.

Run Spark in your container:

```docker
$ docker run -it -v ~/.aws:/home/glue_user/.aws -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name glue_pyspark amazon/aws-glue-libs:glue_libs_3.0.0_image_01 pyspark
```

3. Run the following script (/scripts/src/sample.py):

```python
from pyspark import SparkContext
from operator import add
 
data = sc.parallelize(list("Hello World"))
counts = data.map(lambda x: 
	(x, 1)).reduceByKey(add).sortBy(lambda x: x[1],
	 ascending=False).collect()

print("Hello World")
for (word, count) in counts:
    print("{}: {}".format(word, count))
```

The result should look like this:

```console
Hello World


l: 3
o: 2
r: 1
H: 1
e: 1
W: 1
d: 1
```

4. To run a script directly in your container use the following command:

```console
docker run -it -v ~/.aws:/home/glue_user/.aws -v $WORKSPACE_LOCATION:/home/glue_user/workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name glue_spark_submit amazon/aws-glue-libs:glue_libs_3.0.0_image_01 spark-submit /home/glue_user/workspace/src/$SCRIPT_FILE_NAME
````

The result should look like:

```console
--------------------------------------------- Script Start -----------------------------------------
Hello World
l: 3
o: 2
r: 1
H: 1
e: 1
W: 1
d: 1
 : 1
--------------------------------------------- Script End ------------------------------------------
```

5. Run the following code to starts a Jupyter notebook: 

- Read-only credentials from a Mac or Linux host:

```docker
docker run -itd -p 8888:8888 -p 4040:4040 -v ~/.aws:/root/.aws:ro --name glue_jupyter amazon/aws-glue-libs:glue_libs_3.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh
```

- Read-write credentials from a Windows host:

```docker
docker run -itd -p 8888:8888 -p 4040:4040 -v %UserProfile%\.aws:/root/.aws:rw --name glue_jupyter amazon/aws-glue-libs:glue_libs_3.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh
```

You can now run the following command to make sure that the container is running:

```docker
docker ps
```

The following example code is the docker run command without the notebook server startup:

```docker
docker run -itd -p 8888:8888 -p 4040:4040 -v ~/.aws:/root/.aws:ro --name glue_jupyter amazon/aws-glue-libs:glue_libs_1.0.0_image_01
```

Log into your container

```docker
docker exec -it glue_jupyter bash
```

6. Open your notebook

If your client and host are the same machine, enter the following URL for Jupyter: https://127.0.0.1:8888/lab.

You can write PySpark code in the notebook as shown here. You can also use SQL magic (%%sql) to directly write SQL against the tables in the AWS Glue Data Catalog. If your catalog table is on top of JSON data, you have to place json-serde.jar in the /home/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8/jars directory of the container and restart the kernel in your Jupyter notebook. You can place the jar in this directory by first running the bash shell on the container using the following command:

If you have a local directory that holds your notebooks, you can mount it to /home/jupyter/jupyter_default_dir using the -v option. These notebooks are available to you when you open the Jupyter notebook URL. For example, see the following code:

```docker
docker run -itd -p 8888:8888 -p 4040:4040 -v ~/.aws:/root/.aws:ro -v C:\Users\admin\Documents\notebooks:/home/glue_user/jupyter/jupyter_default_dir --name glue_jupyter amazon/aws-glue-libs:glue_libs_3.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh
```