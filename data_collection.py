import requests
import pandas as pd

# Example: Fetching data from an insurance company API
url = "https://api.insurancecompany.com/data"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

# Convert the data to a DataFrame for further processing
df = pd.DataFrame(data)
