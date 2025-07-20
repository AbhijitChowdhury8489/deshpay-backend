
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class RechargeRequest(BaseModel):
    number: str
    amount: float

class BillPaymentRequest(BaseModel):
    bill_type: str
    account: str
    amount: float
