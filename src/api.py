from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from src.embedder import Embedder
from src.search_engine import SearchEngine
from src.cache_manager import CacheManager
import glob, os
from src.utils import clean_text, compute_hash

app = FastAPI()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

# Load models
embedder = Embedder()
cache = CacheManager()

# Load documents
docs = sorted(glob.glob("/content/data/docs/*.txt"))
embeddings = []
texts = []
doc_ids = []

for path in docs:
    doc_id = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        text = clean_text(f.read())
        hash_val = compute_hash(text)

    cached = cache.retrieve(doc_id)

    if cached and cached["hash"] == hash_val:
        vec = cached["embedding"]
    else:
        vec = embedder.embed(text)
        cache.store(doc_id, vec, hash_val)

    embeddings.append(vec)
    texts.append(text)
    doc_ids.append(doc_id)

engine = SearchEngine(embeddings, doc_ids, texts)

@app.post("/search")
def search(req: SearchRequest):
    query_vec = embedder.embed(req.query)
    results = engine.search(query_vec, req.top_k)
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app)
