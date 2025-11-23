import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
    def __init__(self, embeddings, doc_ids, texts):
        self.embeddings = np.array(embeddings)
        self.doc_ids = doc_ids
        self.texts = texts

    def search(self, query_vec, top_k=5):
        sims = cosine_similarity([query_vec], self.embeddings)[0]
        top_idx = sims.argsort()[::-1][:top_k]

        results = []
        for i in top_idx:
            text = self.texts[i]
            preview = " ".join(text.split()[:30]) + "..."
            score = float(sims[i])

            # explanation: keyword overlap
            query_words = set(query.lower().split())
            doc_words = set(text.lower().split())
            overlap = query_words.intersection(doc_words)

            results.append({
                "doc_id": self.doc_ids[i],
                "score": score,
                "preview": preview,
                "overlap_keywords": list(overlap),
                "overlap_ratio": len(overlap) / (len(query_words) + 1)
            })

        return results
