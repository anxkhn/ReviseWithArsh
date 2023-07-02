import re

def extract_problem_name(url):
    # Define the unified regex pattern for both LeetCode and GeeksforGeeks URLs
    pattern = r'(?:leetcode\.com/problems/|geeksforgeeks\.org/(?:[^/]+/)*)([a-zA-Z0-9\-]+)/?$'

    # Match the problem name using regex
    match = re.search(pattern, url)

    if match:
        problem_name = match.group(1)

        # Replace hyphens with spaces and capitalize each word
        problem_name = problem_name.replace('-', ' ').title()

        return problem_name

    return None

# Read the input markdown from a file
input_file_path = "data.md"
output_file_path = "output.md"

with open(input_file_path, 'r') as file:
    markdown = file.read()

# Split the markdown into lines
lines = markdown.strip().split('\n')

# Extract the table headers and remove leading/trailing spaces
headers = [header.strip() for header in lines[1].split('|')[1:-1]]

# Initialize a list to store the updated markdown
updated_markdown = []

# Add the modified header line to the updated markdown
updated_markdown.append(f"| {' | '.join(headers)} |")

# Add a separator line to the updated markdown
updated_markdown.append(f"|{'|'.join([' --- ']*(len(headers)+1))}|")

# Process each data row and update the markdown
for line in lines[3:]:
    row = [cell.strip() for cell in line.split('|')[1:-1]]

    # Extract the problem name from the URL and create a markdown link
    url = row[1]
    problem_name = extract_problem_name(url)
    
    if problem_name:
        row[1] = f"[{problem_name}]({url})"

    # Add the modified row to the updated markdown
    updated_markdown.append(f"| {' | '.join(row)} |")

# Join the updated markdown lines into a single string
updated_markdown_str = '\n'.join(updated_markdown)

# Save the updated markdown into a file
with open(output_file_path, 'w') as file:
    file.write(updated_markdown_str)

print(f"The updated markdown has been saved to '{output_file_path}'.")
