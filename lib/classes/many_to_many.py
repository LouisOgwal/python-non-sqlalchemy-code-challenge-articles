class Article:
    all = [] 

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    
        author.add_article(self)
        magazine.add_article(self)
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    def __str__(self):
        return self.title


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        """Add an article to the author's list if it isn't already present."""
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        """Return all articles written by the author."""
        return self._articles

    def magazines(self):
        """Return a list of unique magazines where the author has articles."""
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        """Return a list of unique categories of magazines where the author has published."""
        return list(set(article.magazine.category for article in self._articles))

    def __str__(self):
        return self._name


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def add_article(self, article):
        """Add an article to the magazine's list if it isn't already present."""
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        """Return all articles in this magazine."""
        return self._articles

    def contributors(self):
        """Return a list of unique authors who have contributed to the magazine."""
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        """Return a list of titles of all articles in the magazine, or None if no articles exist."""
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        """Return authors who have written more than 2 articles for the magazine."""
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    def __str__(self):
        return self._name

        