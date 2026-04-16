from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', back_populates='comments')

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post')