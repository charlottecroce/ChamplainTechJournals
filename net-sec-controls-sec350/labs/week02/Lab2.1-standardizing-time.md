# Lab 2.1 Standardizing on Time
Time is not recorded consistently across all of our systems.  You will note very quickly that none of your systems record the timezone within the syslog entry.  Without this data it is very hard to develop a cohesive timeline for events that span multiple log sources and multiple time zones.  We are going to fix this.

Though the date is set for EST, the specific log entry that may or may not be forwarded to a log server has no indication of the timezone or the year.

![image](https://github.com/user-attachments/assets/9f753b28-fd3b-4854-b155-54bca96e239c)

## rw01 - ubuntu
We fix this by commenting out a line (shown below) in RW01's main `/etc/rsyslog.conf` file.  By default, rsyslog does not use high precision timestamps.  Make sure to restart rsyslog on rw01
![image](https://github.com/user-attachments/assets/8ed3b550-988b-432c-895e-3f1e3acceb45)

![image](https://github.com/user-attachments/assets/aa578b16-2113-4af0-b7c7-ae18e52ad336)


## web01 & log01 - rocky
in `/etc/rsyslog.conf`
- add these lines:
  - `$ActionFileDefaultTemplate RSYSLOG_SyslogProtocol23Format`---enables RFC 5424-style syslog format, which includes high-precision timestamps with timezone information.
  - `template(name="BetterTiming" type="string" string="%timestamp:::date-rfc3339% %HOSTNAME% %syslogtag%%msg%\n")`---explicitly defines a custom template, including high-fidelity timestamps with timezone info
  - add the suffix `;BetterTiming` to the loggging destination---enables the custom template on your logs

![image](https://github.com/user-attachments/assets/0331dde8-2028-445d-89e2-d55fb5b3cf45)
![image](https://github.com/user-attachments/assets/742df745-1a26-4c6d-a082-d7edfa04fd2f)
