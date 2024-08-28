

# Automated File Sorting System

This Python script organizes files in a specified directory (e.g., the Downloads folder) into categorized subfolders based on their file extensions. It's designed to help you keep your files organized and reduce clutter in your directories.

## Features

- Automatically creates subfolders for different file types (e.g., Documents, Images, Videos, Music, Archives).
- Moves files into the appropriate subfolder based on their extension.
- Places files with unknown or uncategorized extensions into a "Miscellaneous" folder.
- Provides feedback on whether the operation was successful or if any errors occurred.



 When prompted, enter the full path to the directory you want to sort (e.g., your Downloads folder):

```plaintext
Enter the source directory: C:\Users\YourUsername\Downloads
```

 The script will automatically sort the files in the specified directory into appropriate subfolders.

### 3. Output

- **Success Message**: If the files are sorted successfully, you will see the message `Files have been successfully sorted.`.
- **Error Handling**: If an error occurs, the script will print an error message describing what went wrong.

## Customization

### Add or Modify File Categories

You can customize the categories and file extensions by editing the `target_dirs` dictionary in the script:

```python
target_dirs = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
}
```

### Running the Script Automatically

If you'd like the script to run automatically at regular intervals:

1. **Windows Task Scheduler**: You can set up a task in Windows Task Scheduler to run the script daily, weekly, etc.
2. **Cron Job (Linux/MacOS)**: You can add a cron job to schedule the script to run at specific times.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## Support

If you have any questions or need support, feel free to open an issue in the GitHub repository.

---

This `README.md` file should guide users on how to use, customize, and contribute to your automated file sorting system. Adjust the details as needed to fit your project.
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    