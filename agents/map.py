from tools import run_nmap, run_whatweb, run_dnsrecon, run_whois, run_gobuster, run_wapiti

task_tool_map = {
    "port_scan": run_nmap,
    "web_tech": run_whatweb,
    "dns_lookup": run_dnsrecon,
    "whois": run_whois,
    "dir_enum": run_gobuster,
    "vuln_scan": run_wapiti
}
