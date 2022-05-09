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

# Container Setup

1. Pull the image from Docker Hub

```bash
docker pull amazon/aws-glue-libs:glue_libs_3.0.0_image_01
```