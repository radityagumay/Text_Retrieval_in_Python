text = {}

def run():
    for i in xrange(0, 10):
        text[i][0] = "hello"
        for j in xrange(0, 10):
            text[i][j] = "world"


run()
print "result", text
