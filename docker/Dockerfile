FROM debian:latest

RUN apt-get update && apt-get install -y \
    nmap dnsrecon whatweb wapiti gobuster whois curl\
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /wordlists \
  && curl -fsSL \
       https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt \
       -o /wordlists/common.txt


WORKDIR /tools

ENTRYPOINT ["sh", "-c", "exec \"$@\"", "--"]