from scapy.all import *
import argparse
import sys
import platform

def get_working_iface():
    if platform.system() == "Windows":
        return conf.iface.name
    else:
        return conf.iface

def network_scan(interface, ip_range):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    packet = Ether(dst=broadcast_mac)/ARP(pdst=ip_range)
    
    try:
        print(f"Scanning IP range {ip_range} on interface {interface}...")
        answered, unanswered = srp(packet, timeout=2, iface=interface, inter=0.1, verbose=False)
        
        print(f"\nScan results for IP range {ip_range}:")
        for sent, received in answered:
            print(received.sprintf(r"%Ether.src% - %ARP.psrc%"))
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Network Scanner Tool")
    parser.add_argument("-i", "--interface", default=None, help="Network interface to use (default: auto-detect)")
    parser.add_argument("-r", "--range", required=True, help="IP range to scan (e.g., 192.168.1.0/24)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    if args.interface is None:
        args.interface = get_working_iface()
    
    print(f"Using interface: {args.interface}")
    
    try:
        network_scan(args.interface, args.range)
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
        sys.exit(0)