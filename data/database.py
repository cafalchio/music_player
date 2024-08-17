from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    track_number = Column(Integer)
    bitrate = Column(Integer)

    album_id = Column(Integer, ForeignKey("albums.id"), nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    album = relationship("Album", back_populates="songs")
    artist = relationship("Artist", back_populates="songs")


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")
    genres = relationship("Genre", secondary="album_genres", back_populates="albums")


class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="artist")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    albums = relationship("Album", secondary="album_genres", back_populates="genres")


class AlbumGenre(Base):
    __tablename__ = "album_genres"
    album_id = Column(Integer, ForeignKey("albums.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)


class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="playlists")
    songs = relationship("Song", secondary="playlist_songs", back_populates="playlists")


class PlaylistSong(Base):
    __tablename__ = "playlist_songs"
    playlist_id = Column(Integer, ForeignKey("playlists.id"), primary_key=True)
    song_id = Column(Integer, ForeignKey("songs.id"), primary_key=True)
    playlist = relationship("Playlist", back_populates="songs")
    song = relationship("Song", back_populates="playlists")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    playlists = relationship("Playlist", back_populates="user")


Base.metadata.create_all(engine)
