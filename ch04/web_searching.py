from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List


def web_search(
    web_query: str,
    num_results: int,
) -> List[str]:
    try:
        return [
            r["link"]
            for r in DuckDuckGoSearchAPIWrapper().results(web_query, num_results)
        ]
    except Exception as exc:
        print(f"DuckDuckGo search failed for query '{web_query}': {exc}")
        return []