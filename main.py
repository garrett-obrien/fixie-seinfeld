import fixieai

BASE_PROMPT = (
    "I am an expert in trivia about the TV show Seinfeld. I answer questions about the show confidently and concisely."
    # "User may have follow-up questions that refers to something mentioned before but I "
    # "always do Ask Func[fixie_query_corpus] with a complete question, without any "
    # "reference."
    "I only route queries to reference text about Seinfeld. I always do Ask Func[fixie_query_corpus] when answering."
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
    "https://raw.githubusercontent.com/garrett-obrien/fixie-seinfeld/main/seinfeld-text-corpus.txt",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_1)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_2)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_3)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_4)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_5)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_6)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_7)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_8)",
    "https://en.wikipedia.org/wiki/Seinfeld_(season_9)",
   # "https://seinfeld.fandom.com/wiki/*", 
]

CORPORA = [fixieai.DocumentCorpus(urls=URLS)]
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS, CORPORA, conversational=True,
llm_settings=fixieai.LlmSettings(temperature=0, model="openai/gpt-4", maximum_tokens=2000)
)