# Step 14 — Read greeting from file and display it
try:
    with open("greeting.txt", "r") as file:
        content = file.read()
        print("\n--- Saved Greeting ---")
        print(content)
except FileNotFoundError:
    print("No saved greeting found. Please run Step 13 first to create one.")