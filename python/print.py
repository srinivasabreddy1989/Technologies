print("Hello, World!")
print('This is a Python print statement.')
print("You can print numbers too:", 42)
name = "srinivasa reddy B"
company = "Genpact india private limited"
print("My name is", name, "and I work at", company)
print(name)
print(company)
x = 10
y = 20
print(x)
print(y)
print("The sum of", x, "and", y, "is", x + y)
print(x + 20)
name1 = "Jenkins" #application name
status = "running" 
port = 8080 #jenkins port number
print(name1, status, port)
print("jenkins", "kubernetes", "docker", "ansible", sep="||")
print("===========================================================")
print("hello", end=" ")
print("world")
CPU = 75.263783637 # CPU usage in percentage
print(f"server: {name1}, status: {status}, CPU usage: {CPU}%")
print("===========================================================")
print(f"CPU Usage: {CPU:.2f}%")
servers = ["server1", "server2", "server3"]
print(servers)
for server in servers:
    print(f"Server: {server}")
print("==========================Dict=================================")
server = {
    "name": "jenkins",
    "status": "running",
    "port": 8080,
    "CPU": 75.263783637
}
print(server)
print(f"Server: {server['name']}")
print(f"Status: {server['status']}")
print(f"port: {server['port']}")
print(f"CPU Usage: {server['CPU']:.2f}%")
print("==========================Logging=================================")
# This is a simple example of logging in Python

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Jenkins server is UP")
logging.warning("Jenkins response is slow")
logging.error("Jenkins server is DOWN")

print("==========================Logging with format=================================")
import keyword
print("Python Keywords:")
print(keyword.kwlist)
for kw in keyword.kwlist:
    logging.info(f"Keyword: {kw}")
    
