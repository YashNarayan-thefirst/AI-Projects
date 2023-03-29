import requests
from requests.structures import CaseInsensitiveDict
from io import BytesIO
import openai
import urllib.request
import matplotlib.pyplot as plt


# Set up the OpenAI API key
openai.api_key = "your_API_key"

# Set up the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set up the headers for the request
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {openai.api_key}"

# Set up the request parameters
data = """
{
    "prompt": "A TV in a cornfield",
    "model": "image-alpha-001",
    "num_images": 4,
    "size": "512x512",
    "response_format": "url"
}
"""

# Send the request to the API endpoint
resp = requests.post(url, headers=headers, data=data)

# Get the URL of the generated image
image_url = resp.json()["data"][0]["url"]

# Set up the URL for the image
url = image_url

# Open the URL image and read the content
with urllib.request.urlopen(url) as url_response:
    image_content = url_response.read()

# Convert the image content to a format that can be displayed by matplotlib
img = plt.imread(BytesIO(image_content), format='jpg')

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()
