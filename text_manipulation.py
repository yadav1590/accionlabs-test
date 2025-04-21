import re

def read_logs_from_file(filepath):
    """Reads log lines from a file and returns them as a list."""
    with open(filepath, 'r') as file:
        return file.readlines()

def extract_logged_in_emails(logs):
    """Extracts email addresses from lines containing 'Email-'."""
    emails = []
    for line in logs:
        match = re.search(r"Email- ([^:]+):", line)
        if match:
            emails.append(match.group(1))
    return emails

def convert_emails_to_upper(emails):
    """Converts a list of email addresses to uppercase."""
    return [email.upper() for email in emails]

def filter_by_expiry(logs, expiry_date):
    """Filters log lines by a specific expiry date."""
    return [line for line in logs if f"expiry: {expiry_date}" in line]

# --- Main execution ---

log_file_path = "nginx.txt"
log_lines = read_logs_from_file(log_file_path)

# Extract and process emails
emails = extract_logged_in_emails(log_lines)
emails_upper = convert_emails_to_upper(emails)

# Filter logs by expiry date
filtered_logs = filter_by_expiry(log_lines, "06-02-2025")

# --- Output ---
print("🔐 Logged-in User Emails (Uppercase):")
for email in emails_upper:
    print(email)

print("\n📅 Logs with expiry 06-02-2025:")
for log in filtered_logs:
    print(log.strip())
