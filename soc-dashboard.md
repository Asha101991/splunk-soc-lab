# SOC Dashboard Ideas

Use these panels in Splunk dashboards:

## Panel 1: Failed Logins Over Time

```spl
sourcetype=windows_auth EventCode=4625
| timechart count as failed_logins
```

## Panel 2: Top Failed Login Users

```spl
sourcetype=windows_auth EventCode=4625
| top Account_Name
```

## Panel 3: Top Source IPs

```spl
sourcetype=windows_auth EventCode=4625
| top src_ip
```

## Panel 4: Successful Administrator Logins

```spl
sourcetype=windows_auth EventCode=4624 Account_Name="Administrator"
| table _time, Account_Name, src_ip, Workstation_Name
```
