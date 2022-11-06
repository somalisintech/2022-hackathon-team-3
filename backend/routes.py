from backend import api
from backend import schemas
from backend.db import Ticker, Document


@api.post("/analyze")
async def filter_listings(body: schemas.AnalyzeBody):
    ticker = list(Ticker.select().where(Ticker.symbol == body.ticker))
    if not ticker:
        # TODO: Add status code.
        return {
            "error": "Ticker not found"
        }

    cik = ticker.cik
    document = list(Document.select().where(Document.id == cik.document))



    result = {
        "halal": False,
        "ref_text": """Our commitment to producing the highest quality beers is a key part of our heritage and remains so to this day. 
        Our brands are designed to appeal to a wide range of consumer tastes, styles and price preferences. 
        Coors was incorporated in June 1913 under the laws of the state of Colorado.""",
        "ref_link": "https://www.sec.gov/Archives/edgar/data/1652044/000165204422000019/goog-20211231.htm"
    }
    return result
