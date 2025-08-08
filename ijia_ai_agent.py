import streamlit as st

st.set_page_config(page_title="Impact Jersey - Eligibility Checker", layout="centered")

st.title("Impact Jersey Innovation Programme")
st.subheader("Eligibility Checker")

if "step" not in st.session_state:
    st.session_state.step = 0

# Define the questions and their rejection reasons
questions = [
    {
        "text": "Are you a legal resident of Jersey, or is your business legally registered in Jersey?",
        "rejection": "The Impact Jersey programme requires applicants to be based in Jersey to ensure the primary impact benefits the island."
    },
    {
        "text": "Is your project beyond the idea stage (e.g. MVP, business plan, research, or IP)?",
        "rejection": "We need projects that have moved beyond the initial concept stage. Consider developing your idea further before applying."
    },
    {
        "text": "Is your project NOT focused on property development, gambling, tobacco, alcohol, or activities with negative environmental impact?",
        "rejection": "Unfortunately, this programme excludes projects in those sectors."
    },
    {
        "text": "Will the primary impact of your project benefit Jersey?",
        "rejection": "The programme requires the primary impact to be in Jersey."
    },
]

# Go through each question step by step
for i in range(st.session_state.step + 1):
    q = questions[i]
    answer = st.radio(q["text"], ["Yes", "No"], key=f"q{i}", index=None)

    if answer == "No":
        st.error(q["rejection"])
        st.stop()

    if answer == "Yes" and i == st.session_state.step and st.session_state.step < len(questions) - 1:
        if st.button("Next", key=f"next{i}"):
            st.session_state.step += 1
            st.experimental_rerun()

# If they passed all checks
if st.session_state.step == len(questions) - 1 and st.session_state.get(f"q{len(questions)-1}") == "Yes":
    st.success("✅ You meet the core eligibility criteria for the Impact Jersey Innovation Programme!")
    st.markdown("You may now proceed to complete the full application.")
