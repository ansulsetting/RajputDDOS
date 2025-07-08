#!/bin/bash

# RajputDDOS Educational Setup Script

echo "🎓 Setting up RajputDDOS Educational Environment"
echo "================================================"

# Check Python version
python_version=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    echo "✅ Python detected: $python_version"
else
    echo "❌ Python 3 is required but not found"
    exit 1
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
python3 -m pip install -r requirements.txt

if [[ $? -eq 0 ]]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Make scripts executable
echo "🔧 Setting up executable permissions..."
chmod +x tools/network_monitor.py

echo "✅ Setup completed successfully!"
echo ""
echo "🚀 You can now run:"
echo "   python3 tools/network_monitor.py --help"
echo ""
echo "⚠️  Remember: Educational use only!"
echo "   Only use these tools on systems you own or have explicit permission to test."