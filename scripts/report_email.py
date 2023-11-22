#!/usr/bin/env python3

import emails
import os
import datetime
import reports
import glob

def process_text_data(path):
    '''
        process the text data from the path directory into the 
        specified format 
    '''
    data = []
    for text_file in glob.glob(path + "*.txt"):
        with open(text_file) as tf:
            name = tf.readline()
            weight = tf.readline()

            data.append(f"name: {name}")
            data.append(f"weight: {weight}")
            data.append('\n')

    return '<br/>'.join(data)


def main():
    ''' Gather all requirements for the functions'''

    path = os.getcwd() + "/supplier-data/descriptions/"
    today = datetime.datetime.today().strftime("%B %d, %Y")

    if not os.path.exists(path):
        print(f" Path {path} does not exist")
        return
        
    paragraph = process_text_data(path)
    title = f"Processed Update on {today}"
    fname = './processed.pdf'

    reports.generate_report(fname, title, paragraph)

if __name__ == "__main__":
    main()
    username = os.environ.get('USER')

    sender = "automation@example.com"
    receiver = "{}@example.com".format(username)
    subject_line = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = './processed.pdf'

    message = emails.generate_email(sender, receiver, subject_line, body, attachment)
    emails.send_email(message)
