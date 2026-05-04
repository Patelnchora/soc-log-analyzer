# 🛡️ SOC Log Analyzer

It is a Python-based tool designed to simulate real-world Security Operations Center (SOC) workflows by analyzing system logs and detecting suspicious activities. It focuses on identifying failed login attempts, extracting attacker IP addresses, and highlighting potential brute-force attacks.

## 🚀 Features
- **Log Parsing:** Processes authentication logs to extract relevant security events
- **Brute-Force Detection:** Identifies repeated failed login attempts from the same IP
- **IP Extraction:** Uses Regex to accurately extract IPv4 addresses from logs
- **Threat Classification:** Assigns severity levels based on frequency of suspicious activity
- **Investigation Output:** Generates a structured report for quick analysis and response
- **Modular Design:** Built with reusable components for easy scalability and integration

## 🛠️ Technologies Used
- **Python 3.x**
- **Regular Expressions (Regex)**
- **Libraries:** 'collections', 're', 'os', 'csv', 'json'

## 📋 How to use
1. Clone the repository:
   "'bash
   git clone [https://github.com/Patelnchora/soc-log-analyzer.git](https://github.com/Patelnchora/soc-log-analyzer.git)
