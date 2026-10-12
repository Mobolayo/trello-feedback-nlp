"""Demo: semantic embeddings vs TF-IDF on two differently-worded reviews."""
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

A = "The app crashes on launch"
B = "Trello shuts down when I open it"   # same problem, different words
C = "I love how easy it is to use"       # unrelated praise
reviews = [A, B, C]

print("Reviews:")
print("  A:", A)
print("  B:", B, "  <- same problem as A, different words")
print("  C:", C, "  <- unrelated praise\n")

# SEMANTIC (transformer embeddings)
model = SentenceTransformer("all-MiniLM-L6-v2")
emb = model.encode(reviews)
print("Each review becomes a vector of length:", emb.shape[1], "\n")
print("SEMANTIC similarity (embeddings), 1.0 = identical meaning:")
print(f"  A vs B: {util.cos_sim(emb[0], emb[1]).item():.2f}   (should be HIGH)")
print(f"  A vs C: {util.cos_sim(emb[0], emb[2]).item():.2f}   (should be low)\n")

# TRADITIONAL (TF-IDF word vectors)
sim = cosine_similarity(TfidfVectorizer().fit_transform(reviews))
print("WORD-BASED similarity (TF-IDF), 1.0 = identical words:")
print(f"  A vs B: {sim[0,1]:.2f}   (LOW - they share no words)")
print(f"  A vs C: {sim[0,2]:.2f}")