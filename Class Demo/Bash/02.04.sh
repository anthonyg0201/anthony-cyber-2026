#!/bin/bash
LOG_FILE="$HOME/test.log"
ALERT_FILE="$HOME/security_alerts.log"
SEARCH_STR="Failed password"

# Create log if it doesn't exist
touch "$LOG_FILE"

# Count and log matches
MATCHES=$(grep "$SEARCH_STR" "$LOG_FILE" | tee -a "$ALERT_FILE" | wc -l)
echo "$(date): Found $MATCHES matches in $LOG_FILE" >> "$ALERT_FILE"
echo "Found $MATCHES new 'Failed password' entries."