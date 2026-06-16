from datetime import datetime, timedelta

start_time = datetime(2026, 6, 16, 9, 0, 0)
username = "jdoe"
source_ip = "192.168.1.50"

for i in range(10):
    event_time = start_time + timedelta(seconds=i * 15)
    print(
        f"{event_time} EventCode=4625 Account_Name={username} "
        f"src_ip={source_ip} Workstation_Name=WIN-01 Logon_Type=3 Status=Failed"
    )
