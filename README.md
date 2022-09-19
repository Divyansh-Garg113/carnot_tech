Access EC2 server remotely to check logs and code:

To access the required path, first login to the remote server using ssh.

	a) ssh into remote EC2 server:
  
	  $ ssh cornet_tech@35.154.158.70

**The default username:** cornet_tech
**EC2 instance public IP:** 35.154.158.70

	b) Path of application code: /app/carnot_tech/

	c) Path of server logs: /var/log/supervisor/devops_assignment.log
       $ tail -f /var/log/supervisor/devops_assignment.log

	d) Check the uptime of script
       $ supervisorctl status devops_assignment


2. Public Github repository: https://github.com/Divyansh-Garg113/carnot_tech
	There are currently 3 files in the repository:
	1. README.md
	2. devops_assignment.py : Python file
	3. requirments.txt: file that contains dependencies necessary for python code.


3. To Monitor the health of server
	1. CloudWatch monitoring can be used to check essential matrix associated with server like health-check, CPU utilization, Memory, network in/out, etc.
	2. 


4. A few precautions that must be taken in order to ensure server is healthy and running 24x7.
	1. Configure Health Check alarms on AWS console.
	2. Configure server matrix level alerts (like CPU utilization, Memory, Network, 5xx errors, etc.) and dashboards in the monitoring and alerting solutions.
	3. Configure email notifications when CI/CD pipeline failed due to any reason. 
	4. All EC2 machines are prone to hardware or network failures. To minimize downtime in such case, run the server behing a LoadBalancer and attach an auto-scaling policy. In case server is unhealthy, it can be replaced with a healthy server to minimize the downtime.

5. In case of SOS,
	1. I will check the server matrics to identify the affected matrix.
	2. Then, I will check the application status as well as logs on server to find the issue.
	3. In case of issue with service, then provide the appropriate patch and restart the service.
	4. If issue is from hardware side, provision a new server in backend with same configurations and route all incoming traffic to new server. Ensure new server is running as expected. Then investigate the issue by analysiing server logs and service logs in original server.
	5. To avoid such cases, an AutoScaling group must be configured to ensure a healthy server is upand listening when such issues occur.
	6. To avoid such incidents, move the application to either serverless architecture or dockerised environment - Kubernetes where autoscaling is handled automatically by Kubernetes. 
	
