article = "English has two articles: the and a/an. The is used to refer to specific or particular nouns; a/an is used to modify non-specific or non-particular nouns. We call the the definite article and a/an the indefinite article. For example, if I say, Let's read the book, I mean a specific book."
subtitution = {
    "English":"French",
    "We":"They",
    "For example":"Instead",
}
for key, value in subtitution.items():
  article = article.replace(key, value)
print(article)