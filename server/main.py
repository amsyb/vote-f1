import requests

# Define the URL
url = "https://api.openf1.org/v1/drivers?&session_key=latest"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    drivers = response.json()  # Parse the JSON data

    # Print each driver's name
    for driver in drivers:
        print(f"{driver['broadcast_name']} ({driver['full_name']})")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
