import codecs, glob
import tfidf_2

text_dirs = ["articles/*"]
table = tfidf_2.tfidf()

query_document = "Worries about the deficit concerns about China do, however, remain. China's currency remains pegged to the dollar"

def run():
    for i in text_dirs:
        documents = glob.glob(i + "/*.txt")
        for j in documents:
            with codecs.open(j, "r", "utf-8") as raw:
                words = raw.read().replace("\r", "").replace("\n", " ")
                table.addDocument(j, words)


run()
print table.similarities(query_document.split(None))
