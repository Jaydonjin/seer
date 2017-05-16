from db import article


def make_create_article(id, title, author, body, liketime, pushdate):
    tmp_article = article()
    tmp_article.id = id
    tmp_article.title = title
    tmp_article.body = body
    tmp_article.auther = author
    tmp_article.liketime = liketime
    tmp_article.pushdate = pushdate
    return tmp_article
