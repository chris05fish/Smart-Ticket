import re

# Sample category keywords for ticket categorization
category_keywords = {
    "IT Support": ["computer", "network", "software", "hardware"],
    "HR": ["hiring", "employee", "leave", "benefits"],
    "Facilities": ["office space", "maintenance", "security"],
    "Other": ["general inquiry", "feedback"],
}

def categorize_ticket(prompt):
    prompt = prompt.lower()

    for category, keywords in category_keywords.items():
        if any(keyword in prompt for keyword in keywords):
            return category

    return "Uncategorized"

def main():
    while True:
        user_input = input("Enter your ticket description (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        category = categorize_ticket(user_input)
        print(f"Your ticket is categorized as: {category}\n")

if __name__ == "__main__":
    main()

