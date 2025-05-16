import streamlit as st
import requests

# function to get the birthdays
def get_birthdays(month, year):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    birthdays = data["data"]["Births"]
    return birthdays


# function to get the date (i.e, June 1)
def get_date(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    month_day = data["date"]
    return month_day

# set up Streamlit web app
st.set_page_config(
    page_title="Famous Birthdays",
    page_icon="🎂"
)

# set up the page title and the user input
st.title("Famous Birthdays")
st.write("Enter a date to see who was born on that day: ")
month = st.number_input("Enter the month (1-12):", min_value=1, max_value=12, step=1)
day = st.number_input("Enter the day (1-31:", min_value=1, max_value=31, step=1)

# conditional for once the user selects a date
if st.button("Show Birthdays"):
    birthdays = get_birthdays(month, day)
    date = get_date(month, day)

    if birthdays:
        st.subheader(f"Famous Birthdays on {date}:")
        for birthday in birthdays:
            st.write(f"Year: {birthday['year']}")
            st.write(f"Who: {birthday["text"]}")
            st.write(f"Link: {birthday['links'][0]['link']}")
            st.divider()