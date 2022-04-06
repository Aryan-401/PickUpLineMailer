import requests  # pip install requests
import json
from datetime import datetime

DAY_INIT = datetime(2022, 4, 5)  # Enter Starting date

# Gets Pickup line and parses into a json file
response_API = requests.get('https://getpickuplines.herokuapp.com/lines/random')
data = json.loads(response_API.text)
date = (datetime.now() - DAY_INIT).days

content = f'''Hi there cutie ;)
Here is your daily pickup line:

{data["line"]}

Until next time
xoxo

(Day {date} of 30)
'''
