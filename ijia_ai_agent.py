import streamlit as st

st.set_page_config(page_title="Impact Jersey - Eligibility Checker", layout="centered")

st.title("Impact Jersey Innovation Programme")
st.subheader("Eligibility Checker")

# --- Setup session state ---
if "step" not in st.session_state:
    st.session_state.step = 0

# --- Eligibility Questions & Rejections ---
questions = [
    {
        "text": "Are you a legal resident of Jersey, or is your business legally registered in Jersey?",
        "key": "q1",
        "rejection": "❌ The Impact Jersey programme requires applicants to be based in Jersey to ensure the primary impact benefits the island."
    },
    {
        "text": "Is your project beyond the idea stage (e.g. MVP, business plan, research, or IP)?",
        "key": "q2",
        "rejection": "❌ We need projects that have moved beyond the initial concept stage. Consider developing your idea further before applying."
    },
    {
        "text": "Is your project NOT focused on property development, gambling, tobacco, alcohol, or activities with negative environmental impact?",
        "key": "q3",
        "rejection": "❌ Unfortunately, this programme excludes projects in those sectors."
    },
    {
        "text": "Will the primary impact of your project benefit Jersey?",
        "key": "q4",
        "rejection": "❌ The programme requires the primary impact to be in Jersey."
    },
]

# --- Display Current Step ---
current = st.session_state.step
q = questions[current]
response = st.radio(q["text"], ["Yes", "No"], key=q["key"])

if response == "No":
    st.error(q["rejection"])
    st.stop()

# --- Advance to Next Step ---
if response == "Yes":
    if current < len(questions) - 1:
        if st.button("Next"):
            st.session_state.step += 1
            st.experimental_rerun()
    else:
        st.success("✅ You meet the core eligibility criteria for the Impact Jersey Innovation Programme!")
        st.markdown("You may now proceed to complete the full application.")
