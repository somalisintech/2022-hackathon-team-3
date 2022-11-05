from backend import api
from backend import schemas


@api.post("/analyze")
async def filter_listings(body: schemas.AnalyzeBody):
    result = {
        "halal": False,
        "ref_text": """Our commitment to producing the highest quality beers is a key part of our heritage and remains so to this day. 
        Our brands are designed to appeal to a wide range of consumer tastes, styles and price preferences. 
        Coors was incorporated in June 1913 under the laws of the state of Colorado.""",
        "ref_link": "https://www.sec.gov/Archives/edgar/data/1652044/000165204422000019/goog-20211231.htm"
    }
    return result
