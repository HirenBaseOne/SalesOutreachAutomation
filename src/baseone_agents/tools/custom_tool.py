from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
import requests
import os

class GHLMessageInput(BaseModel):
    type: str = Field(..., description="Type of message being sent. Allowed values: SMS, Email, WhatsApp, GMB, IG, FB, Custom, Live_Chat")
    contactId: str = Field(..., description="ID of the contact receiving the message.")
    emailFrom: str = Field(..., description="Email address to send from.")
    emailTo: str = Field(..., description="Recipient email address.")
    subject: str = Field(..., description="Subject line for email messages.")
    message: str = Field(..., description="Plain text content of the message.")
    html: str = Field(..., description="HTML content of the message.")
    emailCc: List[str] = Field(default=[], description="List of CC email addresses.")
    emailBcc: List[str] = Field(default=[], description="List of BCC email addresses.")
    attachments: List[str] = Field(default=[], description="Array of attachment URLs.")
    replyMessageId: str = Field(default=None, description="ID of the message being replied to.")
    templateId: str = Field(default=None, description="ID of the message template.")
    threadId: str = Field(default=None, description="ID of the message thread (for email threading).")
    scheduledTimestamp: int = Field(default=None, description="UTC Timestamp (in seconds) at which the message should be scheduled.")
    conversationProviderId: str = Field(default=None, description="ID of the conversation provider.")
    emailReplyMode: str = Field(default="reply", description="Mode for email replies. Allowed values: reply, reply_all")

class GHLMessageTool(BaseTool):
    name: str = "GHL Message Sending Tool"
    description: str = "This tool sends messages via the GoHighLevel API, including emails, SMS, and WhatsApp messages."
    args_schema: Type[BaseModel] = GHLMessageInput

    def _run(self, **kwargs):
        api_url = "https://services.leadconnectorhq.com/conversations/messages"
        headers = {
            "Authorization": f"Bearer {os.getenv('GHL_ACCESS_TOKEN')}",
            "Version": "2021-04-15",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(api_url, json=kwargs, headers=headers)
            response_data = response.json()

            if response.status_code == 200:
                return {
                    "status": "Success",
                    "conversationId": response_data.get("conversationId"),
                    "emailMessageId": response_data.get("emailMessageId"),
                    "messageId": response_data.get("messageId"),
                    "message": response_data.get("msg", "Message sent successfully.")
                }
            else:
                return {
                    "status": "Error",
                    "error_code": response.status_code,
                    "message": response_data
                }
        except Exception as e:
            return {"status": "Error", "message": str(e)}
