import re

# Open the file and read its content
with open('requirements.txt', 'r') as file:
    content = file.read()

# Remove all locations prefixed with '@'
content = re.sub('@.*', '', content)

# Write the modified content back to the file
with open('requirements.txt', 'w') as file:
    file.write(content)