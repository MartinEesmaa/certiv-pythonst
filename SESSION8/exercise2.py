# Define an empty dictionary
service_dict = {}

# Create the items for the dictionary
service_dict={"HTTP":80, "DNS":53, "FTP":21, "SMTP":25, "POP3":110}
print("The dictionary before sorting is: ", service_dict)

# Sort the dictionary by keys
sorted_dict = dict(sorted(service_dict.items()))
print("The dictionary after sorting is: ", sorted_dict)