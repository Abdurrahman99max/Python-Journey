import requests # Invite the elde to your fireplace
# Send a message to a website and get a response
response =requests.get('https://www.porsche.com/central-eastern-europe/en/_cyprus_/?gad_source=1&gad_campaignid=22829559736&gbraid=0AAAAADczfgm-I6_ZHKs8gUYDgFD-reiKC&gclid=CjwKCAjwq9rFBhAIEiwAGVAZP2mrrD7Fu7uiwzHrFALZiTHzZ0e84BZ9nLJC9w4PzTfrMtJEjIpBvRoC4psQAvD_BwE')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request was successful!")
else:
    print("Request failed with status code:", response.status_code)

# Print the response text (the content of the requested page)
print(response.text)
