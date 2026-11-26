import random
import unicodedata

LIMIT = 1000 

# cleaning
def cleaning(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = " ".join(s.split())
    return s


# looking up titles
titles = {}
with open("data/MovieSummaries/movie.metadata.tsv", encoding="utf-8") as f:
    for line in f:

        line = line.rstrip("\n")
        clms = line.split("\t")
        titles[clms[0]] = clms[2]
        

# making 1 text block / film
films = []
with open("data/MovieSummaries/plot_summaries.txt", encoding="utf-8") as f:
    for line in f:
        wiki_id, plot = line.rstrip("\n").split("\t", 1)
        if wiki_id not in titles:
            continue
        films.append(f"TITLE: {cleaning(titles[wiki_id])}\nPLOT: {cleaning(plot)}\n\n")


# shuffle it, split it, and limit
random.seed(42)
random.shuffle(films)
if LIMIT is not None:
    films = films[:LIMIT]

n = int(0.9 * len(films))
train_films = films[:n]
val_films = films[n:]



# write to the disk
with open("data/train.txt", "w", encoding="utf-8") as f:
    f.write("".join(train_films))
with open("data/val.txt", "w", encoding="utf-8") as f:
    f.write("".join(val_films))

# for my sanity
text = open("data/train.txt", encoding="utf-8").read()

