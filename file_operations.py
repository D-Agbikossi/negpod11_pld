#!/usr/bin/python3
import os
import shutil

# File paths
data_file = "volunteer_opportunities.txt"
backup_folder = "backups"

# Ensure the backup folder exists
os.makedirs(backup_folder, exist_ok=True)

# Function to add a new volunteer opportunity
def add_volunteer_opportunity(name, contact_detail, opportunity):
    volunteer_data = f"Name: {name}, Contact: {contact_detail}, Opportunity: {opportunity}\n"

    # Append new data to the file
    with open(data_file, 'a') as file:
        file.write(volunteer_data)

    print(f"Volunteer opportunity added for {name}.")

# Function to get the next backup file name using an incremental counter
def get_next_backup_file_name(backup_folder):
    existing_backups = [f for f in os.listdir(backup_folder) if os.path.isfile(os.path.join(backup_folder, f))]
    existing_backups.sort()

    if existing_backups:
        last_backup = existing_backups[-1]
        last_backup_number = int(last_backup.split('_')[0])
        next_backup_number = last_backup_number + 1
    else:
        next_backup_number = 1

    return os.path.join(backup_folder, f"{next_backup_number}_volunteer_opportunities.txt")

# Function to back up the volunteer opportunities file
def backup_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    backup_file_path = get_next_backup_file_name(backup_folder)

    shutil.copy(file_path, backup_file_path)
    print(f"Backup created: {backup_file_path}")

# Function to display all volunteer opportunities
def display_volunteer_opportunities():
    if not os.path.exists(data_file):
        print("No volunteer opportunities found.")
        return

    with open(data_file, 'r') as file:
        data = file.readlines()

    for entry in data:
        print(entry.strip())

# Function to handle volunteer sign-ups
def volunteer_opportunities():
    print("\nDo you want to volunteer with us?")
    print("1. Community Clean-Up")
    print("2. Food Distributor")
    print("3. Legal Assistant")
    print("4. Medic")
    print("5. Display all volunteer opportunities")
    choice = input("Choose an opportunity to volunteer for: ")

    if choice == '5':
        display_volunteer_opportunities()
        return

    name = input("Enter your name: ")
    contact_details = input("Enter your contact details: ")

    opportunities = {
        '1': 'Community Clean-Up',
        '2': 'Food Distributor',
        '3': 'Legal Assistant',
        '4': 'Medic'
    }

    if choice in opportunities:
        opportunity = opportunities[choice]
        print(f"Thank you, {name}. You have signed up for the volunteer opportunity {opportunity}. We will contact you at {contact_details}.")
        add_volunteer_opportunity(name, contact_details, opportunity)
    else:
        print("Invalid selection. Please try again.")
