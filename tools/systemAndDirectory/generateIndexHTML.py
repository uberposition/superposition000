import os


def generate_html_for_directory(directory_path):
    """
    Generates an HTML representation of the given directory path.
    """
    html_content = "<html><head><title>Directory Listing</title></head><body>"
    html_content += "<h1>Directory Listing</h1>"
    html_content += "<ul>"

    for root, dirs, files in os.walk(directory_path):
        # Relative path from the directory being listed to the current 'root'
        relative_path = os.path.relpath(root, directory_path)

        if relative_path != ".":
            html_content += f"<li><strong>{relative_path}</strong></li>"
            html_content += "<ul>"

        for file in files:
            # Skip .DS_Store files commonly found on macOS
            if file == ".DS_Store":
                continue

            # Construct relative file path for hyperlink
            file_path = os.path.join(relative_path, file)
            html_content += f"<li><a href='{file_path}'>{file}</a></li>"

        if relative_path != ".":
            html_content += "</ul>"

    html_content += "</ul></body></html>"
    return html_content


# Directory path - for demonstration, using a placeholder
directory_path = "../.."  # Replace with actual directory path

# Generate HTML content
html_content = generate_html_for_directory(directory_path)

# Save the HTML content to an index.html file
with open("index.html", "w") as file:
    file.write(html_content)
