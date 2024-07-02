#!/bin/bash

# Check if the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting..." >&2
    exit 1
fi

# Check if an input file is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Assign the input file path from the argument
INPUT_FILE=$1

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file $INPUT_FILE does not exist." >&2
    exit 1
fi

# Define the log file path
LOG_FILE="/var/log/user_management.log"
SECURE_DIR="/var/secure"
SECURE_FILE="$SECURE_DIR/user_passwords.csv"

# Ensure the secure directory exists
if [ ! -d "$SECURE_DIR" ]; then
    mkdir -p "$SECURE_DIR"
    chmod 700 "$SECURE_DIR"
fi

# Ensure the secure file exists
if [ ! -f "$SECURE_FILE" ]; then
    touch "$SECURE_FILE"
    chmod 600 "$SECURE_FILE"
fi

# Start logging
exec &>>$LOG_FILE

# Read the input file line by line
while IFS=';' read -r username groups password; do
    if [[ -z "$username" || -z "$groups" ]]; then
        echo "$(date): Skipping invalid line: $username;$groups;$password" | tee -a "$LOG_FILE"
        continue
    fi

    # Split the groups by comma
    IFS=',' read -ra group_array <<< "$groups"

    # Create the user
    if ! id "$username" &>/dev/null; then
        useradd "$username"
        echo "$(date): Created user $username" | tee -a "$LOG_FILE"
    else
        echo "$(date): User $username already exists." | tee -a "$LOG_FILE"
    fi

    # Create a group with the same name as the username
    GROUPNAME="$username"
    if ! getent group "$GROUPNAME" &>/dev/null; then
        groupadd "$GROUPNAME"
        echo "$(date): Created group $GROUPNAME" | tee -a "$LOG_FILE"
    else
        echo "$(date): Group $GROUPNAME already exists." | tee -a "$LOG_FILE"
    fi

    # Add the user to the primary group and any additional groups
    usermod -aG "$GROUPNAME" "$username"
    for group in "${group_array[@]}"; do
        group=$(echo "$group" | xargs)  # Trim whitespace
        if [[ "$group" != "$GROUPNAME" ]]; then
            if getent group "$group" &>/dev/null; then
                usermod -aG "$group" "$username"
                echo "$(date): Added $username to group $group" | tee -a "$LOG_FILE"
            else
                echo "$(date): Group $group does not exist. Skipping addition to this group." | tee -a "$LOG_FILE"
            fi
        fi
    done

    # Set up home directory
    mkdir -p "/home/$username"
    chown "$username:$GROUPNAME" "/home/$username"
    chmod 700 "/home/$username"
    echo "$(date): Set up home directory for $username" | tee -a "$LOG_FILE"

    # Generate a random password if the user was newly created and no password was provided
    if ! grep -q "$username" "$SECURE_FILE"; then
        if [ -z "$password" ]; then
            PASSWORD=$(openssl rand -base64 32)
        else
            PASSWORD=$password
        fi
        echo "$username,$PASSWORD" >> "$SECURE_FILE"
        echo "$(date): Generated and stored password for $username" | tee -a "$LOG_FILE"
    fi

done <"$INPUT_FILE"

