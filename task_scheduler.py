import smtplib
import ssl
import os

from dotenv import load_dotenv  # pip install python-dotenv
from pickup import content, date
load_dotenv()

PORT = 465  # For SSL
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
LUCKY_GUY = os.getenv('LUCKY_GUY')
SUBJECT = f"Daily Validation - Day {date}"

if date > 30:
    LUCKY_GUY = 'agarg1_be21@thapar.edu'

# Create a secure SSL context
print(EMAIL, PASSWORD, LUCKY_GUY, SUBJECT)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(EMAIL, PASSWORD)
    message = 'Subject: {}\n\n{}'.format(SUBJECT, content)
    server.sendmail(EMAIL, LUCKY_GUY, message)
