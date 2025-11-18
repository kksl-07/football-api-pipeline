from pydantic import BaseModel


class TransfersDetails(BaseModel):
    player: str | None = None
    team: str | None = None


class Transfer(BaseModel):
    endpoint_name: str = "transfers"
    transfer_obj: TransfersDetails
