#!/usr/bin/env python3
import socket # Allows python to communicate over computer networks(like the internet), we use this to check if a network port is open
import concurrent.futures # Allows python to run multiple tasks at the same time while multi-threading
import argparse # Allows python to parse command line arguments
import sys # Gives python access to system functions like exit() or print()errors
import time # Deals with timing, delays and pauses.
import threading # Runs seperate lightweight tasks at the same time, used for the spinner animation so it doesn't block port scanning.

VERSION = "1.0"

# Spinner animation control
spinner_running = False

def spinner_animation():
    spinner = ['|', '/', '-', '\\']
    idx = 0
    while spinner_running:
        print(f"Scanning... {spinner[idx % len(spinner)]}", end='\r')
        time.sleep(0.1)
        idx += 1
    print("Scanning... done!   ")

# we use to reveal their service name
def grab_banner(ip, port, timeout=1):
    """Attempt to grab banner from service by connecting and recv data."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            try:
                banner = s.recv(1024).decode(errors='ignore').strip()
                return banner if banner else "No banner"
            except socket.timeout:
                return "No banner"
            except Exception:
                return "No banner"
    except Exception:
        return None

# it checks one port that port is open or not
def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                try:
                    service_name = socket.getservbyport(port, 'tcp')
                except OSError:
                    service_name = "Unknown"
                banner = grab_banner(ip, port, timeout)
                if banner is None or banner == "No banner":
                    print(f"[+] Port {port} is open - Service: {service_name}")
                else:
                    print(f"[+] Port {port} is open - Service: {service_name} - Banner: {banner}")
    except Exception:
        pass  # Silent fail

# Runs many scan_ports like 1000 ports at a time in parallel and keep animation going
def scan_ports(ip, start_port, end_port, max_threads=100, timeout=1):
    global spinner_running

    print(f"[*] Scanning ports {start_port} to {end_port} on {ip}...\n")

    # Start spinner animation thread
    spinner_running = True
    spinner_thread = threading.Thread(target=spinner_animation)
    spinner_thread.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(scan_port, ip, port, timeout=timeout))
        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            pass

    # Stop spinner animation
    spinner_running = False
    spinner_thread.join()

# Handle command line arguments
# Handles help, usage, version, and port range
# Star scanning by calling scan_ports()
def main():
    parser = argparse.ArgumentParser(
        description="Simple Python Port Scanner with Service Version (banner grabbing)",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )

    parser.add_argument("target", nargs="?", help="Target IP address or hostname")
    parser.add_argument("-p-", nargs=2, type=int, metavar=("START", "END"),
                        help="Port range to scan (e.g., -p- 1 800)")
    parser.add_argument("--threads", type=int, default=100, help="Max concurrent threads (default: 100)")
    parser.add_argument("--timeout", type=int, default=1, help="Timeout per connection in seconds")
    parser.add_argument("--help", action="store_true", help="Show help message and exit")
    parser.add_argument("--usage", action="store_true", help="Show usage example and exit")
    parser.add_argument("--version", action="store_true", help="Show program version and exit")

    args = parser.parse_args()

    if args.help:
        print("Usage: python3 scanner.py <target> -p- <start_port> <end_port> [--threads N] [--timeout S]\n")
        parser.print_help()
        sys.exit(0)

    if args.usage:
        print("Example:\n  python3 scanner.py 192.168.1.10 -p- 1 800 --threads 200 --timeout 1")
        sys.exit(0)

    if args.version:
        print(f"Python Port Scanner v{VERSION}")
        sys.exit(0)

    if not args.target or not args.p_:
        print("Error: Target and port range required.\nUse --help for more info.")
        sys.exit(1)

    target_ip = args.target
    start_port, end_port = args.p_
    scan_ports(target_ip, start_port, end_port, max_threads=args.threads, timeout=args.timeout)

if __name__ == "__main__":
    main()
