#!/usr/bin/env python3
"""
Educational Network Monitor

This tool demonstrates basic network monitoring concepts for educational purposes.
Use only on systems you own or have explicit permission to monitor.

Author: RajputDDOS Educational Project
License: MIT (Educational Use Only)
"""

import time
import socket
import psutil
import argparse
from datetime import datetime


class NetworkMonitor:
    """Educational network monitoring class"""
    
    def __init__(self):
        self.start_time = datetime.now()
    
    def check_port(self, host, port, timeout=3):
        """Check if a port is open on a host"""
        try:
            socket.create_connection((host, port), timeout)
            return True
        except (socket.timeout, socket.error):
            return False
    
    def monitor_network_usage(self, duration=60):
        """Monitor network usage for educational purposes"""
        print(f"🔍 Starting network monitoring for {duration} seconds...")
        print("⚠️  Educational use only - ensure you have permission to monitor this network")
        print("-" * 60)
        
        start_stats = psutil.net_io_counters()
        start_time = time.time()
        
        while time.time() - start_time < duration:
            current_stats = psutil.net_io_counters()
            
            bytes_sent = current_stats.bytes_sent - start_stats.bytes_sent
            bytes_recv = current_stats.bytes_recv - start_stats.bytes_recv
            
            print(f"📊 Data sent: {bytes_sent:,} bytes | Data received: {bytes_recv:,} bytes")
            
            time.sleep(5)
        
        print("\n✅ Monitoring completed")
    
    def scan_common_ports(self, host, ports=None):
        """Educational port scanning example"""
        if ports is None:
            ports = [22, 23, 53, 80, 110, 443, 993, 995]
        
        print(f"🔍 Educational port scan of {host}")
        print("⚠️  Only use on systems you own or have permission to test")
        print("-" * 50)
        
        for port in ports:
            if self.check_port(host, port):
                print(f"✅ Port {port} is open")
            else:
                print(f"❌ Port {port} is closed/filtered")
    
    def display_system_info(self):
        """Display system information for educational purposes"""
        print("🖥️  System Information (Educational)")
        print("-" * 40)
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        print(f"Network Interfaces: {len(psutil.net_if_addrs())}")
        print(f"Active Network Connections: {len(psutil.net_connections())}")


def main():
    parser = argparse.ArgumentParser(
        description="Educational Network Monitor - For learning purposes only"
    )
    parser.add_argument("--host", default="127.0.0.1", 
                       help="Host to monitor (default: localhost)")
    parser.add_argument("--duration", type=int, default=30,
                       help="Monitoring duration in seconds (default: 30)")
    parser.add_argument("--scan", action="store_true",
                       help="Perform educational port scan")
    parser.add_argument("--monitor", action="store_true",
                       help="Monitor network usage")
    parser.add_argument("--info", action="store_true",
                       help="Display system information")
    
    args = parser.parse_args()
    
    monitor = NetworkMonitor()
    
    print("🎓 Educational Network Security Monitor")
    print("=" * 50)
    print("⚠️  WARNING: Educational use only!")
    print("   Only use on systems you own or have explicit permission to test.")
    print("   Unauthorized network scanning is illegal and unethical.")
    print("=" * 50)
    
    if args.info:
        monitor.display_system_info()
    
    if args.scan:
        response = input(f"\n🔒 Confirm you have permission to scan {args.host} (y/N): ")
        if response.lower() == 'y':
            monitor.scan_common_ports(args.host)
        else:
            print("❌ Scan cancelled - Authorization required")
    
    if args.monitor:
        response = input(f"\n🔒 Confirm you have permission to monitor network (y/N): ")
        if response.lower() == 'y':
            monitor.monitor_network_usage(args.duration)
        else:
            print("❌ Monitoring cancelled - Authorization required")
    
    if not any([args.scan, args.monitor, args.info]):
        print("\n📚 Available options:")
        print("  --info     Display system information")
        print("  --scan     Educational port scanning")
        print("  --monitor  Network usage monitoring")
        print("\nUse --help for more information")


if __name__ == "__main__":
    main()