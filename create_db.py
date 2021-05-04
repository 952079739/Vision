from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True)
    user_password = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True)
    user_file = db.Column(db.String(100), unique=True)
    user_email = db.Column(db.String(100), nullable=True)
    movie = db.relationship('Movie', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.user_name)


class Movie(db.Model):
    __tablename__ = 'movie'
    __table_args__ = {'extend_existing': True}
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), unique=True)
    movie_address = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return '<Movie {}>'.format(self.movie_name)



