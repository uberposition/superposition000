import os
import markdown


def generate_html_for_directory(directory_path):
    """
    Generates an HTML representation of the given directory path, excluding hidden files and directories.
    Converts Markdown files to HTML. Only includes HTML files in the index and excludes original .md files.
    Adjusts paths for files in subdirectories.
    """
    html_content = "<html><head><title>Directory Listing</title></head><body>"
    html_content += "<h1>Directory Listing</h1>"
    html_content += "<ul>"

    for root, dirs, files in os.walk(directory_path):
        # Skip hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        files = [f for f in files if not f.startswith(".")]

        # Relative path from the directory being listed to the current 'root'
        relative_path = os.path.relpath(root, directory_path)

        if relative_path != ".":
            html_content += f"<li><strong>{relative_path}</strong></li>"
            html_content += "<ul>"

        for file in files:
            file_path = os.path.join(root, file)
            file_web_path = f"{relative_path}/{file}" if relative_path != "." else file

            if file.endswith(".md"):
                # Convert Markdown files to HTML and exclude them from the index
                with open(file_path, "r", encoding="utf-8") as md_file:
                    md_content = md_file.read()
                html_converted = markdown.markdown(md_content)
                html_file_name = f"{os.path.splitext(file)[0]}.html"
                html_file_path = os.path.join(root, html_file_name)
                with open(html_file_path, "w", encoding="utf-8") as html_file:
                    html_file.write(html_converted)
            elif not file.endswith(".md"):
                # Include HTML and other files in the index
                html_content += f"<li><a href='{file_web_path}'>{file}</a></li>"

        if relative_path != ".":
            html_content += "</ul>"

    html_content += "</ul></body></html>"
    return html_content


# Example usage of the function
directory_path = "../.."  # Replace with actual directory path
html_content = generate_html_for_directory(directory_path)

# Save the HTML content to an index.html file
output_path = (
    "../../index.html"  # Replace with the path where you want to save the index.html
)
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Note: Ensure the 'markdown' module is installed in your local environment
