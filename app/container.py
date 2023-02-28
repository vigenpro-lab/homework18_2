from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.data_base import db
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from app.services.user import UserService
from app.dao.user import UserDao
from app.services.auth import AuthService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDao(db.session)
user_service = UserService(dao=user_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

auth_service = AuthService(user_service)
