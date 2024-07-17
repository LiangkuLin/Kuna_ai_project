from typing import Any, Dict, List
from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma 
from langchain.schema import BaseRetriever
from langchain_core.documents import Document

class RedundantFilterRetriever(BaseRetriever): 
    embeddings: Embeddings 
    chroma: Chroma 
    
    def get_relevant_documents(self, query):
        # calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)
        # take embeddings and feed them into that 
        # max_marginal_relevance_search_by_vector 
       
        return self.chroma.max_marginal_relevance_search(
            embeddings = emb , 
            # the tolerance of similar documents 
            lambda_mult= 0.8,
        )
    
    async def aget_relevant_documents(self):
        return []