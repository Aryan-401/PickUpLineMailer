import smtplib
import ssl
import os
from email.message import EmailMessage

from dotenv import load_dotenv  # pip install python-dotenv
from pickup import content, date
load_dotenv()

MSG = EmailMessage()
PORT = 465  # For SSL
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
LUCKY_GUY = os.getenv('LUCKY_GUY')
SECONDARY_EMAIL = os.getenv('SECONDARY_EMAIL')
SUBJECT = f"Daily Validation - Day {date}"

if date > 30:
    LUCKY_GUY = SECONDARY_EMAIL

MSG["From"] = EMAIL
MSG["To"] = LUCKY_GUY
MSG["Bcc"] = SECONDARY_EMAIL
MSG["Subject"] = SUBJECT

MSG.set_content(content)
# Create a secure SSL context
print(EMAIL, PASSWORD, LUCKY_GUY, SUBJECT)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(EMAIL, PASSWORD)
    server.send_message(MSG)
