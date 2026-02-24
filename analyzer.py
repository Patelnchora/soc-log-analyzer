import re

ip_count = {}

with open("sample.log", "r") as file:
    logs = file.readlines()

for log in logs:
    if "Failed password" in log:
        
        ip = re.search(r'\d+\.\d+\.\d+\.\d+', log)
        
        if ip:
            ip = ip.group()
            
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1


print("\n=== SOC ALERT REPORT ===\n")

for ip, count in ip_count.items():
    
    if count >= 3:
        severity = "HIGH"
        
    elif count == 2:
        severity = "MEDIUM"
        
    else:
        severity = "LOW"
    
    print(f"""
IP Address: {ip}
Failed Attempts: {count}
Severity: {severity}
Status: {'SUSPICIOUS' if severity == 'HIGH' else 'Monitor'}
------------------------
""")
    
with open("report.txt", "w", encoding="utf-8") as report:
    
    report.write("SOC ALERT REPORT\n\n")
    
    for ip, count in ip_count.items():
        
        if count >= 3:
            severity = "HIGH"
        elif count == 2:
            severity = "MEDIUM"
        else:
            severity = "LOW"
        
        report.write(f"{ip} → Attempts: {count} → Severity: {severity}\n")