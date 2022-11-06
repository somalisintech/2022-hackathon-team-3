from backend import api
from backend import schemas
from backend.db import Ticker, Document, HaramPassage


@api.post("/analyze")
async def filter_listings(body: schemas.AnalyzeBody):
    ticker = list(Ticker.select().where(Ticker.symbol == body.ticker))
    if not ticker:
        # TODO: Add status code.
        return {
            "halal": True
        }

    passages = sorted(list(ticker[0].cik.document.haram_passage),
                      key=lambda x:x.score, reverse=True)
    if passages:
        result = {
            "halal": False,
            "ref_text": passages[0].text,
            "ref_link": ticker[0].cik.document.link
        }
        return result

    return {
        "halal": True
    }
