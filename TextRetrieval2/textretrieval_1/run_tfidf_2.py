import codecs, glob
import rtfidf

text_dirs = ["sample"]  #["articles/*"]
tfidf = rtfidf.tfidf()

query = "Worries about the deficit concerns about China do, however, remain. China's currency remains pegged to the dollar"

def run():
    for i in text_dirs:
        documents = glob.glob(i + "/*.txt")
        for j in documents:
            with codecs.open(j, "r", "utf-8") as raw:
                words = raw.read().replace("\r", "").replace("\n", " ")
                tfidf.addDocument(j, words)

run()
print tfidf.similarities(query.split(None))
