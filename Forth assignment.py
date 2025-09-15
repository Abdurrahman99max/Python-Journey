import os

# File Read & Write Challenge with User Input

# Step 1: Define the file name
filename = "shopping_list.txt"

# Step 2: Check if the file exists, if not, create it
if not os.path.exists(filename):
    print("📂 File not found. Creating a new shopping list...")
    with open(filename, "w") as file:
        file.write("Bread\nEgg\nFish\nRice\nBeans\n")
    print(f"✅ {filename} has been created with default items.")

# Step 3: Ask the user if they want to add new items
choice = input("Would you like to add new items to the shopping list? (yes/no): ").strip().lower()

if choice == "yes":
    new_items = input("Enter new items separated by commas (e.g., Milk, Sugar, Butter): ")
    new_items_list = [item.strip() for item in new_items.split(",") if item.strip()]
    
    # Append new items to the shopping list file
    with open(filename, "a") as file:
        for item in new_items_list:
            file.write(item + "\n")
    print("✅ New items have been added to the shopping list.")

# Step 4: Read the updated file
try:
    with open(filename, "r") as file:
        lines = file.readlines()

    # Step 5: Modify the content (add numbering)
    modified_lines = []
    for i, line in enumerate(lines, start=1):
        modified_lines.append(f"{i}. {line.strip()}\n")

    # Step 6: Save the modified list to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.writelines(modified_lines)

    print(f"✅ Success! Modified shopping list saved to {new_filename}")

except PermissionError:
    print("❌ Error: You don't have permission to open this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")


