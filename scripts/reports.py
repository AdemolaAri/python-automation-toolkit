#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, body):
    ''' Set up PDF builder with simple styling '''
    styles = getSampleStyleSheet()
    processed = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(body, styles["BodyText"])
    empty_line = Spacer(1, 20)
    processed.build([report_title, empty_line, report_info])
