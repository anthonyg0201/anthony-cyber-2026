#!/bin/bash
# Count failed logins
FILE="test.log"
COUNT=0

# Create dummy file if it doesn't exist for testing
if [ ! -f "$FILE" ]; then
    echo "Failed password for user1" > "$FILE"
    echo "Accepted password for user1" >> "$FILE"
    echo "Failed password for user2" >> "$FILE"
fi

# Read file line by line
while IFS= read -r line; do
    if echo "$line" | grep -q "Failed password"; then
        ((COUNT++))
    fi
done < "$FILE"

echo "Total failed logins: $COUNT"