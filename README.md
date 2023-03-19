# Firewall Manager

This is a Python 3 script for managing firewall rules using the `firewalld` utility. It was developed and tested on openSUSE Tumbleweed but should also work on CentOS, Red Hat, and Fedora systems, as long as they have `firewalld` installed.

## Features

- Allow incoming traffic to a port (runtime)
- Block incoming traffic to a port (runtime)
- Allow incoming traffic to a port (permanent)
- Block incoming traffic to a port (permanent)
- List all firewall rules
- Remove a firewall rule
- Set default deny policy for incoming traffic

## Requirements

- Python 3.x
- firewalld

## Usage

1. Clone this repository or download the script.
2. Make the script executable with `chmod +x <script-name>`.
3. Run the script with `./<script-name>` or `python3 <script-name>`.

## Contributing

Feel free to contribute by opening a pull request or reporting issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

