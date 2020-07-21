from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dbBooks.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    author_cpf = Column(String, ForeignKey('authors.cpf'))
    author = relationship('Authors')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Categories')
    year = Column(Integer)
    amount = Column(Integer)
    price = Column(Float(2), )


    def __repr__(self):
        return '<Book:> {}'.format(self.title)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Authors(Base):
    __tablename__ = 'authors'
    name = Column(String(40), index=True)
    cpf = Column(String(11), primary_key=True)

    def __repr__(self):
        return '<Author:> {}'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Categories(Base):
    __tablename__ ='categories'
    id = Column(Integer, primary_key=True)
    category = Column(String(40), index=True)

    def __repr__(self):
        return '<Category:> {}'.format(self.category)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

