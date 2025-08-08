import streamlit as st
import json

st.set_page_config(page_title="IJIA - Impact Jersey Innovation Assistant", layout="centered")

st.title("💡 Impact Jersey Innovation Assistant (IJIA)")
st.markdown("""
Welcome! I'm **IJIA**, your assistant for the **Impact Jersey Innovation Programme**.

I'll guide you through the eligibility check and application form. This will take around **15–20 minutes**.

---""")
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Step 1: Eligibility - Sequential Enforcement
def eligibility_check():
    st.header("Step 1: Eligibility Check (Mandatory)")

    if st.session_state.step == 1:
        q1 = st.radio(
            "1. Are you a legal resident of Jersey or a business registered in Jersey?",
            ["", "Yes", "No"],
            index=0,
            key="jersey_connection"
        )
        if q1 == "No":
            st.error("❌ Unfortunately, only Jersey-based individuals or entities are eligible.")
            st.stop()
        elif q1 == "Yes":
            st.session_state.step = 2
            st.experimental_rerun()

    if st.session_state.step == 2:
        q2 = st.radio(
            "2. Is your project beyond just an idea? (e.g. prototype, MVP, business plan, user research, or IP?)",
            ["", "Yes", "No"],
            index=0,
            key="project_stage"
        )
        if q2 == "No":
            st.error("❌ Projects must be past idea stage. Explore support from Jersey Business or Digital Jersey.")
            st.stop()
        elif q2 == "Yes":
            st.session_state.step = 3
            st.experimental_rerun()

    if st.session_state.step == 3:
        q3 = st.radio(
            "3. Is your project **not** focused on property speculation, gambling, tobacco, alcohol, or environmentally harmful activities?",
            ["", "Yes", "No"],
            index=0,
            key="sector_check"
        )
        if q3 == "No":
            st.error("❌ Projects in excluded sectors are not eligible.")
            st.stop()
        elif q3 == "Yes":
            st.session_state.step = 4
            st.experimental_rerun()

# Step 2: Application Form
def application_form():
    st.header("Step 2: Application Form")

    def text_input(label, key):
        return st.text_area(label, key=key)

    st.session_state.answers['project_title'] = text_input("Project Title", "project_title")
    st.session_state.answers['summary'] = text_input("One-Sentence Summary", "summary")

    st.session_state.answers['problem'] = text_input("What problem are you solving (specific to Jersey)?", "problem")
    if len(st.session_state.answers['problem']) < 30:
        st.warning("Try to describe the local Jersey context in more detail.")

    st.session_state.answers['solution'] = text_input("What is your innovative solution?", "solution")
    if len(st.session_state.answers['solution']) < 30:
        st.warning("Please expand on what makes your approach innovative or new for Jersey.")

    st.session_state.answers['audience'] = text_input("Who will benefit in Jersey?", "audience")
    st.session_state.answers['impact'] = text_input("How will you measure impact?", "impact")
    if "jobs" not in st.session_state.answers['impact'].lower() and "metrics" not in st.session_state.answers['impact'].lower():
        st.info("Consider including specific metrics like jobs created, revenue, or carbon savings.")

    st.session_state.answers['team'] = text_input("Who is on your team and what are their key skills?", "team")
    st.session_state.answers['funding'] = text_input("How much funding are you requesting?", "funding")

    if st.button("Submit Application"):
        st.session_state.step = 5

# Step 3: Summary and Output
def summary_output():
    st.header("✅ Application Submitted")

    output = {
        "status": "SUBMITTED",
        "project_title": st.session_state.answers.get("project_title", ""),
        "summary": st.session_state.answers.get("summary", ""),
        "problem": st.session_state.answers.get("problem", ""),
        "solution": st.session_state.answers.get("solution", ""),
        "audience": st.session_state.answers.get("audience", ""),
        "impact": st.session_state.answers.get("impact", ""),
        "team": st.session_state.answers.get("team", ""),
        "funding": st.session_state.answers.get("funding", "")
    }

    st.json(output)
    st.success("Your application has been submitted. A confirmation email will follow shortly. You’ll hear from us within 10 working days.")

# Render Logic
if st.session_state.step < 4:
    eligibility_check()
elif st.session_state.step == 4:
    application_form()
elif st.session_state.step == 5:
    summary_output()
