import arxiv
from typing import Dict,List
from autogen_core.tools import FunctionTool

def arvix_search(query:str,max_results:int =5):
    """
    Search arXiv for research papers matching a query and return structured metadata.

    This function queries the arXiv API for papers relevant to the provided search
    string, sorted by relevance, and returns a list of dictionaries containing
    key information about each paper. It is designed to be used as a tool inside
    an AI agent or retrieval workflow.

    Args:
        query (str):
            The search query used to find relevant arXiv papers. This can include
            keywords, phrases, author names, or subject areas.
        max_results (int, optional):
            The maximum number of papers to return. Defaults to 5.

    Returns:
        List[Dict]:
            A list of dictionaries where each dictionary contains:
                - "title" (str): Title of the paper.
                - "authors" (List[str]): Names of the authors.
                - "published" (str): Publication date in YYYY-MM-DD format.
                - "summary" (str): Abstract/summary of the paper.
                - "pdf_url" (str): Direct link to the PDF version of the paper.

    Notes:
        - Results are sorted by relevance using arXiv's ranking.
        - Requires the `arxiv` Python package and internet access.
        - Returned data is lightweight and suitable for LLM tool usage,
          summarization, or retrieval-augmented generation (RAG).

    Example:
        >>> arvix_search("diffusion models in computer vision", max_results=3)
        [
            {
                "title": "...",
                "authors": ["Author A", "Author B"],
                "published": "2024-01-15",
                "summary": "...",
                "pdf_url": "https://arxiv.org/pdf/....pdf"
            }
        ]
    """
    client = arxiv.Client()
    search = arxiv.Search(
                query = query,
                max_results = max_results,
                sort_by = arxiv. SortCriterion.Relevance
                    )
    
    papers: List[Dict] = []
    for result in client.results(search):
        papers.append(
            {
                "title": result.title,
                "authors": [a.name for a in result.authors],
                "published": result.published.strftime("%Y-%m-%d"),
                "summary": result.summary,
                "pdf_url": result.pdf_url,
            }
        )
    return papers

def arvix_tool():

    return FunctionTool(
                arvix_search,
                description=(
                    "Searches arXiv and returns up to *max_results* papers, each containing "
                    "title, authors, publication date, abstract, and pdf_url."
                ),
                )