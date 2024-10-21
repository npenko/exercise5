import random
import time
import threading


# Global variable to store the list of names
last_word = []

# Step 1: Tell players to stand
print("Players stand")

# Step 2: Function to sleep for a random time
def sleep_random_time():
    set_time = random.randint(10, 25)
    print("Players can sit down!")
    time.sleep(set_time)
    print("Time's up!")
    
    # Step 4: After waking up, print the last name entered
    if names_list:  # Ensure there's at least one name
        print(f"The winner is: {last_word[-1]}")  # Last name entered wins
    else:
        print("No one entered a name!")
    
 
# Function to handle user input
def get_user_input():
    global last_word
    while True:
        user_input = input("Enter a player's name: ")
        if user_input:  # Append the name if the input is not empty
            last_word.append(user_input)

# Step 3: Start the thread for user input
input_thread = threading.Thread(target=get_user_input)
input_thread.daemon = True  # This ensures the input thread stops when the main thread finishes
input_thread.start()

# Sleep for a random amount of time
sleep_random_time()


