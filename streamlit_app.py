import streamlit as st

### Define questions and point system
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

#### define result categories
result_categories = {
    "Financial Instability": (6, 12),
    "Financial Stability": (13, 18),
    "Financial Security": (19, 24),
    "Financial Freedom": (25, 30),
    "Financial Wealth": (31, 36)
}

#### create streamlit app
def main():
    st.title("Financial Health Calculator")

    total_points = 0

    for question, options in questions.items():
        st.write(question)
        selected_option = st.radio("Select an option:", list(options.keys()))
        total_points += options[selected_option]

    st.write(f"Total Points: {total_points}")

    result_category = None
    for category, (min_points, max_points) in result_categories.items():
        if min_points <= total_points <= max_points:
            result_category = category
            break

    if result_category:
        st.write(f"Financial Health Category: {result_category}")
    else:
        st.write("Unable to determine financial health category")

if __name__ == "__main__":
    main()