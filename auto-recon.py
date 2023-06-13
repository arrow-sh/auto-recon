# Tool Developed By: ArrowXDev (https://www.github.com/arrowxdev)
# Tool used: host, ping, nmap
import os

# example of IP/URL
print("example of IP: 127.0.0.1")
print("example of URL: localhost.com")
print("-"*100)

# grab the input from user
ip=input("[+] Enter the targeted IP/URL: ")
os.system(f"clear")
print("Starting recon on your targeted IP/URL",ip)
print("-"*100)

# ping the targeted ip
print("HOST INFORMATION :")
print(" ")
os.system(f"host {ip}")
print("-"*100)
print("PING INFORMATION :")
print(" ")
os.system(f"ping -c 5 {ip}")
print("-"*100)

# scan the open ports
print("NMAP SCAN INFORMATION :")
print(" ")
os.system(f"sudo nmap -sV -sC -T4 -p- -v {ip}")
print("-"*100)
    
# complete the auto recon
print(f"Your {ip} auto-recon is completed")
print("-"*100)