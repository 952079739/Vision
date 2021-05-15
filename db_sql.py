from app import db
from create_db import User, Movie


def select_user(name, password):
    user = User.query.filter(User.user_name == name, User.user_password == password).first()
    return user


def select_user_name(name):
    user = User.query.filter(User.user_name == name).first()
    return user


def select_movie(id):
    movie = Movie.query.filter(Movie.movie_id == id).first()
    return movie


def select_movie_name(name):
    movie = Movie.query.filter(Movie.movie_name == name).first()
    return movie


def select_user_movie(username):
    movie_list = Movie.query.filter(Movie.user_name == username)
    return movie_list


def add_user(user_name, password, userfile):
    user = User(user_name=user_name, user_password=password, user_file=userfile)
    db.session.add_all([user])
    db.session.commit()


def update_user_password(user_name, password):
    user = User.query.filter(User.user_name == user_name).first()
    user.user_password = password
    db.session.commit()


def update_user_name(user_name, update_name):
    user = User.query.filter(User.user_name == user_name).first()
    user.user_name = update_name
    db.session.commit()


def add_movie(movie_name, movie_address, user_id):
    movie = User(movie_name=movie_name, movie_address=movie_address, user_id=user_id)
    db.session.add_all([movie])
    db.session.commit()



#
# def add_position(p_name, p_type, p_treatment, p_place, c_id):
#     position = Position(name=p_name, position_type=p_type, position_treatment=p_treatment,
#                         position_place=p_place, company_id=c_id)
#     db.session.add_all([position])
#     db.session.commit()

