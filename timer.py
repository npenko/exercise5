"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""
import random
import time
import threading
from PIL import Image
# Step 1: Tell players to stand 
print("Players stand")
# Global variable to store the last word entered
last_word = []
# Step 2: Function to sleep for a random time
def sleep_random_time():
    set_time = random.randint(10, 25)
    time.sleep(set_time)
    game_active = True
   print("While timer is running, players can sit down.") 
 # step 4: keep track of the people who sat down
    people_sitting = []
# Start the thread for user input
input_thread = threading.Thread(target=get_user_input)
input_thread.start()

# Function to handle user input
def get_user_input():
    global last_word
    while True:
        user_input = input("Enter a word: ")
        if user_input:  # Update the last word if the input is not empty
            last_word = user_input.split()[-1]  # Get the last word entered


# Start the thread for user input
#input_thread = threading.Thread(target=get_user_input)
#input_thread.daemon = True  # Daemon thread will automatically exit when the main thread ends
#input_thread.start()

# Sleep for a random amount of time
#sleep_random_time()
image = Image.open('times-up.jpg')
image.show()
# After waking up, print the last word entered
print(f"The winner is: {last_word}")


