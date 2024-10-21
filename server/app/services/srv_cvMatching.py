import os
from dotenv import load_dotenv
import numpy as np
from numpy.linalg import norm
from typing import Dict, List
from langchain_openai import OpenAIEmbeddings

load_dotenv()

class CvMatching(object):
    def __init__(self, model: str = "text-embedding-3-large", dimensions: int = 3072):
        self.__embeddings = OpenAIEmbeddings(api_key = os.environ.get("OPENAI_API_KEY"), model = model, dimensions = dimensions)

    def embed_text(self, text):
        return np.array(self.__embeddings.embed_document([text])[0])

    @staticmethod
    def cosine_similarity(a: np.array, b: np.array):
        return np.dot(a, b) / (norm(a) * norm(b))

    def cv_matching(self, candidate: Dict[str, str], job_string: str, categories: List[str]):        
        candidate_for_return = {}
        candidate_string = []
        for category, segment in candidate.items():
            if segment != "":
                candidate_for_return.update({category: segment})
            else:
                segment = "none"
            if category not in categories:
                continue

            candidate_string.append(f"{category}: {segment}")
        
        candidate_string = "; ".join(candidate_string.sort(lambda x: x[0]))
        job_string_embeded = self.embed_text(job_string)
        candidate_string_embeded = self.embed_text(candidate_string)
        candidate_for_return.update({"cv_matching": self.cosine_similarity(job_string_embeded, candidate_string_embeded)})
        return candidate_for_return