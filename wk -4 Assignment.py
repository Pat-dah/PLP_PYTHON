# Create input.txt and write data into it
with open("input.txt", "w") as file:
    file.write("office opens by 8am \n")
    file.write("lateness is not allowed \n")
    file.write("Office opens Monday to Friday \n")
    file.write("Saturdays office closes by 2pm \n")
    file.write("Please Work is Important \n")
print(" input.txt created successfully!")

# Read the contents of input.txt
with open("input.txt", "r") as file:
    data = file.read()
    print("\nFile Contents:\n", data)

# Count the number of words in the file
word_count = len(data.split())
print("\n Word Count:", word_count)

# Convert all text to uppercase
new_data = data.upper()
print("\n Uppercase Version:\n", new_data)

# Write the processed text and the word count to a new file called output.txt
with open("output.txt", "w") as file:   # 
    file.write("Processed Text:\n")
    file.write(new_data + "\n\n")
    file.write(f"Word Count: {word_count}\n")
print(" output.txt created successfully!")

# Ask user for filename and handle errors
filename = input("\nWhat is the file name you want to open? ")

try:
    with open(filename, "r") as file:   #  now uses user input
        content = file.read()
        print("\n File opened successfully!\n")
        print(content)
except FileNotFoundError:
    print("\n Error: File not found. Please check the filename.")
