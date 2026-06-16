# Splunk SOC Lab Walkthrough

## Step 1: Upload Logs

Upload `sample-logs/windows-auth-sample.log` into Splunk.

## Step 2: Search Failed Logins

```spl
sourcetype=windows_auth EventCode=4625
```

## Step 3: Detect Brute Force Activity

```spl
sourcetype=windows_auth EventCode=4625
| stats count by Account_Name, src_ip
| where count >= 5
```

## Step 4: Check for Successful Login After Failures

```spl
sourcetype=windows_auth (EventCode=4625 OR EventCode=4624)
| table _time, EventCode, Account_Name, src_ip, Workstation_Name
| sort _time
```

## Step 5: Create an Alert

Suggested alert settings:

- Alert type: Scheduled
- Run every: 5 minutes
- Trigger condition: Number of results is greater than 0
- Severity: Medium or High

## Step 6: Document the Incident

Use `docs/incident-report-template.md` to write your findings.
