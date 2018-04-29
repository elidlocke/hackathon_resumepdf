# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generate_pdf.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: enennige <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/28 12:47:28 by enennige          #+#    #+#              #
#    Updated: 2018/04/28 18:15:02 by enennige         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

#global vars
filename = "resume.pdf"
Story = []

doc = SimpleDocTemplate(filename,pagesize=letter,
                        rightMargin=30,leftMargin=30,
                        topMargin=30,bottomMargin=18)

#user input vars
phone_number = "510-396-3057"
full_name = "Nik Roman"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]
job_skills = ["landscaping", "gardening", "pruning bushes", "shovelling", "being the coolest"]
availability = "Weekdays after 9am"
languages = ["Spanish", "English"]

class Job(object):
    def __init__(self, start_date, end_date, company_name, job_title, duties):
        self.start_date = start_date
        self.end_date = end_date
        self.company_name = company_name
        self.job_title = job_title
        self.duties = duties

jobs = [Job("Jan 2015", "Feb 2016", "Bayside Landscaping", "Landscaper",
            ["Shovelled large loads of gravel to level surfaces",
            "Used heavy machinery including backhoe mini-digger and lawnmower",
            "Trimmed hedges by hand"]),
        Job("Jan 2014", "Dec 2014", "Gumbos Painting", "Painter",
            ["Matched color samples for clients based on their taste preferences",
            "Rolling, brushing and spraying of exterior surfaces", 
            "Patching and wood filling of trim and detailing of windows"])]


#styling
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
title_size = 30
header_size = 18
paragraph_size = 12

def put_content_line(content, size):
    ptext = '<font size=%d>%s</font>' % (size, content)
    Story.append(Paragraph(ptext, styles["Normal"]))

#Resume Name
def put_name():
    put_content_line(full_name, title_size)
    Story.append(Spacer(1, title_size))

# Write section header
def put_header(section_title):
    put_content_line(section_title, header_size)
    Story.append(Spacer(1, header_size))

# Write section paragraph
def put_paragraph(content):
    put_content_line(content, paragraph_size)
    Story.append(Spacer(1, paragraph_size))

# Contact Information
def put_contact(phone_number, address):
    put_content_line(phone_number, paragraph_size)
    for part in address:
        put_content_line(part.strip(), paragraph_size)
    Story.append(Spacer(1, paragraph_size))

#Experience
def put_experience(jobs):
    put_header("Experience")
    for job in jobs:
        put_content_line(job.start_date + " - " + job.end_date, paragraph_size)
        put_content_line(job.job_title + " at " + job.company_name, paragraph_size)
        for duty in job.duties:
            put_content_line("- " + duty, paragraph_size)
        Story.append(Spacer(1, paragraph_size))

# Put a list
def put_list(title, job_skills):
    put_header(title)
    job_string = ', '.join(job_skills)
    put_paragraph(job_string)

# Availability
def put_availability(availability):
    put_header("Availability")
    put_paragraph(availability)


if __name__ == "__main__":
    put_name()
    put_contact(phone_number, address_parts)
    put_list("Skills", job_skills)
    put_experience(jobs)
    put_list("Languages", languages)
    put_availability(availability)
    doc.build(Story)
