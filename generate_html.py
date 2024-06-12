# import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the directory URL
directory_url = "http://43.136.235.235/d/%E8%B5%84%E6%96%99/news/"

# Send HTTP request and get the directory page content
response = requests.get(directory_url)
html_content = response.content

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all image links
image_links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href.endswith(".jpg") or href.endswith(".jpeg") or href.endswith(".png"):
        image_links.append(directory_url + href)

# Generate HTML file
html_output = "<!DOCTYPE html>\n<html>\n<head>\n  <title>Image Gallery</title>\n</head>\n<body>\n"
for image_link in image_links:
    html_output += f"  <img src='{image_link}' alt='Image'>\n"
html_output += "</body>\n</html>"

# Write HTML content to a file
with open("image_gallery.html", "w") as f:
    f.write(html_output)

print("HTML file generated successfully!")
