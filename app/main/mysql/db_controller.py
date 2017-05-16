from db import article
from app import db
from db_utils import make_create_article


def create_article(title, author, body, like_time, pushdate):
    max_id = db.session.query(db.func.max(article.id)).scalar()
    article_id = max_id + 1
    articles = make_create_article(article_id, title, author, body, like_time, pushdate)
    db.session.add(articles)
    db.session.commit()
    return 'success'


def get_article_by_id(id):
    cur_article = db.session.query(article).filter(article.id == id).first()
    if cur_article:
        article_title = cur_article.title
        article_author = cur_article.auther
        article_body = cur_article.body
        article_liketime = cur_article.liketime
        article_pushdate = cur_article.pushdate
        article_result = {'title': article_title, 'author': article_author, 'body': article_body,
                          'like_time': article_liketime, 'push_date': article_pushdate}
        return article_result
    else:
        return 404
