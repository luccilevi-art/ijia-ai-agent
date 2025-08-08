import streamlit as st

st.set_page_config(page_title="Eligibility Checker", layout="centered")
st.title("Eligibility Checker")

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
    ans = st.radio("2. Does the Proposal clearly aligned with one or more of the Jersey Strategic Priorities?", ["Yes", "No"], key="q2")
    if ans == "No":
        st.error("Your business must align with condition to qualify.")
        st.stop()
    if ans == "Yes":
        st.session_state['values']['employment'] = True
        st.session_state.step = 3
        return

def step_3():
    ans = st.radio("3. Do you ??", ["Yes", "No"], key="q3")
    if ans == "No":
        st.error("Tax/Social obligations must be current or on an agreed plan.")
        st.stop()
    if ans == "Yes":
        st.session_state['values']['tax_ok'] = True
        st.session_state.step = 4
        return

def step_4():
    ans = st.selectbox("4. Was the Proposal clearly aligned with one or more of the Jersey Strategic Priorities?", ["Select one", "Environment", "Existing Jersey", "Health"], key="q4")
    if ans != "Select one":
        st.session_state['values']['operation_length'] = ans
        st.session_state.step = 5
        return

def show_result():
    vals = st.session_state['values']
    if vals['operation_length'] == "More than 18 months":
        max_amount = Tier 1
    else:
        max_amount = Tier 2

    st.success("🎉 Congratulations! You appear to be eligible.")
    msg = f"Eligible for up to **£{max_amount:,}** Productivity grant"
    if vals['visitor_economy']:
        msg += f", plus up to **£{max_amount:,}** Visitor Economy grant"
    st.markdown(msg)

# Step controller
step = st.session_state.step

if step == 1:
    step_1()
elif step == 2:
    step_2()
elif step == 3:
    step_3()
elif step == 4:
    step_4()
elif step == 5:
    step_5()
elif step == 6:
    show_result()
