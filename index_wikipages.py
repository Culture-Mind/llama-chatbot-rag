from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.program.openai import OpenAIPydanticProgram
import openai
from utils import get_apikey
from pydantic import BaseModel

# define the data model in pydantic
class WikiPageList(BaseModel):
    "Data model for WikiPageList"
    pages: list 


def wikipage_list(query):
    openai.api_key = get_apikey() 

    prompt_template_str = """
    Given the input {query}, 
    extract the Wikipedia pages mentioned after 
    "please index:" and return them as a list.
    If only one page is mentioned, return a single
    element list.
    """

    program = OpenAIPydanticProgram.from_defaults(
        output_cls=WikiPageList,
        prompt_template_str=prompt_template_str,
        verbose=True
    )

    wikipage_requests = program(query=query)

    return wikipage_requests


def create_wikidocs(wikipage_requests):
    
    reader = WikipediaReader()
    documents = reader.load_data(pages=wikipage_requests)
    return documents


def create_index(query):
    global index
    
    wikipage_requests = wikipage_list(query)
    docs = create_wikidocs(wikipage_requests)

    splitter = SentenceSplitter(chunk_size=150, chunk_overlap=45)
    nodes = splitter.get_nodes_from_documents(docs)

    index = VectorStoreIndex(nodes)
    return index


if __name__ == "__main__":
    query = "/get wikipages: paris, lagos, lao"
    index = create_index(query)
    print("INDEX CREATED", index)
