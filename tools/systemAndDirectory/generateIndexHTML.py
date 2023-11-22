import os
import markdown


def generate_html_for_directory(directory_path):
    """
    Generates an HTML representation of the given directory path, excluding hidden files and directories.
    Converts Markdown files to HTML and includes only the generated HTML files in the index.
    Paths are adjusted for a GitHub Pages project site.
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
            # Correctly format the file path
            formatted_path = os.path.join(relative_path, file).replace("\\", "/")
            file_web_path = f"superposition000/{formatted_path}"
            # Convert Markdown files to HTML
            if file.endswith(".md"):
                # Read the markdown file content
                with open(file_path, "r", encoding="utf-8") as md_file:
                    md_content = md_file.read()
                # Convert to HTML
                html_converted = markdown.markdown(md_content)
                # Generate the HTML file name
                html_file_name = f"{os.path.splitext(file)[0]}.html"
                html_file_path = os.path.join(root, html_file_name)
                # Save the HTML file, replacing if it exists
                with open(html_file_path, "w", encoding="utf-8") as html_file:
                    html_file.write(html_converted)
                # Add the link to the HTML file in the index, with the adjusted path
                html_content += (
                    f"<li><a href='{file_web_path}'>{html_file_name}</a></li>"
                )
            elif not file.endswith(".html"):
                # Link to non-HTML files directly, with the adjusted path
                html_content += f"<li><a href='{file_web_path}'>{file}</a></li>"

        if relative_path != ".":
            html_content += "</ul>"

    html_content += "</ul></body></html>"
    return html_content


# Example usage of the function
directory_path = "../.."  # Replace with actual directory path

# Generate HTML content
html_content = generate_html_for_directory(directory_path)

# Save the HTML content to an index.html file
output_path = "../../index.html"  # Adjust this path as needed
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Note: Ensure the 'markdown' module is installed in your local environment
