
# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
The objective was to practise Terminal commands, manage files and folders safely, understand command flags and pipes, and learn about package managers.

## 2. Work completed
I practised these operations inside my assignment repository:

| Operation | Command | Purpose |
|---|---|---|
| Show current folder | `pwd` | Displays the current directory path |
| List files | `ls` | Shows files and folders |
| Detailed listing | `ls -l` | Shows detailed file information |
| Parent folder | `cd ..` | Moves to the parent directory |
| Create folder | `mkdir` | Creates a directory |
| Create file | `touch` | Creates an empty file |
| Copy file | `cp` | Makes a copy |
| Move/rename | `mv` | Moves or renames a file |
| Display contents | `cat` | Displays file contents |

I practised by creating the `terminal-practice` folder, writing two lines in `practice.txt`, displaying the file, copying it, and renaming the copy to `practice-backup.txt`. The example files are included in the repository.

## 3. Commands / tools used
- `pwd` — displays the current working directory.
- `ls` and `ls -l` — list files and folders.
- `cd` — changes the current directory.
- `mkdir` — creates a folder.
- `touch` — creates an empty file.
- `cp` — copies a file.
- `mv` — moves or renames a file.
- `cat` — displays file contents.
- `ls -lah` — displays detailed information, including hidden files, with readable file sizes.
- `ls -lah | head` — sends the listing to `head`, which displays its first few lines.

## 4. My understanding
The Terminal allows us to control the computer by entering commands. Copying creates another version of a file, while moving changes its location. Adding text to the end preserves the existing content, whereas replacing content removes the previous text. A flag changes how a command works, and a pipe (`|`) sends the output of one command to another command.

A package manager helps users manage software. Homebrew is installed on this Mac; `brew --version` reported version 7.0.16.

## 5. Difficulties faced
At first, it was easy to mix up copying a file with moving or renaming it.

## 6. How I resolved them
I checked the result after each command with `ls` and `cat`. This helped me confirm that the original file stayed in place and that the backup had the expected contents and name.

## 7. Evidence / files
- `terminal-practice/` folder
- Practice text file and renamed backup
- This README with command explanations

## 8. Commit details
Commit message: Complete Terminal and file management mission.
GitHub repository: [cherryx18/digital-detective-8455](https://github.com/cherryx18/digital-detective-8455).
