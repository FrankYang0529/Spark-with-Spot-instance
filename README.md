# Spark-with-Spot-instance
This is the python script which use spark_ec2.py in Spark to automatize.

## Document
First you have to movie spot-script.py to /spark and then run with python2.7.

### AWS_ACCESS_KEY_ID & AWS_SECRET_KEY_ID
You can get AWS_ACCESS_KEY_ID and AWS_SCRET_KEY_ID from [Security Credentials](https://console.aws.amazon.com/iam/home?#home)

### Key pair name & Key file direction
You can get key pair from amazon ec2.

Example:
    key file direction: /Users/frank/test-ec2.pem
    key pair name: test-ec2

### Slave number
Type an integer which mean how many slave you want.

### zone
Type a zone where you want to launch your spot instance.

Example:
    zone: us-east-1b

### Spot price
Type an float which mean the max price you want to launch instance.

### Cluster name
Type a cluster name which you want.

Example:
    cluster name: test

### Program name
Type the program name which you want to run on spot instance.

Example:
    program name: premovie.py

### Program file direction
Type the program file direction which you put program file on local.

Example:
    program file direction: /Users/frank/premovie.py
