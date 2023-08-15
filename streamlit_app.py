import streamlit as st

#### Define questions and point system
questions = {
    "1. What is your main source of income?": {
        "Uncertain source of income": 1,
        "Have a stable source of income": 2,
        "Have a stable and comfortable source of income": 3,
        "Have various sources of stable income": 4,
        "Having various sources of strong active and passive income": 5
    },
    "2. How are you budgeting your monthly expenses according to your income?": {
        "The amount of monthly expenses exceeds income": 1,
        "Budget monthly expenses according to income": 2,
        "Have a monthly surplus after expenses": 3,
        "Monthly expenses are much lower compared to income": 4,
        "One or two sources of income can cover monthly expenses": 5
    },
    "3. How much do you currently have in savings?": {
        "Not able to save": 1,
        "Able to save but do not have savings": 2,
        "Have savings equivalent to 1-6 months of income": 3,
        "Have savings equal to 6-12 months of income": 4,
        "Have a savings amount that exceeds the amount of 12 months of income": 5
    },
    "4. Do you own any assets for personal use?": {
        "No assets": 1,
        "Own assets for personal use": 2,
        "Own assets for personal use and some assets for investment purposes": 3,
        "Owning assets for own use and family members as well as various assets for investment purposes": 4,
        "Owning assets for personal use and family members as well as various assets that provide consistent returns": 5
    },
    "5.Are you able to pay off your debts with your current income?": {
        "Earned income is not able to pay debt": 1,
        "Earned income is able to pay off debt": 2,
        "Earned income is able to pay off debt and have excess funds after paying off debt": 3,
        "Earned income able to pay off debt and able to generate additional income": 4,
        "Free from debt": 5
    },
    "6.Do you have any insurance protection?": {
        "No insurance protection": 1,
        "Have minimum insurance protection for yourself or insurance coverage from the employer only": 2,
        "Have insurance protection equivalent to approximately the annual income for yourself and family members": 3,
        "Have insurance protection equivalent to twice or triple your annual income for yourself and family members": 4,
        "Have insurance protection exceeding three times the annual income for yourself and family members": 5
    },  
}

#### Define result categories and their details
result_categories = {
    "Financial Instability": {
        "range": (6, 12),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%201.JPG"
    },
    "Financial Stability": {
        "range": (13, 18),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%202.JPG",
    },
    "Financial Security": {
        "range": (19, 24),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%203.JPG"
    },
    "Financial Freedom": {
        "range": (25, 30),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%204.JPG"
    },
    "Financial Wealth": {
        "range": (31, 36),
         "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%205.JPG"
    },
}

#### create streamlit app
def main():
    st.title("Financial Health Calculator")

    question_number = 0
    total_points = 0

    for question, options in questions.items():
        st.write(question)
        selected_option = st.radio("Select an option:", [''] + list(options.keys()), key=question_number)
        if selected_option:
            total_points += options[selected_option]
        question_number += 1

    if question_number == len(questions):
        if st.button("Calculate"):
            st.write("Calculating result...")
            result_category = calculate_result_category(total_points)
            display_result(result_category)

def calculate_result_category(total_points):
    for category, details in result_categories.items():
        if details["range"][0] <= total_points <= details["range"][1]:
            return category

def display_result(result_category):
    st.subheader("Result:")
    if result_category:
        st.write(f"Based on your responses, you are in the stage of '{result_category}' category.")
        result_image = result_categories[result_category].get("image")
        if result_image:
            st.image(result_image, caption="Category Image", use_column_width=True)

if __name__ == "__main__":
    main()
