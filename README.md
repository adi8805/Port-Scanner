
# 🔍 Python Port Scanner

A **multi-threaded port scanner** written in Python that supports **service detection** and **banner grabbing** for open ports.  
Lightweight, fast, and customizable for scanning small or large port ranges.

---

## 📌 Features
- 🚀 **Multi-threaded** scanning for speed (default: 100 threads)
- 🛠 **Customizable port range** and timeout
- 🔎 **Service detection** using built-in socket functions
- 📰 **Banner grabbing** for basic version detection
- 🎡 **Spinner animation** during scanning for progress indication

---

## 📥 Installation

Ensure you have **Python 3.7+** installed.

```bash
git clone https://github.com/adi8805/Port-Scanner
cd python-port-scanner
````

---

## ⚡ Usage

```bash
Usage: python3 scanner.py <target> -p- <start_port> <end_port> [--threads N] [--timeout S]
```

### **Examples**

1. **Basic scan** for ports 1–1000:
    
    ```bash
    python3 scanner.py 192.168.1.10 -p- 1 1000
    ```
    
2. **Scan with custom thread count and timeout:**
    
    ```bash
    python3 scanner.py example.com -p- 20 500 --threads 200 --timeout 2
    ```
    
3. **Display usage help:**
    
    ```bash
    python3 scanner.py --help
    ```
    
4. **Show version:**
    
    ```bash
    python3 scanner.py --version
    ```
    

---

## 🖥 Expected Output

When scanning, you’ll see a spinner animation until results appear:

```text
[*] Scanning ports 20 to 100 on 192.168.1.10...

Scanning... /
Scanning... |
Scanning... -

[+] Port 22 is open - Service: ssh - Banner: OpenSSH_8.2
[+] Port 80 is open - Service: http
[+] Port 443 is open - Service: https
Scanning... done!
```

---

## ⚙️ Arguments

|Argument|Description|Default|
|---|---|---|
|`<target>`|Target IP address or hostname|_Required_|
|`-p- <start> <end>`|Port range to scan|_Required_|
|`--threads N`|Number of concurrent threads|100|
|`--timeout S`|Timeout for each connection (seconds)|1|
|`--help`|Show help message|-|
|`--usage`|Show usage example|-|
|`--version`|Show program version|-|

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, make your changes, and submit a pull request.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
Unauthorized scanning of networks that you don't own or have permission to test may be **illegal**.

```

Would you like me to tailor this README with a **badges section** (like Python version, license, etc.) for a more professional look?
```
