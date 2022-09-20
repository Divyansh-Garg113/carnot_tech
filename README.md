Hi, welcome to the devops assignment. Below are the details like technologies used, files in the repository, etc. which are necessary for evaluation of problems 1 to 6.

There are currently 5 files in the repository:
1. README.md
2. devops_assignment.py : Python file (for the code deployed on EC2 instance for problems 1 and 2)
3. requirments.txt: file that contains dependencies necessary for python code.
4. serverless_devops_assignment.py : Python file (for the code deployed on serverless(Lambda) probem 6)
5. buildspec.yml : file for AWS CodeDely which is the CI/CD solution for Problem 6.

**Technologies:**
This module describes the technologies used to achieve goals for problems 1 to 6.

Problem 1: 
1. Server configuration: t2.micro
2. Monitor and run the python application : Supervisor process manager
3. CI/CD : Jenkins (hosted on another instance in same VPC)
4. Trigger : Github Webhooks
5. Trigger condition : Push to main branch
6. python file: devops_assignment.py

Problem 6:
1. Serverless solution: AWS Lambda 
2. CI/CD : AWS CodeBuild
3. Trigger : Github Webhook(configured in CodeBuild configurations)
4. Trigger condition : Push to main branch
5. python file: serverless_devops_assignment.py


**Problem 1. Access EC2 server remotely to check logs and code:**

	To access the required path, first login to the remote server using ssh.

	a) ssh into remote EC2 server:
  
	  $ ssh cornet_tech@35.154.158.70

	**The default username:** cornet_tech	
	**EC2 instance password:** provided in a word document attached with the email.
	**EC2 instance public IP:** 35.154.158.70


	b) Path of application code: /app/carnot_tech/

	c) Path of server logs: /var/log/supervisor/devops_assignment.log
       		$ tail -f /var/log/supervisor/devops_assignment.log

	d) Check the uptime of python application
      		 $ supervisorctl status devops_assignment

**Problem 3.** To Monitor the health of server
	1. CloudWatch monitoring can be used to check essential matrix associated with server like health-check, CPU utilization, Memory, network in/out, etc.
	2.  


**Problem 4.** A few precautions that must be taken in order to ensure server is healthy and running 24x7.
	1. Configure Health Check alarms for EC2 instance.
	2. Configure server matrix level alerts (like CPU utilization, Memory, Network, 5xx errors, etc.) and dashboards in the monitoring and alerting solutions.
	3. Configure email notifications when CI/CD pipeline failed due to any reason.
	4. In case of web-servers like apache/Nginx, web-hooks can be configured to trigger emails when a particular threshold is breached.
	5. All EC2 machines are prone to hardware or network failures. To minimize downtime in such case, run the server behing a LoadBalancer and attach an auto-scaling policy. In case server is unhealthy, it can be replaced with a healthy server to minimize the downtime.

**Problem 5.** In case of SOS,
	1. I will first check the server matrics like CPU, Memory, I/O, etc. It will give a rough estimate of the time when the actual outage started.
	2. There are cases when current server configurations are less than required by the application. Then, we can upgrade the instance type to handle the load.
	3. Then, I will login to server and check the application status as well as application logs to investigate the issue.  
	4. In case of issue with application, then provide an appropriate patch, restart the service and then analyse it's status.
	4. If issue is from hardware side, provision a new server in backend with same configurations and route all incoming traffic to new server. Ensure new server is running as expected. Then investigate the issue by analysiing server logs and service logs in original server.
	5. To avoid such cases, an AutoScaling group must be configured to ensure a healthy server is up and available when such issues occur.
	
**Problem 6: Deploy application on serverless with CI/CD enabled** 
	The trigger for CI/CD pipeline is push event in Github repository.
	Primary Source Webhook Event is enabled in CodeBuild project. Hence, when a file is modified in the repo, CodeBuild project is triggered and the service is deployed on AWS Lambda.
	Note: Timeout in AWS Lambda is set to 2min 10sec. Hence, the given python code will terminate after Timeout. As a result, the print statement in the code will be printed only 2 times in AWS Lambda Logs (a screenshot is attached with the email for reference).  
