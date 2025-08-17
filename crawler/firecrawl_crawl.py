import os
import requests
import json
from typing import List

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

FIRECRAWL_BASE = "https://api.firecrawl.ai/v1"

def crawl_site(start_url:str , max_pages: int = 200) -> List[dict]:
    """
    Call Firecrawl to crawl start_url and return list of docs with fields:
    [{'id':..., 'url':..., 'title':..., 'text':...}, ...]
    """

    headers = {"Authorization" : f"Bearer {FIRECRAWL_API_KEY}"}
    payload = {
        "start_url" : start_url,
        "max_pages" : max_pages,
        "render_js" : True
    }

    resp = requests.post(f"{FIRECRAWL_BASE}/crawl", json = payload , headers = headers , timeout = 120)
    resp.raise_for_status()
    job = resp.json()

    return job.get("documents" , [])

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("start_url")
    p.add_argument("--max", type=int, default= 200)
    args = p.parse_args()
    docs = crawl_site(args.start_url , max_pages = args.max)
    print(f"Crawled {len(docs)} docs")
    print(json.dumps(docs[:2], indent=2))
    