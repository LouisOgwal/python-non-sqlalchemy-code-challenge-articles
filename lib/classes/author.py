class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

  def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article
           
    def get_articles(self):
        return self._articles

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def __str__(self):
        return self._name