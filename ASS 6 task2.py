import json

state_capitals = {
    "Andhra pradesh": "Amaravathi",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur",
    "Telangana": "Hyderabad"
}

with open('indian_states.json', 'w') as file:
    json.dump(state_capitals, file, indent=4)

print("JSON file created successfully.")
