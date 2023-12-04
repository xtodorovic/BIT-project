import subprocess

def nmap_probe(target, options):
    # Construct the Nmap command
    nmap_command = ["nmap", target] + options

    # Run the Nmap command
    try:
        result = subprocess.run(nmap_command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stderr)

if __name__ == "__main__":
    # Default options for a TCP SYN scan (-sS), and with service version detection (-sV)
    options = ["-sS", "-sV"]

    # Prompt the user for the target IP
    target_ip = input("\nEnter the target IP address or a domain: ")

    # Prompt the user for the ports to scan
    print("Scan all ports or only the most common 100?")
    print("1. All ports")
    print("2. 100 most common ports")
    choice = input("Enter the option number (e.g. 1 or 2): ")
    if choice == "2":
        options += ["-F"]
    elif choice != "1":
        print("Invalid option. Exiting.")
        exit(1)
    # Prompt the user for the scan speed
    print("\nSelect scan speed:")
    print("0. Paranoid (Every 5 minutes each probe - Not detected by IDS/IPS)")
    print("1. Slow (15 seconds between probes)")
    print("2. Polite (Scan slower than normal)")
    print("3. Normal (Scan at the default rate)")
    print("4. Agressive (Scan faster than normal)")
    print("5. Insane (Scan as fast as possible - Easily detected by IDS/IPS)")
    speed = "-T" 
    choice = input("Enter the speed option (e.g., 0, 1, 2, etc.): ")
    if int(choice) > 5 and int(choice) < 0:
        print("Invalid option. Exiting.")
        exit(1)
    speed += choice
    options += [speed]
    # Prompt the user for scan options
    print("\nSelect option:")
    print("1. Packet Fragmentation")
    print("2. Decoy Scan")
    print("3. Spoofed source IP address")
    print("4. Spoofed source port")
    print("5. MTU manipulation")
    print("6. TCP SYN scan (stealthy)")
    print("7. Version detection")

    # Get user choice
    choice = input("Enter the option number (e.g., 1, 2, etc.): ")

    # Process user choice
    if choice == "1":
        options += ["-f"]  # Packet Fragmentation
    elif choice == "2":
        decoy_ip = input("Enter decoy IP address (comma-separated if multiple): ")
        options += ["-D", decoy_ip]  # Decoy Scan
    elif choice == "3":
        source_ip = input("Enter spoofed source IP address: ")
        options += ["-S", source_ip]  # Spoof source IP address
        options += ["-e", "eth0", "-Pn"]
    elif choice == "4":
        source_port = input("Enter spoofed source port: ")
        options += ["--source-port", source_port]  # Spoof source port
    elif choice == "5":
        size = input("Enter MTU size: ")
        options += ["--mtu", size]  # Scanning Timing
    elif choice == "6":
        options.pop(1)
    elif choice == "7":
        options.pop(0)
    else:
        print("Invalid option. Exiting.")
        exit(1)

    # Run the Nmap scan
    print("Performing scan...")
    print(options)
    nmap_probe(target_ip, options)
