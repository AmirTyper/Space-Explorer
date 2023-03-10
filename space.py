import requests
import colorama
from termcolor import cprint
import os
import datetime
import time

# Clearing the terminal (or cmd)
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
clear()

cool_loadup = """
                         /\             
                        /  \            
                       /    \           
                      /      \          
                     /________\         
                   / \        / \       
                  /   \      /   \      
                 /     \    /     \     
                /_______\  /_______\    
                   |   |      |   |     
                   |---|      |---|     
                   |---|      |---|     
                   |   |      |   |     
                   |---|      |---|     
                   '---'      '---'     
                    /   \  /    \       
                   / / \ \/ / \  \       
                   \_\__/  \__/_/      
                         /\       
                        /  \       
                       /    \     
                      /      \        
                     /________\      
"""

cprint(cool_loadup,"yellow")
time.sleep(2)
clear()
welcome = """
|||||             ~ Space Explorer ~            |||||
 ||||           Coded By : AmirTyper            ||||
  |||         My Instagram : @amir_typer        |||
   ||        https://github.com/AmirTyper       ||
    |                     V1                    |
"""
print(welcome)

# Initialize colorama for cross-platform console coloring
colorama.init()

# Make request to the APIs
people_response = requests.get('http://api.open-notify.org/astros.json')
ISS_response = requests.get('http://api.open-notify.org/iss-now.json')

all_people = 0

if people_response.status_code == 200:
    data = people_response.json()
    cprint(f"|+| Number of people that are currently in space: {data['number']}\n","cyan")
    time.sleep(0.8)
    for person in data['people']:
        all_people = all_people + 1
        # Print the data that have been received
        print(f"-| {str(all_people)}. {person['name']}, is on the {person['craft']}")
else:
        cprint(f"|!| Unsuccessful request. Error code: {people_response.status_code}","red")
            
if ISS_response.ok:
    # Extract the current coordinates of the ISS from the response
    data = ISS_response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp'] # timestamp in seconds
    dt_object = datetime.datetime.fromtimestamp(timestamp) 
    formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S") # converting seconds to real time.
    # Print the data received
    time.sleep(0.8)
    cprint(f"\n|~| The International Space Station (ISS) is currently located at {latitude}, {longitude}", "magenta")
    time.sleep(0.8)
    cprint(f"|~| The data was updated on {timestamp} | {formatted_time}\n", "magenta")
    time.sleep(0.4)
    cprint("|+| Done!, See you soon.\n","cyan")
else:
    # Give a clear error message if data is not available
    cprint("|!| Error: Unable to retrieve data from the API.", "red")

# Clean up colorama before exiting
colorama.deinit()