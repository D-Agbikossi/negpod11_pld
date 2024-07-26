#!/usr/bin/python3
""" This class records brutality incidents """

class BrutalityIncident:
    def __init__(self):
        """Initializes the attributes of the BrutalityIncident class"""
        self.user_name = ""
        self.age = ""
        self.date = ""
        self.location = ""
        self.role = ""
        self.situation_description = ""

    def gather_info(self):
        """Gathers information about the brutality incident from the user"""
        self.user_name = input("Please write your name and surname: ")
        self.age = input("Please write your age: ")
        self.location = input("Where is the incident venue? Please give a location or a landmark within 1km if you are in doubt: ")

        # Prompt the user to specify when the incident occurred
        date_prompt = "Please choose one of the following options:\n"
        date_prompt += "1. The incident is happening now. I require immediate assistance.\n"
        date_prompt += "2. The incident is happening now. I do not need immediate assistance.\n"
        date_prompt += "3. The incident took place in the past."
        self.date = input(date_prompt)

        # Prompt the user to specify their role in the incident
        role_prompt = "Please choose one of the following options:\n"
        role_prompt += "1. I am the victim\n"
        role_prompt += "2. I am a witness\n"
        role_prompt += "3. I am a culprit"
        self.role = input(role_prompt)

        # Prompt the user to describe the situation
        self.situation_description = input("Please briefly describe the incident. Do not leave out any details. Specify the date or period if the incident took place in the past: ")

    def display_summary(self):
        """Displays a summary of the gathered information"""
        print("\nSummary of the information provided:")
        print(f"Name: {self.user_name}")
        print(f"Age: {self.age}")
        print(f"Date: {self.date}")
        print(f"Location: {self.location}")
        print(f"Role in the event: {self.role}")
        print(f"This is what happened: {self.situation_description}")

         # If the incident is happening now and immediate assistance is required, provide emergency contact information
        if self.date == '1':
            print("\nCall one of the following services according to your need:\nPolice: 911\nEmergency: 112\nFire department: 101")

        print("Thank you for reporting this incident. You will receive updates on progress when we start examining your case.")

# 2
#!/usr/bin/python3
""" Script to record brutality incidents """

def gather_info():
    """Gathers information about the brutality incident from the user"""
    user_info = {}

    user_info['user_name'] = input("Please write your name and surname: ")
    user_info['age'] = input("Please write your age: ")
    user_info['location'] = input("Where is the incident venue? Please give a location or a landmark within 1km if you are in doubt: ")

    date_prompt = "Please choose one of the following options:\n"
    date_prompt += "1. The incident is happening now. I require immediate assistance.\n"
    date_prompt += "2. The incident is happening now. I do not need immediate assistance.\n"
    date_prompt += "3. The incident took place in the past."
    user_info['date'] = input(date_prompt)

    role_prompt = "Please choose one of the following options:\n"
    role_prompt += "1. I am the victim\n"
    role_prompt += "2. I am a witness\n"
    role_prompt += "3. I am a culprit"
    user_info['role'] = input(role_prompt)

    user_info['situation_description'] = input("Please briefly describe the incident. Do not leave out any details. Specify the date or period if the incident took place in the past: ")

    return user_info

def display_summary(user_info):
    """Displays a summary of the gathered information"""
    print("\nSummary of the information provided:")
    print(f"Name: {user_info['user_name']}")
    print(f"Age: {user_info['age']}")
    print(f"Date: {user_info['date']}")
    print(f"Location: {user_info['location']}")
    print(f"Role in the event: {user_info['role']}")
    print(f"This is what happened: {user_info['situation_description']}")

    if user_info['date'] == '1':
        print("\nCall one of the following services according to your need:\nPolice: 911\nEmergency: 112\nFire department: 101")

    print("Thank you for reporting this incident. You will receive updates on progress when we start examining your case.")
