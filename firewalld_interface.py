#!/usr/bin/env python3

import subprocess

# Displays initial menu options
def display_menu():
    # Displays 50 equal signs for formatting
    print("=" * 50)
    print("firewalld interface - markmental\n")
    print("1. Allow incoming traffic to a port (runtime)")
    print("2. Block incoming traffic to a port (runtime)")
    print("3. Allow incoming traffic to a port (permanent)")
    print("4. Block incoming traffic to a port (permanent)")
    print("5. List all firewall rules")
    print("6. Remove a firewall rule")
    print("7. Set default deny policy for incoming traffic")
    print("8. Exit")
    print("=" * 50)

# Adds a firewall rule to allow incoming traffic to a port (permanent)
def allow_port_permanent():
    port = input("Enter the port number to allow: ")
    protocol = input("Enter the protocol (tcp or udp): ")
    source = input("Enter the source IP address (0.0.0.0/0 to allow connections from any IP): ")
    subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public", "--add-rich-rule",
                    f'rule family="ipv4" source address="{source}" port protocol="{protocol}" port="{port}" accept'])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print(f"Incoming traffic to port {port} ({protocol}) from {source} has been allowed (permanent).")

# Adds a firewall rule to block incoming traffic to a port (permanent)
def block_port_permanent():
    port = input("Enter the port number to block: ")
    protocol = input("Enter the protocol (tcp or udp): ")
    source = input("Enter the source IP address (0.0.0.0/0 to block connections from any IP): ")
    subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public", "--add-rich-rule",
                    f'rule family="ipv4" source address="{source}" port protocol="{protocol}" port="{port}" reject'])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print(f"Incoming traffic to port {port} ({protocol}) from {source} has been blocked (permanent).")

# List all current firewall rules
def list_firewall_rules():
    subprocess.run(["sudo", "firewall-cmd", "--list-all"])

# Removes a firewall rule
def remove_firewall_rule():
    rule = input("Enter the rule to remove: ")
    subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public", "--remove-rich-rule", rule])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print(f"The rule '{rule}' has been removed.")

# Adds a firewall rule to allow incoming traffic to a port
def allow_port():
    port = input("Enter the port number to allow: ")
    protocol = input("Enter the protocol (tcp or udp): ")
    source = input("Enter the source IP address (0.0.0.0/0 to allow connections from any IP): ")
    subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public", "--add-rich-rule",
                    f'rule family="ipv4" source address="{source}" port protocol="{protocol}" port="{port}" accept'])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print(f"Incoming traffic to port {port} ({protocol}) from {source} has been allowed.")

# Adds a firewall rule to block incoming traffic to a port
def block_port():
    port = input("Enter the port number to block: ")
    protocol = input("Enter the protocol (tcp or udp): ")
    source = input("Enter the source IP address (0.0.0.0/0 to block connections from any IP): ")
    subprocess.run(["sudo", "firewall-cmd", "--permanent", "--zone=public", "--add-rich-rule",
                    f'rule family="ipv4" source address="{source}" port protocol="{protocol}" port="{port}" reject'])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print(f"Incoming traffic to port {port} ({protocol}) from {source} has been blocked.")

def set_default_deny():
    subprocess.run(["sudo", "firewall-cmd", "--remove-service=ssh", "--permanent"])
    subprocess.run(["sudo", "firewall-cmd", "--reload"])
    print("Default deny policy set.")

# While true loop is the main block of the program
# This is always the return destination for the functions unless the user exits
while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        allow_port_runtime()
    elif choice == "2":
        block_port_runtime()
    elif choice == "3":
        allow_port_permanent()
    elif choice == "4":
        block_port_permanent()
    elif choice == "5":
        list_firewall_rules()
    elif choice == "6":
        remove_firewall_rule()
    elif choice == "7":
        set_default_deny()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
