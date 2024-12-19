from collections import Counter

# Detect brute-force attempts
def detect_brute_force(logs, threshold=10):
    """Detect IPs with repeated failed login attempts."""
    failed_ips = [log['ip'] for log in logs if log['status'] == 401]
    brute_force_ips = Counter(failed_ips)
    suspicious_ips = {ip: count for ip, count in brute_force_ips.items() if count > threshold}
    return suspicious_ips

# Analyze suspicious patterns
def analyze_suspicious_patterns(logs):
    """Analyze logs for suspicious activity."""
    print("\n=== Brute Force Attempts ===")
    brute_force = detect_brute_force(logs)
    print(brute_force)

    print("\n=== Top Status Codes ===")
    status_codes = Counter([log['status'] for log in logs])
    print(status_codes)

    print("\n=== Top IPs ===")
    ip_counts = Counter([log['ip'] for log in logs])
    print(ip_counts.most_common(10))

# Main execution
if __name__ == "__main__":
    log_file = "accesslog.txt"  # Replace with your log file path
    
    # Reuse the parser from the first file
    from log_parser import parse_apache_logs_to_dict
    log_data = parse_apache_logs_to_dict(log_file)
    
    print("Parsed Logs:", log_data[:5])  # Display first 5 logs
    analyze_suspicious_patterns(log_data)
