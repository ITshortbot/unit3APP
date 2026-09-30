import re

# Sample text
text = """
Hello everyone!

You can contact us at:
Atharv@gmail.com
student123@college.edu
support@example.org
invalid-email@com
hello@domain.co.in

Thank you!
"""

# Regular expression pattern for email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all email addresses
emails = re.findall(email_pattern, text)

# Display results
print("Email addresses found:")

if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

Comment:-
Email addresses found:
Atharv@gmail.com
student123@college.edu
support@example.org
hello@domain.co.in

Total emails found: 4

print("\nTotal emails found:", len(emails))
