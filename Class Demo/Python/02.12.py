# 02.12.py

import csv
from collections import Counter

# Sample comments data
comments = [
    {"email": "user1@example.com", "comment": "This is a comment."},
    {"email": "user2@example.com", "comment": "Another comment."},
    {"email": "user1@example.com", "comment": "Yet another comment."},
    {"email": "user3@example.com", "comment": "More comments."},
    {"email": "user2@example.com", "comment": "Comment again."},
]

# Group comments by email and count them
email_counts = Counter(comment['email'] for comment in comments)

# Save to comments.csv
with open('comments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email', 'Count'])
    for email, count in email_counts.items():
        writer.writerow([email, count])