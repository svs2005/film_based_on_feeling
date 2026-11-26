import random
import unicodedata

LIMIT = 1000 

# cleaning
def cleaning(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = " ".join(s.split())
    return s
   
print(cleaning("Amélie in Paris"))  #my test

# looking up titles
titles = {}
with open("data/MovieSummaries/movie.metadata.tsv", encoding="utf-8") as f:
    for line in f:

        line = line.rstrip("\n")
        clms = line.split("\t")
        titles[clms[0]] = clms[2]
        

print(len(titles))
print(list(titles.items())[:3])

# making 1 text block / film
films = []
with open("data/MovieSummaries/plot_summaries.txt", encoding="utf-8") as f:
    for line in f:
        wiki_id, plot = line.rstrip("\n").split("\t", 1)
        if wiki_id not in titles:
            continue
        films.append(f"TITLE: {cleaning(titles[wiki_id])}\nPLOT: {cleaning(plot)}\n\n")

print(len(films))
print(films[0])
