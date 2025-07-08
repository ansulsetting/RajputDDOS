# RajputDDOS - Network Security Educational Tool

## ⚠️ IMPORTANT DISCLAIMER

This repository is for **EDUCATIONAL PURPOSES ONLY**. The tools and concepts presented here are intended to help cybersecurity professionals, students, and researchers understand network security vulnerabilities and defense mechanisms.

**NEVER use these tools against systems you do not own or without explicit permission. Unauthorized network attacks are illegal and unethical.**

## Overview

RajputDDOS is an educational repository that demonstrates network security concepts, particularly focusing on:

- Understanding Distributed Denial of Service (DDoS) attack vectors
- Learning defensive mechanisms and mitigation strategies
- Exploring network stress testing for authorized systems
- Studying traffic analysis and monitoring techniques

## Current Status

✅ **Repository Status: Functional Educational Environment**

This repository now provides a complete educational environment for learning about network security concepts:

- [x] Educational documentation about DDoS concepts
- [x] Legal stress testing tools for authorized use
- [x] Defense mechanism examples
- [x] Network monitoring demonstrations
- [x] Best practices for network security
- [x] Proper setup and installation scripts
- [x] Interactive educational tools with safety confirmations

## Prerequisites

- Basic understanding of networking concepts
- Knowledge of Python programming
- Familiarity with cybersecurity principles
- **Authorization to test on target systems**

## Legal and Ethical Use

### ✅ Authorized Uses:
- Testing your own networks and systems
- Educational research in controlled environments
- Cybersecurity training with proper authorization
- Penetration testing with explicit client consent

### ❌ Prohibited Uses:
- Attacking systems without permission
- Disrupting public services or infrastructure
- Any malicious or harmful activities
- Bypassing security measures unlawfully

## Getting Started

### Quick Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ansulsetting/RajputDDOS.git
   cd RajputDDOS
   ```

2. **Run the setup script:**
   ```bash
   ./setup.sh
   ```

3. **Explore the educational tools:**
   ```bash
   # Display system information
   python3 tools/network_monitor.py --info
   
   # View help for all options
   python3 tools/network_monitor.py --help
   ```

### Manual Setup

If you prefer manual setup:

```bash
# Install dependencies
pip3 install -r requirements.txt

# Make scripts executable
chmod +x tools/network_monitor.py
```

### Available Tools

- **Network Monitor** (`tools/network_monitor.py`): Educational network monitoring and scanning tool
- **Documentation** (`docs/`): Comprehensive educational materials about network security
- **Examples** (`examples/`): Practical examples for learning

### Educational Usage Examples

```bash
# Display system information (safe)
python3 tools/network_monitor.py --info

# Monitor network usage (requires permission confirmation)
python3 tools/network_monitor.py --monitor --duration 30

# Educational port scan (requires permission confirmation)
python3 tools/network_monitor.py --scan --host 127.0.0.1
```

## Contributing

We welcome contributions that enhance the educational value of this repository while maintaining ethical standards. Please ensure all contributions:

- Include proper documentation
- Follow ethical guidelines
- Include appropriate disclaimers
- Focus on defensive/educational aspects

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions about ethical use or educational applications, please open an issue in this repository.

---

**Remember: With great power comes great responsibility. Use these tools wisely and ethically.**