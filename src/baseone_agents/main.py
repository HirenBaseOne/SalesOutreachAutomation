#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from baseone_agents.crews.poem_crew.poem_crew import PoemCrew


class LeadInfo(BaseModel):
    first_name: str = Field(description="first name of the sales lead")
    last_name: str = Field(description="last name of the sales lead")
    email: str = Field(description="email of the sales lead")
    company: str = Field(description="current company sales lead works for")
    country: str = Field(description="country the sales lead is currently located")
    company: str = Field(description="current company sales lead works for")
    linkedin_web: str = Field(description="sales lead LinkedIn website")

class WorkExperience(BaseModel):
    job_title: str = Field(description="Job title of the sales lead at this company")
    company_name: str = Field(description="Name of the company where the sales lead worked")
    start_date: Optional[date] = Field(None, description="Start date of employment (YYYY-MM-DD)")
    end_date: Optional[date] = Field(None, description="End date of employment (YYYY-MM-DD), if applicable")
    industry: Optional[str] = Field(None, description="Industry of the company")
    responsibilities: Optional[str] = Field(None, description="Brief description of job responsibilities and key contributions")
    achievements: Optional[str] = Field(None, description="Notable achievements or impact in this role")
    location: Optional[str] = Field(None, description="Location of the job (City, Country)")
    employment_type: Optional[str] = Field(None, description="Type of employment (Full-time, Part-time, Contract, Internship, Freelance)")

class EmailTemplate(BaseModel):
    recipient: EmailStr = Field(description="Email address of the recipient")
    sender: EmailStr = Field(description="Email address of the sender")
    subject: str = Field(description="Subject line of the email")
    body: str = Field(description="Main content of the email in plain text or HTML format")
    cc: Optional[List[EmailStr]] = Field(None, description="List of email addresses to CC")
    bcc: Optional[List[EmailStr]] = Field(None, description="List of email addresses to BCC")
    attachments: Optional[List[str]] = Field(None, description="List of file paths or URLs for attachments")
    reply_to: Optional[EmailStr] = Field(None, description="Email address for reply-to field")
    content_type: str = Field(default="text/plain", description="Content type of the email (text/plain or text/html)")

class Persona(BaseModel):
    name: str = Field(description="Full name of the persona")
    role: str = Field(description="Job title or role of the persona")
    company: Optional[str] = Field(None, description="Company where the persona works")
    industry: Optional[str] = Field(None, description="Industry the persona operates in")
    pain_points: List[str] = Field(description="Key challenges the persona faces")
    goals: List[str] = Field(description="Primary goals or objectives the persona is trying to achieve")
    preferred_communication: Optional[str] = Field(None, description="Preferred method of communication (Email, LinkedIn, Phone, etc.)")
    decision_making_process: Optional[str] = Field(None, description="How the persona evaluates and makes decisions")

class Tone(BaseModel):
    style: str = Field(description="Overall style of communication (e.g., Professional, Friendly, Persuasive, etc.)")
    approach: str = Field(description="The communication approach (e.g., Consultative, Direct, Empathetic, etc.)")
    voice: str = Field(description="The personality of the communication (e.g., Confident, Knowledgeable, Engaging, etc.)")



class SalesFlow(Flow[LeadInfo]):

    @start()
    def fun1():
        pass


    @listen()
    def func2():
        pass

    @listen()
    def func3():
        pass



def kickoff():
    sales_flow = SalesFlow()
    sales_flow.kickoff()


def plot():
    sales_flow = SalesFlow()
    SalesFlow.plot()


input = {
    "lead_name": ,
    "company": ,
    "": ,
}

if __name__ == "__main__":
    kickoff()
