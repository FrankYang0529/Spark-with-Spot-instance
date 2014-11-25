#!/usr/bin/env python
# encoding: utf-8

import subprocess

print ("Must start in spark direction !")
access_key = raw_input('Please input your AWS_ACCESS_KEY_ID: ')
access_secret_key = raw_input('Please input your AWS_SECRET_ACCESS_KEY: ')
key_pair = raw_input('Please input your key pair name: ')
key_file_dir = raw_input('Please input your key file direction: ')
slave_num = raw_input('Please input slave number: ')
zone = raw_input('Please input zone which you want to launch: ')
spot_price = raw_input('Please input spot instance price: ')
cluster_name = raw_input('Please input your cluster name: ')
program_name = raw_input('Please input your program name: ')
program_file_dir = raw_input('Please input your program file direction: ')

print ("Start !")

subprocess.call("AWS_ACCESS_KEY_ID={} AWS_SECRET_ACCESS_KEY={} \
                 ./ec2/spark-ec2 -k {} -i {} -s {} --spot-price={} --zone={} launch {}"\
                 .format(access_key, access_secret_key, key_pair, key_file_dir, slave_num, spot_price, zone, cluster_name), shell=True)

output = subprocess.check_output("AWS_ACCESS_KEY_ID={} AWS_SECRET_ACCESS_KEY={} \
                                  ./ec2/spark-ec2 -k {} -i {} get-master {}"\
                                  .format(access_key, access_secret_key, key_pair, key_file_dir, cluster_name), shell=True)
host = output.split()[-1]
subprocess.call("scp -i {} {} root@{}:/root/"\
                 .format(key_file_dir, program_file_dir, host), shell=True)

proc = subprocess.Popen("ssh -i {} root@{}"\
                         .format(key_file_dir, host), shell=True,stdin=subprocess.PIPE)
# proc = subprocess.Popen("AWS_ACCESS_KEY_ID=AKIAI5VHNNPWZIWFPDEQ AWS_SECRET_ACCESS_KEY=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 ./spark/ec2/spark-ec2 -k test-ec2 -i /Users/yangpoan/test-ec2.pem login frank", shell=True, stdin=subprocess.PIPE)
proc.stdin.write("./spark-ec2/copy-dir /root/{}".format(program_name))
proc.communicate()
proc.stdin.close()

proc = subprocess.Popen("ssh -i {} root@{}".format(key_file_dir, host), shell=True,stdin=subprocess.PIPE)
proc.stdin.write("AWS_ACCESS_KEY_ID={} AWS_SECRET_ACCESS_KEY={} \
                  ./spark/bin/pyspark {}".format(access_key, access_secret_key, program_name))
proc.communicate()
proc.stdin.close()

subprocess.call("AWS_ACCESS_KEY_ID={} AWS_SECRET_ACCESS_KEY={} \
                 ./ec2/spark-ec2 -k {} -i {} destroy {}"\
                 .format(access_key, access_secret_key, key_pair, key_file_dir, cluster_name), shell=True)
