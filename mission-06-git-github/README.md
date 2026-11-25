
# Mission 6 — Git and GitHub

## 1. Task / objective
The objective was to understand version control, practise Git commands, create a branch and open a Pull Request on GitHub.

## 2. Work completed
- Checked the Git repository status.
- Organised the assignment as nine commits in mission order, with the initial setup as the first commit.
- Created the `update-about` branch and opened a Pull Request to the default branch so the mission history can be reviewed and merged.

### Git workflow
| Git operation | Purpose |
|---|---|
| `git init` | Initialises a Git repository |
| `git status` | Shows the current changes |
| `git add` | Stages selected changes |
| `git commit` | Saves staged changes in Git history |
| `git log` | Displays commit history |
| `git branch` | Lists or creates branches |
| `git switch` | Changes the current branch |
| `git push` | Publishes commits to a remote repository |
| `git pull` | Retrieves and integrates remote changes |

### Branch and Pull Request
A branch is a separate line of development where changes can be made without directly changing the main branch.

A Pull Request is a request to review and merge changes from one branch into another. It helps people discuss and check changes before they become part of the main project.

### Difference between add and commit
`git add` selects changes and places them in the staging area. `git commit` saves the staged changes as a recorded point in the repository history.

## 3. Commands / tools used
- `git status`
- `git add`
- `git commit`
- `git log`
- `git branch`
- `git switch`
- `git push`
- `git pull`
- GitHub website — to create and view the Pull Request.

## 4. My understanding
I learned that Git tracks changes in a project, while GitHub hosts repositories online and supports collaboration. Branches allow separate work, and Pull Requests help review changes before merging them.

## 5. Difficulties faced
A challenge was understanding why `git add` and `git commit` are separate steps.

## 6. How I resolved them
I used `git status` to see which files were staged, then committed them and reviewed the history with `git log`.

## 7. Evidence / files
- Updated root `README.md`
- Git commit history
- `update-about` branch
- Opened [Pull Request #1](https://github.com/cherryx18/digital-detective-8455/pull/1) from `update-about` into `main` and merged it using GitHub’s rebase option.
- PR status: merged into `main` using rebase; the mission history remains nine commits.

## 8. Commit details
Commit message: Complete Git and GitHub collaboration mission.
GitHub repository: [cherryx18/digital-detective-8455](https://github.com/cherryx18/digital-detective-8455).
