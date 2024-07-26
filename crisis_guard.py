#!/usr/bin/env python3


def report_medical_emergency():
    print("\nReporting a Medical Emergency\n")

    # Collecting information about the user
    user_name = input("What is your name? ")
    location = input("What is your location? ")
    prompt = f"{user_name}, are you reaching out for yourself or someone else?\n"
    prompt += "Please choose:\n"
    prompt += "1- Self\n"
    prompt += "2- Others\n"

    relation_to_victim = input(prompt).strip().lower()

    # Scenario 1: The victim is the one calling
    if relation_to_victim == "1":
        print("What happened?")
        print("1- I have been shot")
        print("2- I have been exposed to tear gas")
        print("3- I am badly burned")
        print("4- I have been exposed to a chemical")
        print("5- Other (please describe)")
        situation_description = input("Please select one number above: ").strip().lower()

        # Handling the different cases when the victim is the one calling:
        if situation_description == "1":
            print(f"{user_name}, you have been shot. Apply pressure to the wound with a clean cloth or bandage to control bleeding. Do not remove any objects stuck in the wound. If you can, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "2":
            print(f"{user_name}, you have been exposed to tear gas. Leave the vicinity of tear gas as swiftly as possible to reduce exposure. Upon reaching fresh air, rinse your eyes and face with water to mitigate irritation. Avoid rubbing your face and ensure the water flows off without re-entering your eyes. Call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "3":
            print(f"{user_name}, you are badly burned. Move to a safe, cool environment away from the source of the fire. Call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "4":
            print(f"{user_name}, you have been exposed to a chemical. If you have breathed in the chemical, immediately move to fresh air. If this chemical contacts the skin, flush the contaminated skin with water promptly. If the chemical has been ingested, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "5":
            other_description = input("Please describe your situation: ")
            print(f"{user_name}, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        else:
            print("Invalid selection. Please try again.")

    # Scenario 2: The victim is not the one calling
    elif relation_to_victim == "2":
        print(f"\nChoose the option that describes the emergency:\n")
        print("1. The person has been shot")
        print("2. The person is unconscious")
        print("3. The person is choking")
        print("4. The person is having difficulty breathing")
        print("5. The person has been in contact with chemicals")
        print("6. Other (please describe)")

        # Getting the user's choice
        emergency_choice = input(f"{user_name}, please enter the corresponding number for the emergency: ").strip()

        # Handling different emergency scenarios when the victim is not the one calling
        if emergency_choice == '1':
            print(f"\n{user_name}, for a gunshot wound, apply pressure to the wound with a clean cloth or bandage to control bleeding. Do not remove any objects stuck in the wound. Call 112 immediately and inform them of the situation. We have also connected you to emergency services.")

        elif emergency_choice == '2':
            print(f"\n{user_name}, for an unconscious person, check if they are responsive. If not, roll them onto their side to prevent choking on vomit or saliva. Call 112 immediately. We have also connected you to emergency services.")

        elif emergency_choice == '3':
            print(f"\n{user_name}, for choking, perform the Heimlich maneuver (if you have been trained) if the person is unable to breathe. Call 112 immediately after performing the maneuver. We have also connected you to emergency services.")

        elif emergency_choice == '4':
            print(f"\n{user_name}, for difficulty breathing, sit the person upright and keep them comfortable. Administer oxygen if available. Call 112 immediately. We have also connected you to emergency services.")

        elif emergency_choice == '5':
            print(f"\n{user_name}, for exposure to poisonous chemicals, if the person has breathed in a chemical, immediately move them to fresh air. If this chemical touched the skin, flush the contaminated skin with water promptly. If the chemical has been ingested, call 112 immediately and inform them of the situation. We have also connected you to emergency services.")

        elif emergency_choice == '6':
            other_description = input(f"{user_name}, please describe the emergency: ").strip()
            print(f"\n{user_name}, for '{other_description}', here are some general steps: Call 112 immediately and stay on the line with the dispatcher. They will guide you through the initial steps until help arrives. We have also connected you to emergency services.")

        else:
            print(f"\n{user_name}, invalid option selected. Please try again.")

    # A wrong option has been selected
    else:
        print("Invalid selection. Please select between 1 and 2. Note that the emergency number is 112.")

""" Script to record brutality incidents """

def report_incident():
    """Gathers information about the brutality incident from the user"""
    user_info = {}

    user_info['location'] = input("Where is the incident venue? Please give a location or a landmark within 1km if you are in doubt: ")

    # Prompt the user to specify when the incident occurred
    date_prompt = "Please choose one of the following options:\n"
    date_prompt += "1. The incident is happening now. I require immediate assistance.\n"
    date_prompt += "2. The incident is happening now. I do not need immediate assistance.\n"
    date_prompt += "3. The incident took place in the past."
    user_info['date'] = input(date_prompt)

    # Prompt the user to specify their role in the incident
    role_prompt = "Please choose one of the following options:\n"
    role_prompt += "1. I am the victim\n"
    role_prompt += "2. I am a witness\n"
    role_prompt += "3. I am a culprit"
    user_info['role'] = input(role_prompt)

    # Prompt the user to describe the situation
    user_info['situation_description'] = input("Please briefly describe the incident. Do not leave out any details. Specify the date or period if the incident took place in the past: ")

    # Displays a summary of the gathered information
    print("\nSummary of the information provided:")
    print(f"Date: {user_info['date']}")
    print(f"Location: {user_info['location']}")
    print(f"Role in the event: {user_info['role']}")
    print(f"This is what happened: {user_info['situation_description']}")

    # Provide emergency contact information if the incident is happening now
    if user_info['date'] == '1':
        print("\nCall one of the following services according to your need:\nPolice: 999\nEmergency: 911\nFire department: 112")

    print("Thank you for reporting this incident. You will receive updates on progress when we start examining your case.")

""" This function is to inform about the workshops and webinars available. """
def educational_workshops():
    print("\nEducational Workshops and Webinars")
    print("1. First Aid Training - July 5")
    print("2. Legal Rights Workshop - July 12")
    print("3. Community Organizing Webinar - July 19")
    choice = input("Enter the workshop number to get more details: ")
    if choice == '1':
        print("First Aid Training - July 5, 2 PM at Health Clinic")
    elif choice == '2':
        print("Legal Rights Workshop - July 12, 4 PM on X-Space")
    elif choice == '3':
        print("Community Organizing Webinar - July 19, 6 PM on X-space")
    else:
        print("Invalid choice, please try again.")

def request_legal_assistance():
    print("\nRequesting Legal Assistance\n")

    # Collecting information about the user
    user_name = input("What is your name? ")
    location = input("What is your location? ")
    contact_details = input("Enter your contact details: ")

    # Asking about the nature of the legal issue
    print("\nPlease describe the nature of your legal issue:")
    print("1. Arrest/Detention")
    print("2. Property Dispute")
    print("3. Employment Issue")
    print("4. Discrimination or Harassment")
    print("5. Other (please describe)")

    legal_issue = input("Please select one number above: ").strip().lower()

    # Handling the different cases for the legal issue
    if legal_issue == "1":
        print(f"{user_name}, we have recorded your request for legal assistance regarding an arrest or detention. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "2":
        print(f"{user_name}, we have recorded your request for legal assistance regarding a property dispute. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "3":
        print(f"{user_name}, we have recorded your request for legal assistance regarding an employment issue. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "4":
        print(f"{user_name}, we have recorded your request for legal assistance regarding discrimination or harassment. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "5":
        other_issue = input("Please describe your legal issue: ")
        print(f"{user_name}, we have recorded your request for legal assistance regarding '{other_issue}'. Our legal team will contact you at {contact_details} to provide support.")

    else:
        print("Invalid selection. Please try again.")

def volunteer_opportunities():
    print("\nDo you want to volunteer with us?")
    print("1. Community Clean-Up")
    print("2. Food Distribution")
    print("3. Legal assistant")
    print("4.Medic")
    choice = input("Choose an opportunity to volunteer for: ")
    name = input("Enter your name: ")
    contact_details = input("Enter your contact details: ")
    print(f"Thank you, {name}. You have signed up for the volunteer opportunity '{choice}'. We will contact you at {contact_details}.")

def community_events():
    print("\nCommunity Events\n")
    print("1. Neighborhood Meeting - July 10")
    print("2. Health Workshop - July 15")
    print("3. Safety Training - July 20")
    print("4. Blood drive - July 21st - July 30th")
    choice = input("\nEnter the event number to get more details: \n")
    if choice == '1':
        print("\n📍 Neighborhood Meeting - July 10, 5 PM at Community Center\n")
    elif choice == '2':
        print("\n📍 Health Workshop - July 15, 3 PM at Health Clinic\n")
    elif choice == '3':
        print("\n📍 Safety Training - July 20, 10 AM at Fire Station\n")
    elif choice == '4':
        print("\n📍 Blood donations - Everyday from July 21st to July 30th at Health Clinic from 9AM\n")
    else:
        print("Invalid choice, please try again.")

def local_resources_directory():
    print("\nLocal Resources Directory")
    print("1. Shelters")
    print("2. Food Banks")
    print("3. Mental Health Services")
    choice = input("\nEnter the resource type number to get more details: \n")
    if choice == '1':
        print("\nShelters: \n- Community Shelter: 123 Main St, Phone: 555-1234\n")
    elif choice == '2':
        print("\nFood Banks: \n- City Food Bank: 456 Elm St, Phone: 555-5678\n")
    elif choice == '3':
        print("\nMental Health Services: \n- Wellness Center: 789 Oak St, Phone: 555-9012\n")
    else:
        print("\nInvalid choice, please try again.\n")
