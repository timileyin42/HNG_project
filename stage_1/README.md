# User Management Script

## Description

This project provides a Bash script, `create_users.sh`, for managing user accounts on a Unix-based system. The script reads an input file containing user details and performs actions such as creating users, adding them to groups, and setting up their home directories. It also generates random passwords for newly created users and logs all actions for auditing purposes.

## Features

- Create users and their primary groups.
- Add users to multiple groups.
- Generate random passwords for users.
- Log all actions to a log file.
- Handle various test cases including duplicate users, multiple groups, and invalid formats.

## Requirements

- Unix-based system (Linux, macOS, etc.)
- Bash shell
- Root privileges to run the script
- OpenSSL (for password generation)

## Usage

### 1. Preparation

Ensure you have root privileges to execute the script. The script must be run as root to perform user management tasks.

### 2. Input File

Create an input file with user details. Each line in the file should contain the username, primary group, and optionally a password, separated by semicolons (`;`).

