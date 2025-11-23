import json
import os
import time

class CacheManager:
    def __init__(self, path="embedding_cache.json"):
        self.path = path
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump({}, f)

        with open(path, "r") as f:
            self.cache = json.load(f)

    def retrieve(self, doc_id):
        return self.cache.get(doc_id, None)

    def store(self, doc_id, embedding, hash_value):
        self.cache[doc_id] = {
            "doc_id": doc_id,
            "embedding": embedding.tolist(),
            "hash": hash_value,
            "updated_at": time.time()
        }
        with open(self.path, "w") as f:
            json.dump(self.cache, f, indent=4)
