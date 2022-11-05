from pydantic import BaseModel


class AnalyzeBody(BaseModel):
    ticker: str = ''
