import streamlit as st

st.set_page_config(page_title="BBSP Eligibility Checker", layout="centered")
st.title("Better Business Support Package – Eligibility Checker")

# ✅ Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'values' not in st.session_state:
    st.session_state['values'] = {}

def step_1():
    ans = st.radio("1. Is your business registered and controlled in Jersey?", ["Yes", "No"], key="q1")
    if ans == "No":
        st.error("You must be Jersey-registered to qualify.")
        st.stop()
    elif ans == "Yes":
        st.session_state['values']['registered'] = True
        st.session_state.step = 2
        st.experimental_rerun()

def step_2():
    ans = st.radio("2. Do you employ at least one person (owner + 1) paid £128+ per week for 3+ months?", ["Yes", "No"], key="q2")
    if ans == "No":
        st.error("Your business must meet the employment condition to qualify.")
        st.stop()
    if ans == "Yes":
        st.session_state.values['employment'] = True
        st.session_state.step = 3
        st.experimental_rerun()

def step_3():
    ans = st.radio("3. Are your tax/social obligations up to date or on an adhered payment plan for 3+ months?", ["Yes", "No"], key="q3")
    if ans == "No":
        st.error("Tax/Social obligations must be current or on an agreed plan.")
        st.stop()
    if ans == "Yes":
        st.session_state.values['tax_ok'] = True
        st.session_state.step = 4
        st.experimental_rerun()

def step_4():
    ans = st.selectbox("4. How long has your business been operating?", ["Select one", "Under 6 months", "6 to 18 months", "More than 18 months"], key="q4")
    if ans != "Select one":
        st.session_state.values['operation_length'] = ans
        st.session_state.step = 5
        st.experimental_rerun()

def step_5():
    ans = st.radio("5. Does your business operate in the Visitor Economy?", ["Yes", "No"], key="q5")
    if ans:
        st.session_state.values['visitor_economy'] = (ans == "Yes")
        st.session_state.step = 6
        st.experimental_rerun()

def show_result():
    vals = st.session_state.values
    if vals['operation_length'] == "More than 18 months":
        max_amount = 75000
    else:
        max_amount = 5000

    st.success("Congratulations! You appear to be eligible.")
    msg = f"Eligible for up to £{max_amount:,} Productivity grant"
    if vals['visitor_economy']:
        msg += f", plus up to £{max_amount:,} Visitor Economy grant"
    st.write(msg)

# Render steps
if st.session_state.step == 1:
    step_1()
elif st.session_state.step == 2:
    step_2()
elif st.session_state.step == 3:
    step_3()
elif st.session_state.step == 4:
    step_4()
elif st.session_state.step == 5:
    step_5()
elif st.session_state.step == 6:
    show_result()
