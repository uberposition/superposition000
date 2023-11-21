import re


def generate_toc(markdown_text):
    """
    Generates a Table of Contents for the given markdown text, including all headings.
    """
    headings = re.findall(r"^(#+ .+)$", markdown_text, re.MULTILINE)
    toc = ["## Table of Contents"]
    for heading in headings:
        indent_level = len(heading.split(" ")[0]) - 2  # Subtract 2 for '##' base level
        title = heading[indent_level + 2 :].strip()
        anchor = (
            title.lower()
            .replace(" ", "-")
            .replace(".", "")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
        )
        toc.append(f"{'  ' * indent_level}- [{title}](#{anchor})")
    return "\n".join(toc) + "\n\n"


def insert_or_replace_toc_in_markdown(file_path):
    """
    Inserts or replaces the Table of Contents in the markdown file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    toc_start = content.find("## Table of Contents")
    toc_end = content.find("## ", toc_start + 1)
    new_toc = generate_toc(content)

    if toc_start != -1 and toc_end != -1:
        # Replace existing ToC
        updated_content = content[:toc_start] + new_toc + content[toc_end:]
    else:
        # Insert new ToC
        updated_content = re.sub(r"(#+ .+?\n)", r"\1" + new_toc, content, 1)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Table of Contents updated in {file_path}")


def main():
    file_path = input("Enter the path of the Markdown file: ")
    insert_or_replace_toc_in_markdown(file_path)


if __name__ == "__main__":
    main()
