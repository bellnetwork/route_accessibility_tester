# Created by: Bell Security (https://bellnetwork.eu/access_security)
# 
# Script Description:
# -------------------
# This script is designed to test the accessibility of specific routes on a given IP address or domain. 
# By sending GET requests to these routes, the script determines whether they are reachable and prints 
# the response status codes. This can be helpful for security assessments or monitoring the availability of certain routes.
#
# Usage:
# ------
# 1. Run the script.
# 2. When prompted, enter either an IP address (e.g., 192.168.1.1) or a domain (e.g., bellnetwork.eu).
# 3. The script will then make GET requests to each route in the `routes_to_test` list.
# 4. For each route, the script will print the HTTP status code and the JSON response (if any).
# 5. If there's an error accessing a route, the script will print an error message.
#
# Note: 
# - The routes in `routes_to_test` are predefined. You can modify this list to test different routes as per your needs.
# - The script assumes that IP addresses use the `http` protocol, while domains use the `https` protocol.
# - Use this script at your own risk. We are not responsible for any damage caused by this script.
# - This script is for educational purposes only. It is not intended to be used for illegal purposes.

import requests
import re

def test_routes(base_url, routes):
    for route in routes:
        url = f"{base_url}/{route}"
        try:
            response = requests.get(url)
            print(f"Response from {url}: {response.status_code}")
            print(response.json())
            print("----------")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

if __name__ == "__main__":
    # Prompt the user for an IP address or domain
    input_value = input("Enter the IP address or domain (e.g. 192.168.1.1 or bellnetwork.eu): ")

    # Check if the input value is an IP address
    if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", input_value):
        base_url = f"http://{input_value}"
    else:
        base_url = f"https://{input_value}"

    routes_to_test = [
    "api/v1/users/get_details",
    "assets/js/config.js",
    "docs/api/endpoints/login",
    "public/assets/img/logo.png",
    "internal/db/backup.sql",
    "v2/data/retrieve_records",
    "user_profile/images/avatar",
    "system/config/db_config.php",
    "scripts/load_balancer/status",
    "admin/dashboard/settings"
    ]

    test_routes(base_url, routes_to_test)
