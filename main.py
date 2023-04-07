import fixieai

BASE_PROMPT = (
    "I am an agent that answers questions using the script of the TV show Seinfeld."
    "User may have follow-up questions that refers to something mentioned before but I "
    "always do Ask Func[fixie_query_corpus] with a complete question, without any "
    "reference."
)

FEW_SHOTS = """
Q: What is the first job that George lies about having?
Ask Func[fixie_query_corpus]: What is the first job that George lies about having?
Func[fixie_query_corpus] says: In the first episode, George lies to Vanessa and tells her that he is an architect.
A: In the first episode, George lies to Vanessa and tells her that he is an architect.

Q: How does Mr. Pitt eat his Snickers?
Ask Func[fixie_query_corpus]: How does Mr. Pitt eat his Snickers?
Func[fixie_query_corpus] says: Elaine tells George and Jerry that Mr. Pitt eats his Snickers with a knife and fork.
A: Elaine tells George and Jerry that Mr. Pitt eats his Snickers with a knife and fork.
Q: Why does he do it?
Ask Func[fixie_query_corpus]: Why does Mr. Pitt eat his Snickers with a knife and fork?
Func[fixie_query_corpus] says: George guesses that Mr. Pill probably eats his Snickers with a knife and fork because he doesn't want to get chocolate on his fingers.
A: George guesses that Mr. Pill probably eats his Snickers with a knife and fork because he doesn't want to get chocolate on his fingers.
"""

URLS = [
    "https://raw.githubusercontent.com/luonglearnstocode/Seinfeld-text-corpus/master/corpus.txt",
]

CORPORA = [fixieai.DocumentCorpus(urls=URLS)]
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS, CORPORA, conversational=True)