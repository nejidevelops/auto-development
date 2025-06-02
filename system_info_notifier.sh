#!/bin/bash

# Get system info
UPTIME=$(uptime -p)
CPU=$(lscpu | grep 'Model name' | sed 's/Model name:\s*//')
MEMORY=$(free -h | grep Mem | awk '{print $3 "/" $2}')
DISK=$(df -h / | tail -1 | awk '{print $3 "/" $2 " used"}')
OS=$(lsb_release -d | cut -f2)

# Compose message
MESSAGE="Uptime: $UPTIME
CPU: $CPU
Memory: $MEMORY
Disk: $DISK
OS: $OS"

# Show desktop notification (requires `notify-send`)
notify-send "🖥️ System Status" "$MESSAGE"

# Optional: Log to file
echo -e "$(date):\n$MESSAGE\n" >> ~/system_info_log.txt
