import re
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

# Parse logs into dictionaries
def parse_apache_logs_to_dict(file_path):
    """Parse Apache logs into a list of dictionaries."""
    logs = []
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.+?)\] "(?P<method>\w+) (?P<url>.+?) HTTP/1.1" (?P<status>\d+) (?P<size>\d+|-)'
    
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                log_entry = match.groupdict()
                log_entry['size'] = int(log_entry['size']) if log_entry['size'] != '-' else 0
                log_entry['status'] = int(log_entry['status'])
                logs.append(log_entry)
    
    return logs

# Index logs into Elasticsearch
def index_logs_to_elasticsearch(logs, index_name="logs"):
    """Index a list of log dictionaries into Elasticsearch."""
    try:
        es = Elasticsearch("http://localhost:9200")
        if not es.ping():
            print("Elasticsearch is not running. Ensure it's started.")
            return

        for log_entry in logs:
            es.index(index=index_name, document=log_entry)

        print(f"Logs successfully indexed to Elasticsearch index: {index_name}")

    except ConnectionError:
        print("Failed to connect to Elasticsearch. Ensure it is running on http://localhost:9200.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    log_file = "access.log"  # Replace with your log file path
    log_data = parse_apache_logs_to_dict(log_file)
    print("Parsed Logs:", log_data[:5])  # Display first 5 logs

    index_logs_to_elasticsearch(log_data)
