
# Mission 3 — Understand the Operating System

## 1. Task / objective
The objective was to explore the operating system, running processes, storage, file paths and permissions, and understand the responsibilities of an operating system.

## 2. Work completed

### System information
| Information | What it tells us | My observation |
|---|---|---|
| Operating system | Which OS the computer uses | macOS (Darwin, based on the available environment) |
| Current account | Which account is active | Omitted to protect account privacy |
| Storage | Used and available disk space | The system reported about 16 GiB used and 824 GiB available on the main volume when checked. |
| System activity | Programs currently running | `top` reported 690 processes at the time of observation; 3 were running and 687 were sleeping. This changes over time. |

### Understanding processes
A process is a program that is currently running.

- PID means Process Identifier.
- It is a number used to identify a running process.
- Examples: a web browser and a text editor.

### File permissions
| Permission | Meaning |
|---|---|
| r — Read | Allows reading a file |
| w — Write | Allows changing a file |
| x — Execute | Allows running a file |

### Operating-system responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Manages running programs | Running a browser |
| Memory management | Manages RAM used by programs | Allocating memory to an application |
| Device management | Controls connected hardware | Managing a keyboard |
| File management | Organises files and folders | Saving a document |
| User interface / shell | Lets users interact with the computer | Terminal or desktop |
| Security and permissions | Controls access to files and resources | File access permissions |

### Paths
An absolute path gives the complete location of a file. A relative path gives its location in relation to the current directory.

- Absolute path example (account name omitted): `/Users/learner/Developer/S&AI/digital-detective-8455/mission-03-operating-system/README.md`
- Relative path (from the project root): `mission-03-operating-system/README.md`

## 3. Commands / tools used
- `uname` — checks operating-system information.
- `whoami` — displays the current account name. Do not publish its output.
- `df -h` — displays storage information.
- `top` — shows running system activity.
- `ps` — displays process information.
- `pwd` — displays the current directory.
- `ls -l` — displays file details and permissions.

## 4. My understanding
I learned that the operating system acts as a connection between the user, applications and computer hardware. It manages processes, memory, devices, files and security. Permissions help control who can read, change or execute files.

## 5. Difficulties faced
It took a little practice to tell an absolute path from a relative path.

## 6. How I resolved them
I compared the complete project path with the shorter path written from the project root. That made it clearer that the relative path depends on the current folder.

## 7. Evidence / files
- System information notes
- Process and permission observations
- This README

## 8. Commit details
Commit message: Document operating system and file management.
GitHub repository: [cherryx18/digital-detective-8455](https://github.com/cherryx18/digital-detective-8455).
