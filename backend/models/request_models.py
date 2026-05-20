from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

# frontend will send req and fastapi validates it 