import csv

def csv_to_markdown(csv_file_path, md_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        table_data = list(reader)

    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in table_data:
        markdown += "| " + " | ".join(row) + " |\n"

    with open(md_file_path, 'w') as md_file:
        md_file.write(markdown)

# Example usage
csv_file_path = 'data.csv'  # Replace with the actual path to your CSV file
md_file_path = 'data.md'    # Replace with the desired path for your Markdown file
csv_to_markdown(csv_file_path, md_file_path)
