# Log Analysis Tool

## Overview
The **Log Analysis Tool** is a Python-based project designed to parse, analyze, and detect suspicious patterns in server log files, such as Apache access logs. It supports indexing log data into Elasticsearch and provides insights into suspicious activities like brute-force attacks, failed logins, and more.

## Features
- Parse server logs (e.g., Apache logs) into structured data.
- Detect patterns such as:
  - Brute-force attacks
  - Failed login attempts
  - Most active IP addresses and status codes
- Index parsed logs into Elasticsearch for advanced querying.
- Analyze logs and generate actionable insights.

## Technologies Used
- **Python**: Core language for parsing and analysis.
  - Libraries: `re`, `pandas`, `elasticsearch`, `loguru`
- **Elasticsearch**: For indexing and querying log data.
- **Kibana**: (Optional) For creating visual dashboards.
  
## Installation

### Prerequisites
- Python 3.8 or higher
- Elasticsearch (Ensure it's running on `http://localhost:9200`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/ghulamahmadkhan/log-analysis-tool.git
   cd log-analysistool
