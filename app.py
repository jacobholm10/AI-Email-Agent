from crewai import Agent, Task, Crew, Process
import streamlit as st
import os


os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-8b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'



st.title("AI Email Assistant")

email = st.text_input("Enter an email:")



classifier = Agent(
    role = "email classifier",
    goal = "accuractely classify emails based on their importance. give every email one of these ratings: important, casual, or spam",
    backstory = """You are an AI assistant whose only job is to classify emails
    accurately and honestly. Do not be afraid to give emails bad rating
    if they are not important. Your job is to help the user manage their
    inbox.""",
    verbose = True,
    allow_delegation = False,
)


responder = Agent(
    role = "email responder",
    goal = """Based on the importance of the email, write a concise
    and simple response. If the email is rated 'important' write a formal
    response, if the email is rated 'casual' write a casual response,
    and if the email is rated 'spam' ignore the email. no matter what, be
    very concise.""",
    backstory = """You are an AI assistant whose only job is to write a short
    responses to emails based on their importance. The importance will
    be provided to you by the 'classifier' agent""",
    verbose = True,
    allow_delegation = False,
)


classify_email = Task(
    description = f"Classify the following email: '{email}'",
    agent = classifier,
    expected_output = "One of these three options: 'important', 'casual', or 'spam'"
)


respond_to_email = Task(
    description = f"Respond to the email: '{email}' based on the importance provided by the 'classifier agent.",
    agent = responder,
    expected_output = """a very nice consise response to the email based on
    the importance provided by the 'classifier' agent"""
)


crew = Crew(
    agents = {classifier, responder},
    tasks = {classify_email, respond_to_email},
    verbose = 2,
    process = Process.sequential
)




if st.button("Enter"):
    output = crew.kickoff()
    st.write("AI Response: ")
    st.write(output)



