import docker
import os

def get_docker_client():
    """
    Create and return a Docker client instance.
    """
    try:
        client = docker.from_env()
        return client
    except docker.errors.DockerException as e:
        print(f"Error connecting to Docker: {e}")
        return None
    

def run_nmap(ip : str, client: docker.DockerClient) -> str:
    """
    Run nmap scan on the given IP address and return the output.
    """
    try:
        check_if_up = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["nmap", "-sn", ip],
            network_mode="host",
            remove=True,
            detach=False,
            stdout=True,
            stderr=True
        )
        if "Host is up" not in check_if_up.decode('utf-8'):
            return f"Host {ip} is not reachable or does not exist."
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["nmap","-Pn","-sV", "-T4", "-p-", ip],
            network_mode="host",
            remove=True,
            detach=False,
            stdout=True,
            stderr=True
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"
    
    
def run_whois(domain : str, client : docker.DockerClient) -> str:
    """
    Run whois lookup on the given domain and return the output.
    """
    try:
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["whois", domain],
            network_mode="host",
            remove=True,
            detach=False,
            stdout=True,
            stderr=True
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"
    
    
def run_dnsrecon(domain : str, client : docker.DockerClient) -> str :
    """
    Run DNS reconnaissance on the given domain and return the output.
    """
    try:
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["sh", "-c", f"dnsrecon -d {domain} -t std 2>&1"],
            network_mode="host",
            remove=True,
            detach=False
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"

def run_whatweb(url : str, client : docker.DockerClient) -> str:
    """
    Run WhatWeb on the given URL and return the output.
    """
    try:
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["sh", "-c", f"whatweb --color=never -v {url} 2>&1"],
            network_mode="host",
            remove=True,
            detach=False
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"

def run_gobuster(url: str, client: docker.DockerClient) -> str:
    """
    Run Gobuster on the given URL and return the output.
    """
    try:
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            ["gobuster", "dir", "-u", url, "-w", "/wordlists/common.txt"],
            network_mode="host",
            remove=True,
            detach=False
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"


def run_wapiti(url: str, client: docker.DockerClient) -> str:
    """
    Run Wapiti on the given URL and return the output.
    """
    try:
        output = client.containers.run(
            os.getenv("DOCKER_IMAGE"),
            [
                "sh", "-c",
                f"mkdir -p /tools/report && "
                f"wapiti -u {url} -f txt &&"
                f"cat $(find . -name '*.txt' | head -n 1)"
            ],
            network_mode="host",
            remove=True,
            detach=False
        )
        return output.decode('utf-8')
    except docker.errors.ContainerError as e:
        return f"Container error: {e}"
    except docker.errors.DockerException as e:
        return f"Docker error: {e}"
