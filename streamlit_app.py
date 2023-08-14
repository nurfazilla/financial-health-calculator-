import streamlit as st

#### Define questions and point system
questions = {
    "1. What is your main source of income?": {
        "a.Uncertain source of income": 1,
        "b.Have a stable source of income": 2,
        "c.Have a stable and comfortable source of income": 3,
        "d.Have various sources of stable income": 4,
        "e.Having various sources of strong active and passive income": 5
    },
    "2. How are you budgeting your monthly expenses according to your income?": {
        "a.The amount of monthly expenses exceeds income": 1,
        "b.Budget monthly expenses according to income": 2,
        "c.Have a monthly surplus after expenses": 3,
        "d.Monthly expenses are much lower compared to income": 4,
        "e.One or two sources of income can cover monthly expenses": 5
    },
    "3. How much do you currently have in savings?": {
        "a.Not able to save": 1,
        "b.Able to save but do not have savings": 2,
        "c.Have savings equivalent to 1-6 months of income": 3,
        "d.Have savings equal to 6-12 months of income": 4,
        "e.Have a savings amount that exceeds the amount of 12 months of income": 5
    },
    "4. Do you own any assets for personal use?": {
        "a.No assets": 1,
        "b.Own assets for personal use": 2,
        "c.Own assets for personal use and some assets for investment purposes": 3,
        "d.Owning assets for own use and family members as well as various assets for investment purposes": 4,
        "e.Owning assets for personal use and family members as well as various assets that provide consistent returns": 5
    },
    "5.Are you able to pay off your debts with your current income?": {
        "a.Earned income is not able to pay debt": 1,
        "b.Earned income is able to pay off debt": 2,
        "c.Earned income is able to pay off debt and have excess funds after paying off debt": 3,
        "d.Earned income able to pay off debt and able to generate additional income": 4,
        "e.Free from debt": 5
    },
    "6.Do you have any insurance protection?": {
        "a.No insurance protection": 1,
        "b.Have minimum insurance protection for yourself or insurance coverage from the employer only": 2,
        "c.Have insurance protection equivalent to approximately the annual income for yourself and family members": 3,
        "d.Have insurance protection equivalent to twice or triple your annual income for yourself and family members": 4,
        "e.Have insurance protection exceeding three times the annual income for yourself and family members": 5
    },  
}

#### Define result categories and their details
result_categories = {
    "Financial Instability": {
        "range": (6, 12),
        "description": "Your financial health seems unstable."
    },
    "Financial Stability": {
        "range": (13, 18),
        "description": "Your financial health seems stable."
    },
    "Financial Security": {
        "range": (19, 24),
        "description": "Your financial health seems secured."
    },
    "Financial Freedom": {
        "range": (25, 30),
        "description": "Your financial health is financial freedom."
    },
    "Financial Wealth": {
        "range": (31, 36),
        "description": "Your financial health is financial wealth."
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
        st.button("Calculate")
        if st.button:
            result_category = calculate_result_category(total_points)
            display_result(result_category)

def calculate_result_category(total_points):
    for category, details in result_categories.items():
        if details["range"][0] <= total_points <= details["range"][1]:
            return category

def display_result(result_category):
    st.subheader("Result:")
    if result_category:
        st.write(f"Based on your responses, you are in the '{result_category}' category.")
        st.write(result_categories[result_category]["description"])

if __name__ == "__main__":
    main()
