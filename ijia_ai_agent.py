
import uuid
from datetime import datetime
import streamlit as st

class IJIAAgent:
    def __init__(self):
        self.application = {
            "application_id": str(uuid.uuid4()),
            "submission_timestamp": datetime.utcnow().isoformat() + "Z",
            "status": None,
            "rejection_stage": None,
            "rejection_reason": None,
            "eligibility_checks": {
                "jersey_connection": None,
                "project_stage": None,
                "excluded_sectors": None
            },
            "application_data": {},
            "applicant_details": {},
            "conversation_log_summary": ""
        }

    def reject(self, stage, reason):
        self.application["status"] = "REJECTED"
        self.application["rejection_stage"] = stage
        self.application["rejection_reason"] = reason
        return self.application

    def submit(self):
        self.application["status"] = "SUBMITTED"
        return self.application

    def check_eligibility(self, jersey_connection, project_stage, excluded_sectors):
        self.application["eligibility_checks"]["jersey_connection"] = jersey_connection
        self.application["eligibility_checks"]["project_stage"] = project_stage
        self.application["eligibility_checks"]["excluded_sectors"] = excluded_sectors

        if not jersey_connection:
            return self.reject("jersey_connection", "Applicant is not a Jersey-registered entity or legal resident.")
        if not project_stage:
            return self.reject("project_stage", "Project is still at idea stage without validation.")
        if not excluded_sectors:
            return self.reject("excluded_sectors", "Project falls within excluded sectors.")
        return None

    def collect_application_data(self, title, summary, problem, solution, audience, impact, team, funding):
        self.application["application_data"] = {
            "project_title": title,
            "project_summary": summary,
            "problem_statement": problem,
            "solution_description": solution,
            "jersey_impact": {
                "description": impact.get("description"),
                "metrics": impact.get("metrics")
            },
            "team_details": team,
            "funding_request": {
                "amount": funding.get("amount"),
                "currency": funding.get("currency", "GBP")
            }
        }

    def provide_feedback(self, field, content):
        if field == "impact" and "help the economy" in content.lower():
            return "That's a good start. Could you estimate jobs created, sectors boosted, or potential revenue?"
        if field == "innovation" and "common" in content.lower():
            return "What makes your approach uniquely different or more effective for Jersey?"
        return "Thanks! That looks strong."

    def collect_applicant_details(self, name, email):
        self.application["applicant_details"] = {
            "name": name,
            "email": email
        }

    def set_conversation_summary(self, summary):
        self.application["conversation_log_summary"] = summary

# Streamlit UI
agent = IJIAAgent()
st.title("Impact Jersey Innovation Assistant (IJIA)")
st.write("I'm here to help you start your application and check if it's the right fit for you. The process should take about 15–20 minutes.")

with st.form("eligibility_form"):
    st.subheader("Step 1: Eligibility Check")
    jc = st.radio("Are you a Jersey-registered business or legal resident?", ["Yes", "No"])
    ps = st.radio("Is your project beyond the idea stage?", ["Yes", "No"])
    es = st.radio("Is your project outside of excluded sectors (e.g., property speculation, gambling, etc.)?", ["Yes", "No"])
    submitted = st.form_submit_button("Check Eligibility")

    if submitted:
        result = agent.check_eligibility(jc == "Yes", ps == "Yes", es == "Yes")
        if result:
            st.error("Sorry, you are not eligible.")
            st.json(result)
            st.stop()
        else:
            st.success("You're eligible! Continue below.")

            with st.form("application_form"):
                st.subheader("Step 2: Application Form")
                title = st.text_input("Project Title")
                summary = st.text_input("One-Sentence Summary")
                problem = st.text_area("The Problem You're Solving (for Jersey)")
                solution = st.text_area("Your Innovative Solution")
                audience = st.text_area("Your Target Audience / Beneficiaries in Jersey")
                impact_description = st.text_area("Measurable Impact - Description")
                impact_metrics = st.text_area("Measurable Impact - Metrics")
                team = st.text_area("Team Members and Key Skills")
                amount = st.number_input("Amount of Funding Requested (GBP)", min_value=0)
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                final_submit = st.form_submit_button("Submit Application")

                if final_submit:
                    agent.collect_application_data(
                        title, summary, problem, solution, audience,
                        {"description": impact_description, "metrics": impact_metrics},
                        team, {"amount": amount}
                    )
                    agent.collect_applicant_details(name, email)
                    agent.set_conversation_summary("Application submitted successfully via Streamlit interface.")
                    submitted_app = agent.submit()

                    st.success("Application Submitted!")
                    st.json(submitted_app)
