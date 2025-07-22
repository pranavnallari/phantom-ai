# 🛡️ Phantom — Cyber Reconnaissance Tool

**Phantom** is a modular, intelligent cybersecurity reconnaissance framework designed for streamlined scanning of IPs, domains, and URLs. Powered by Dockerized tools and LLM agents, it automates common recon workflows into a structured report — making it ideal for red teamers, bug bounty hunters, or students building deep skills in cybersecurity.

---

## 🚀 Features

- 🔍 **URL, Domain, and IP Intelligence**
- 🧠 **Task Inference with LLMs** — detects what actions to take from user input
- 🧰 **Dockerized Tools** — isolates scanning logic for reliability & portability
- 🧾 **Auto-generated Markdown Reports** — complete with summaries & raw outputs
- 🧩 **Composable Graph Execution** via LangGraph for clean control flow
- 🤖 **LLM-powered Summarization** of each tool's output

---

## 🔧 Tools Used

| Task             | Tool        |
|------------------|-------------|
| Port Scanning    | `nmap`      |
| Web Tech Fingerprinting | `whatweb` |
| DNS Recon        | `dnsrecon`  |
| WHOIS Lookup     | `whois`     |
| Directory Enum   | `gobuster`  |
| Vulnerability Scan | `wapiti` |

All tools are installed in a custom **Debian-based Docker image**.

---

## 🧠 Architecture

Phantom is structured into modular agents using **LangGraph**:


Each stage is powered by an **LLM agent** and contributes tool output to the final report.

---

## 📄 Sample Output

Reports are generated as `.md` files and include:

- Tool summaries
- Raw command outputs
- Security insights
- Final recommendations

---

## 🛠️ Getting Started

### 1. Clone and Set Up
```bash
git clone https://github.com/pranavnallari/phantom-ai.git
cd phantom
```

### 2. Build Docker Image
```bash
docker build -t phantom-tools -f docker/Dockerfile .
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run a Scan
```bash
python main.py
```

You'll be prompted to enter an input like:

```text
Scan this website: https://example.com for vulnerabilities and directories.
```

Phantom will:
- Parse the input
- Decompose it
- Run relevant tools
- Generate a report in `./reports/`

---

## 🧱 Tech Stack

- Python 3.10+
- LangChain + LangGraph
- Docker (Debian-based)
- LLM backend (Ollama or other local/remote models)
- Rich Markdown generation

---

## ⚠️ Disclaimer

**For educational purposes only.** Always get permission before scanning live systems.

---
