# report/summarizer.py

PORT_SCAN_SUMMARY_PROMPT = """
You are a cybersecurity expert.

Summarize the following Nmap scan output. Highlight:
- Any open ports and their associated services
- The purpose or risk of these services
- Any anomalies or suspicious services
- Omit closed/filtered ports unless relevant

Raw Output:
"""

WEB_TECH_SUMMARY_PROMPT = """
You are a cybersecurity analyst.

Summarize the results of a WhatWeb scan. Include:
- Web server type and version
- CMS/frameworks detected (e.g., WordPress, Django)
- JavaScript libraries or other technologies
- Any outdated or insecure components

Raw Output:
"""

DNS_LOOKUP_SUMMARY_PROMPT = """
You are a DNS security analyst.

Summarize the DNSRecon output. Include:
- Name servers and their IPs
- MX (mail) records
- Recursion or DNSSEC issues
- Any unusual subdomains or findings

Raw Output:
"""

WHOIS_SUMMARY_PROMPT = """
You are a cybersecurity investigator.

Summarize the WHOIS data. Focus on:
- Registrar and creation/expiry dates
- Contact or organization info (if available)
- Suspicious or privacy-shielded data
- Any indicators of legitimacy or risk

Raw Output:
"""

DIR_ENUM_SUMMARY_PROMPT = """
You are an ethical hacker.

Summarize the Gobuster output. Include:
- Discovered directories or files
- Potential sensitive endpoints (e.g., /admin, /backup)
- Any hints about technologies or misconfigurations

Raw Output:
"""

VULN_SCAN_SUMMARY_PROMPT = """
You are a vulnerability analyst.

Summarize the Wapiti report. Include:
- Vulnerabilities detected and their type (e.g., XSS, SQLi)
- Severity levels (if available)
- Affected endpoints
- Any recommendations if implied

Raw Output:
"""