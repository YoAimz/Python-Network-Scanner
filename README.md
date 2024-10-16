# Python Network Scanner

A simple, network scanning tool written in Python using Scapy. This tool allows you to easily scan IP ranges to discover active hosts on your network. (cross-platform)

## Features

- Cross-platform compatibility (Windows and Linux)
- Customizable IP range scanning
- Automatic network interface detection
- Easy-to-use command-line interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Scapy library
- Npcap (for Windows users)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YoAimz/Python-Network-Scanner.git
   cd Python-Network-Scanner/networkScanner
   ```

2. Install the required dependencies:
   - For Windows:
     ```
     pip install scapy[complete]
     ```
   - For Linux:
     ```
     pip install scapy
     ```

3. Windows users: Download and install Npcap from [https://npcap.com/](https://npcap.com/)

## Usage

Run the script with the following command:

```
python networkScanner.py -r <IP_RANGE>
```

Replace `<IP_RANGE>` with the IP range you want to scan, for example:

```
python networkScanner.py -r 192.168.1.0/24
```

To specify a network interface, use the `-i` or `--interface` option:

```
python networkScanner.py -i eth0 -r 192.168.1.0/24
```

For help and to see all available options:

```
python networkScanner.py --help
```

## Note

Please ensure you have permission to scan the network you're targeting. Unauthorized network scanning may be illegal or against network usage policies in many contexts.


## Acknowledgements

- [Scapy](https://scapy.net/) - The powerful Python-based interactive packet manipulation program & library.

