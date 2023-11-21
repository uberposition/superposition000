import os


def generate_markdown_tree(dir_path, prefix=""):
    """
    Generates a markdown tree structure for the given directory path.

    :param dir_path: The path of the directory to generate the tree for.
    :param prefix: The prefix used for formatting the tree structure.
    """
    if not os.path.isdir(dir_path):
        raise ValueError(f"The provided path '{dir_path}' is not a valid directory.")

    files = sorted(os.listdir(dir_path))
    for i, file in enumerate(files):
        # Check if it's the last file or directory in the list
        is_last = i == (len(files) - 1)

        # Determine the prefix for the current item and its children
        current_prefix = prefix + ("└── " if is_last else "├── ")
        children_prefix = prefix + ("    " if is_last else "│   ")

        print(f"{current_prefix}{file}")

        # Recurse into directories
        full_path = os.path.join(dir_path, file)
        if os.path.isdir(full_path):
            generate_markdown_tree(full_path, children_prefix)


def main():
    dir_path = input("Enter the directory path to generate its markdown tree: ")
    print(f"Markdown Tree for '{dir_path}':\n")
    generate_markdown_tree(dir_path)


if __name__ == "__main__":
    main()
