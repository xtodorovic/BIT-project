# Nmap Probe Script

## Introduction

This Python script is designed to facilitate Nmap scans with customizable options. It prompts the user for various parameters such as the target IP, scan type, scan speed, and additional scan options.

## Requirements

- Python 3.x
- Nmap installed on your system

## Usage

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/xtodorovic/nmap-probe.git
    cd nmap-probe
    ```

2. Run the script.

    ```bash
    python nmap_probe.py
    ```

3. Follow the on-screen prompts to configure your Nmap scan.

4. Review the generated Nmap command and results.

## Options

### Default Scan Type

- **TCP SYN Scan (`-sS`):** Stealthy scan that sends SYN packets to discover open ports.
- **Service Version Detection (`-sV`):** Attempts to determine the service version running on open ports.

### Port Selection

- **All Ports:** Scan all ports on the target.
- **Common Ports (100):** Scan the 100 most common ports.

### Scan Speed

- **Paranoid:** Slow scan with a delay of 5 minutes between probes.
- **Slow:** 15 seconds delay between probes.
- **Polite:** Slower than normal scan.
- **Normal:** Default scan rate.
- **Aggressive:** Faster than normal scan.
- **Insane:** As fast as possible (may be easily detected by IDS/IPS).

### Additional Options

1. **Packet Fragmentation (`-f`):** Enable packet fragmentation.
2. **Decoy Scan (`-D`):** Send decoy packets to confuse IDS/IPS.
3. **Spoofed Source IP Address (`-S`):** Set spoofed source IP address.
4. **Spoofed Source Port (`--source-port`):** Set spoofed source port.
5. **MTU Manipulation (`--mtu`):** Set the Maximum Transmission Unit (MTU) size.
6. **TCP SYN scan (stealthy) (`-sS`):** A stealthy scan using TCP SYN packets to discover open ports.
7. **Version detection (`-sV`):** Scan attempting to determine the service version running on open ports.

## Example

```bash
python nmap_probe.py
```
Follow the on-screen prompts to customize your scan. For instance:

Target IP: 192.168.1.1 or domain
Port Selection: 1 (All Ports)
Scan Speed: 2 (Polite)
Select Option: 2 (Decoy Scan) - Enter decoy IP addresses, or for random enter **RND:{n}**, where n is the number of random addresses.

The script will generate and execute the corresponding Nmap command and display the results.