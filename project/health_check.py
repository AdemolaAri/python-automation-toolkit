#!/usr/bin/env python3

import psutil
import socket
import time
import emails
import os

def cpu_usage_pct(threshold = 80):
    ''' check if CPU usage percentage is greater than threshold (80% by default) '''
    usage = psutil.cpu_percent()
    return usage > threshold

def disk_available_pct(threshold = 20):
    ''' check if available disk space is lower than threshold (20% default) '''
    free = 100 - psutil.virtual_memory().percent
    return free < threshold

def disk_memory_available(threshold = 500):
    ''' check if available memory is less than threshold (in MB) '''
    threshold = threshold * 1024 * 1024
    available = psutil.virtual_memory().available
    return available < threshold

def hostname_not_localhost():
    ''' check if hostname "localhost" cannot be resolved to "127.0.0.1" '''
    return socket.gethostbyname('localhost') != "127.0.0.1"

def report_issues(subject):
    ''' send email report with status update if any of above issues is
        encountered
    '''
    sender = "automation@example.com"
    to = os.environ.get('USER') + "@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, to, subject, body)
    emails.send_email(message)

def system_monitor(interval = 60):
    ''' Monitor computer health every `interval` seconds and
        report issues via email
		
		```NOTE: Using the While Loop and time.sleep() module is highly inefficient
			set up a cron job instead. 
		```
    '''
    while True:
        cpu_over_80_pct = cpu_usage_pct()
        disk_less_20_pct = disk_available_pct()
        disk_mem_less_500mb = disk_memory_available()
        hostname_unresolved = hostname_not_localhost()

        if cpu_over_80_pct:
            report_issues("Error - CPU usage is over 80%")
        if disk_less_20_pct:
            report_issues("Error - Available disk space is less than 20%")
        if disk_mem_less_500mb:
            report_issues("Error - Available memory is less than 500MB")
        if hostname_unresolved:
            report_issues("Error - localhost cannot be resolved to 127.0.0.1")
		
        time.sleep(interval)


if __name__ == "__main__":
    system_monitor()
