---
# Metadata
date: "2023-11-22"
author: superQ
document_type: toolDocumentation
tags: [Python, Script, HTML, Index Generation]
---

# GenerateIndexHTML.py

## Overview

- This script is designed to generate an index HTML file from a specified source directory.
- It's used to automate the creation of a structured HTML file that lists all files and directories in the source location.
- Key features include automatic scanning of directory contents, HTML template rendering, and optional sorting functionalities.

## Script Functionality

- Scans a specified directory to identify all files and subdirectories.
- Utilizes a predefined HTML template to format the output.
- Offers options to sort the listed items alphabetically, by file type, or by date modified.
- Generates a single index.html file that provides a navigable view of the directory's contents.

## Purpose

- The primary purpose of this script is to streamline the creation of an index HTML file for directory listings.
- It provides a user-friendly interface to browse directory contents, useful for internal documentation and project management.

## Usage

- Run the script with the command `python generateIndexHTML.py <source_directory_path>`.
- Optional arguments can be provided for sorting preferences.
- Ensure that the script has read access to the specified directory and write access to the output location.
- Common use case scenario: Generating an index file for the `superPosition/lab` directory to facilitate easy navigation.

## Output Example

- The output is an `index.html` file with a structured, navigable list of files and directories.
- Sample output for a directory containing `README.md`, `script.py`, and `data` folder:

  ```html
  <ul>
    <li><a href="README.md">README.md</a></li>
    <li><a href="script.py">script.py</a></li>
    <li><a href="data/">data</a></li>
  </ul>
  ```

## Notes

- The script does not currently support deep scanning of nested directories.
- For large directories, the script may take longer to execute.
- Future updates may include more advanced sorting options and enhanced HTML templates.
