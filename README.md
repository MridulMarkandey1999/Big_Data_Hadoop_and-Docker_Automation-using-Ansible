# Big_Data_Hadoop_and-Docker_Automation-using-Ansible
The project was developed during 
**Industrial Training on Machine Learning using Python, Big Data Hadoop,Automation using Ansible (DevOps), Redhat Linux and AWS Cloud.**

The project aims at developing a market-ready web service for RHEL clients which aims to provide client means for DevOps. 

The project is python implementation of a number of technologies, like hadoop to setup hdfs and storage clusters for big data analytics, Machine learning for to build face  recognition system for authentication  and Dockers. 

The entire configuration requirement was met by creating Ansible playbooks. 

The software is entirely controlled through our voice.

## Prerequisites:

1. You should have any RHEL version installed in your system because the server will run on RHEL.(Recommended is RHEL-7.5 or RHEL-8)

2. You should have Anaconda installed in your system. If you don't have then you can download it from this link:
    https://www.anaconda.com/distribution/


3. You should have openCV installed in your system. If you don't have then you can download it from here
    https://pypi.org/project/opencv-contrib-python/

4. You should have Ansible package installed in RHEL Virtual Machine.

5. You must specify the hosts file, which contains a list of all IP's along with their hostname.( Required in Hadoop cluster)

6. You must have **speechrecognition** and **pyaudio** python libraries pre-installed in your windows. This is required so that the client can control the system through his voice.

7. There should be proper connectivity bewteen **RHEL VM (server)** and **Windows (client)**. Try to ping each other using IP address just to make sure there is no chance of error. Both server and client must be pingable.

8. Replace the IP address in both **server.py** and **client.py** with the IP address of server.

9. You must have python3 installed in your system. (In both windows and RHEL VM)

## How to RUN:

1. Download or clone the complete repository. 

2. Copy **server.py** , **reps repository** , **bin repository** to RHEL VM which will be our server.

3. Copy **client.py** to windows which will be the client side code.

4.  First execute **server.py**.( IN RHEL VM )
    
    $python3 server.py
    
5. Then execute **client.py**.( IN WINDOWS )

   $python3 client.py

6. Speak out any of the commands:

   Let's say : Show me the date 
   
   It will display date as output
   
   Let's say: Can you setup Hadoop for me
   
   output: All hadoop configurations will be done and NameNode and DataNode setup  will be done automatically in few seconds. So in this    way **hadoop Storage Cluster and Computational Cluster will be setup in few seconds** 
   
   **NOTE: You can also configure Docker using this as well. So in this way, only by your voice, the complex task can be automated using            Ansible.
 
 ## WOW-FACTOR:
 
 **For this your camera and remote system camera must be connected to the system. The remote system, server and all the networking     devices must be in the same network**
 
 if you say:
 Hey can you click photograph for me
 
 Output: It will ask for IP address
 
 After entering IP Address manually, it will go to that remote system
 
 Open their camera on its own, click their photograph and interestingly that photograph is hosted on a website automatically.
 
 So finally it'll return me with link, a **WEB-URL** of the website which contains that photograph. 
 
 And you can even access that website through your mobile phone's browser.
 
 
 
 **So if you like this project, or you have some suggestions then you can contact me through email: mridul.mark@gmail.com**
   
