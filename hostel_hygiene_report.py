print("#### Hostel Hygiene Report System ####")


name = input("Enter Student Name: ")
reg_no = input("Enter Registration Number: ")
gender = input("Enter Gender (Boy/Girl): ").strip().lower()

print("\nSelect Your Hostel Block:")

if gender == "boy":
    blocks = [
        "Block 1", "Block 2", "Block 3", "Block 4",
        "Block 5", "Block 6", "Block 7", "Block 8A",
        "Amenity Block 1", "Amenity Block 2"
    ]
elif gender == "girl":
    blocks = ["Block 1", "Block 2"]
else:
    blocks = []


for i in range(len(blocks)):
    print(f"{i+1}. {blocks[i]}")

block_choice = int(input("Enter block number: "))
hostel_block = blocks[block_choice - 1]

room_no = input("Enter your Room Number (Like:A001):")
final_reports = []

while True:
    print("\nChoose a category to report:")
    print("1. Water Quality")
    print("2. Food Quality")
    print("3. Cleanliness")
    print("4. Kitchen/mess Hygiene")
    print("5. Waste Management")
    print("6. Complaints / Feedback")
    print("7. finish (no more)")

    choice = input("Enter your choice (1-7): ")

    if choice in ["1","2","3","4","5"]:
        
        categories = {
            "1": "Water Quality",
            "2": "Food Quality",
            "3": "Cleanliness",
            "4": "Kitchen/mess Hygiene",
            "5": "Waste Management"
        }
        category_name = categories[choice]
        rating = input(f"Rate {category_name} (Good/Average/Poor): ")
        feedback = input(f"Describe any problem / give feedback for {category_name} (or type 'None'): ")
        final_reports.append(f"{category_name}: {rating}\nFeedback: {feedback}")

    elif choice == "6":
        comp = input("Enter Complaint / Feedback: ")
        final_reports.append(f"Complaint / Feedback: {comp}")

    elif choice == "7":
        print("\nFinishing reporting...")
        break

    else:
        print("Invalid choice! Try again.")


print("\n######## FINAL HYGIENE REPORT ########")
print(f"Student Name     : {name}")
print(f"Registration No. : {reg_no}")
print(f"Gender           : {gender.capitalize()}")
print(f"Hostel Block     : {hostel_block}")
print(f"Room No     : {room_no}")
print("--------------------------------")

for rep in final_reports:
    print(rep)
    print("--------------------------------")

print("############# END OF REPORT #############")

