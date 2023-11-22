import os


def generate_html_for_directory(directory_path, repo_name):
    """
    Generates an HTML representation of the given directory path.
    Includes the repository name in the paths for GitHub Pages.
    """
    html_content = "<html><head><title>Directory Listing</title></head><body>"
    html_content += "<h1>Directory Listing</h1>"
    html_content += "<ul>"

    for root, dirs, files in os.walk(directory_path):
        # Relative path from the directory being listed to the current 'root'
        relative_path = os.path.relpath(root, directory_path)
        # Prepend the repository name to the path
        web_path = f"/{repo_name}/{relative_path}".replace("\\", "/").strip(".")

        if relative_path != ".":
            html_content += f"<li><strong>{web_path}</strong></li>"
            html_content += "<ul>"

        for file in files:
            # Skip .DS_Store files commonly found on macOS
            if file == ".DS_Store":
                continue

            # Construct web file path for hyperlink
            file_web_path = os.path.join(web_path, file).replace("\\", "/")
            html_content += f"<li><a href='{file_web_path}'>{file}</a></li>"

        if relative_path != ".":
            html_content += "</ul>"

    html_content += "</ul></body></html>"
    return html_content


# Example usage of the function
directory_path = "../.."  # Replace with actual directory path
repo_name = "superposition000"  # Repository name to include in the path

# Generate HTML content
html_content = generate_html_for_directory(directory_path, repo_name)

# Save the HTML content to an index.html file
with open("index.html", "w") as file:
    file.write(html_content)

# After running this script, you'll get an index.html with paths adjusted for GitHub Pages.
