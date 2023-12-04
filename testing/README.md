# Testing Folder

## Introduction

This testing folder contains pcap files generated from various Nmap scans. These scans were conducted for educational purposes, and the pcap files serve as a record of the network traffic during the scans. All scans were performed on a target **scanme.nmap.org**, which has destination IP: 45.33.32.156. 

## Recorded Scenarios

### Scenario 1: TCP SYN Scan

- **Description:** A stealthy scan using TCP SYN packets to discover open ports.
- **File:** `tcp_syn_scan.pcapng`

### Scenario 2: Service Version Detection

- **Description:** Scan attempting to determine the service version running on open ports.
- **File:** `service_version_detection.pcapng`

### Scenario 3: Decoy Scan

- **Description:** Scan with decoy packets to confuse IDS/IPS.
- **File:** `decoy_scan.pcapng`

### Scenario 4: Spoofed Source IP Address

- **Description:** Scan with a spoofed source IP address.
- **File:** `spoofed_source_ip.pcapng`

### Scenario 5: Spoofed Source Port

- **Description:** Scan with a spoofed source port.
- **File:** `spoofed_source_port.pcapng`

### Scenario 6: Packet Fragmentation

- **Description:** Scan with packet fragmentation enabled.
- **File:** `packet_fragmentation.pcapng`

### Scenario 7: MTU Manipulation

- **Description:** Scan with Maximum Transmission Unit (MTU) manipulation.
- **File:** `mtu_manipulation.pcapng`

## Usage

These pcap files can be analyzed using tools such as Wireshark. The recorded scenarios provide insights into the network traffic patterns during the respective Nmap scans.

1. Download and install Wireshark: [Wireshark Download](https://www.wireshark.org/download.html)
2. Open Wireshark.
3. Load the desired pcap file to analyze.

## Disclaimer

These pcap files were recorded in a controlled and ethical environment for educational and testing purposes. It is crucial to use network scanning tools responsibly and with proper authorization. Unauthorized scanning can violate terms of service and legal agreements.

## Caution

If you plan to use these pcap files for testing on a live network or with an Intrusion Detection System (IDS), ensure that you have the appropriate authorization and are compliant with legal requirements.

---

Feel free to adjust the content to better match your specific use case, intentions, and the scenarios you recorded.
