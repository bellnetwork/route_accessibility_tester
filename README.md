# route_accessibility_tester
    Route Accessibility Tester
    Description
    The Route Accessibility Tester is a Python script that checks the accessibility of specific routes on a given IP address or domain. By sending GET requests to these routes, it determines whether they are reachable and prints the response status codes. It's a handy tool for security assessments or monitoring the availability of certain routes.

    ⚠️ Important Notice: This tool is designed to be used only on servers owned by you or where you have explicit permission to test. Using this tool on servers without proper authorization may violate terms of service, laws, or ethical guidelines. Always seek permission before conducting any form of penetration testing or vulnerability assessment.

    Installation
    Clone the repository:

    git clone https://github.com/BellSecurity/route-accessibility-tester.git

    Navigate to the directory:
    cd route-accessibility-tester

    No additional installation steps required. Just ensure you have Python and requests library installed.

    Usage
    Run the script:
    python route_tester.py

    When prompted, enter either an IP address (e.g., 192.168.1.1) or a domain (e.g., bellnetwork.eu).

    The script will make GET requests to each route in the routes_to_test list.

    For each route, the script will print the HTTP status code and the JSON response (if available).

    If there's an error accessing a route, the script will print an error message.

    Customization
    The routes in routes_to_test are predefined. Modify this list in route_tester.py to test different routes as per your needs.

    By default, the script assumes that IP addresses use the http protocol, while domains use the https protocol. Adjust as necessary.

    Contribution
    Contributions are welcome! Please submit a pull request or open an issue to suggest changes or additions.

    License
    MIT License. See LICENSE for more details.