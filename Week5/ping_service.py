###Task 1
### Q1: command: python ping_service.py 172.18.0.1; cat /etc/passwd 
### Q2: Possibility to input special characters such as " ' ; -- ' enables code injection after the input. The lack of whitelist input validation.
### Q3: It is possible to fix the problem with proper input requirements/validations
### Q4: Implementation of input sanitizer with regex sub to take out characters that aren't needed for IP address.
### Q5: It is not possible to know if injection is possible anymore or not since there isn't such thing as "silver bullet".

import argparse
import subprocess
import re

def ping_device(target):
    sanitized_target = re.sub(r'[0-9.]', '', target)
    command = f"ping -c 4 {sanitized_target}"
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {sanitized_target}\n{e.output.decode()}")

def main():
    parser = argparse.ArgumentParser(description="Ping a device. WARNING: This tool is vulnerable to command injection.")
    parser.add_argument("target", type=str, help="IP address or DNS name of the target device")
    args = parser.parse_args()
    ping_device(args.target)

if __name__ == "__main__":
    main()