import hashlib
import json

from backend.db import Ticker, Document, CIK, HaramPassage


def hash_(str_id):
    return int(hashlib.sha256(
        str_id.encode('utf-8')).hexdigest(), 16) % 10**16


def dump_data():
    fpath = "/home/haks/HAKS/Downloads/ticker_to_cik (12).json"
    with open(fpath) as f_:
        data = json.load(f_)

    for ticker, meta in data.items():
        doc_id = str(hash(meta["link"]))
        doc, is_created = Document.get_or_create(
            id=doc_id,
            defaults={
                "business_statement": meta["business_statement"],
                "link": meta["link"],
                "processed": meta.get("processed") or False
            }
        )

        cik, cik_is_created = CIK.get_or_create(
                id=meta["cik"],
                defaults={
                    "document": doc
                }
            )

        ticker = Ticker.create(
            symbol=ticker,
            cik=cik
        )

        if meta.get("processed"):
            for idx, (score, passage) in enumerate(meta.get("top_passages", [])):
                HaramPassage.get_or_create(
                    id=f"{doc_id}-{idx}",
                    defaults={
                        "text": passage,
                        "score": score,
                        "document": doc
                    }
                )
