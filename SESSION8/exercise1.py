# Define an empty dictionary
service_dict = {}

# Create the items for the dictionary
service_dict={"HTTP":80, "DNS":53, "FTP":21, "SMTP":25, "POP3":110}

# Enter a key to check if it is existing in the dictionary or not
checked_service=input("Enter a key of dictionary you would like to check:")
# Get all current keys of the dictionary
key_list=service_dict.keys()

# Check

if checked_service in key_list:
    print(f"The key '{checked_service}' exists in the dictionary.")
else:
    print(f"The key '{checked_service}' does not exist in the dictionary.")