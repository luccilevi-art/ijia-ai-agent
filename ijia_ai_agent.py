import streamlit as st

st.set_page_config(page_title="BBSP Eligibility Checker", layout="centered")
st.title("Better Business Support Package – Eligibility Checker")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'values' not in st.session_state:
    st.session_state['values'] = {}

def step_1():
    ans = st.radio("1. Is your business registered and controlled in Jersey?", ["Yes", "No"], key="q1")
    if ans == "No":
        st.error("You must be Jersey-registered to qualify.")
        st.stop()
    if ans == "Yes":
        st.session_state['values']['registered'] = True
        st.session_state.step = 2
        return

def step_2():
    ans = st.radio("2. Do you employ at least one person (owner + 1) paid £128+ per week for 3+ months?", ["Yes", "No"], key="q2")
    if ans == "No":
        st.error("Your business must meet the employment condition to qualify.")
        st.stop()
    if ans == "Yes":
        st.session_state['values']['employment'] = True
        st.session_state.step = 3
        return

def step_3():
    ans = st.radio("3. Are your tax/social obligations up to date or on an adhered payment plan for 3+ months?", ["Yes", "No"], key="q3")
    if ans == "No":
        st.error("Tax/Social obligations must be current or on an agreed plan.")
        st.stop()
    if ans == "Yes":
        st.session_state['values']['tax_ok'] = True
        st.session_state.step = 4
        return

def step_4():
    ans = st.selectbox("4. How long has your business been operating?", ["Select one", "Under 6 months", "6 to 18 months", "More than 18 months"], key="q4")
    if ans != "Select one":
        st.session_state['values']['operation_length'] = ans
        st.session_state.step = 5
        return

def step_5():
    ans = st.radio("5. Does your business operate in the Visitor Economy?", ["Yes", "No"], key="q5")
    if ans:
        st.session_state['values']['
