import requests
import csv
from datetime import datetime


def read_websites(file_path):
    try:
        with open(file_path, 'r') as file:
            websites = [line.strip() for line in file if line.strip()]
        return websites
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        response_time = response.elapsed.total_seconds() * 1000
        return "Online", status_code, round(response_time, 2)
    except requests.RequestException:
        return "Offline", "N/A", "N/A"

def log_results(file_name, results):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "URL", "Response Time (ms)", "Status Code", "Status"])
        for result in results:
            writer.writerow(result)

def main():
    print("Checking websites...")
    websites = read_websites('websites.txt')

    if not websites:
        return

    results = []
    for url in websites:
        status, status_code, response_time = check_website_status(url)
        print(f"{url} - {status} - {status_code}")

        results.append([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            url,
            response_time,
            status_code,
            status
        ])

    log_results('log.csv', results)


if __name__ == "__main__":
    main()
