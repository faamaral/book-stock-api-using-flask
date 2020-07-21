from models import Authors, db_session

def insert_authors():
    author = Authors(name='Scr2', cpf='00000000002')
    print(author)
    author.save()

def insert_books():
    pass

def search_author():
    author = Authors.query.all()
    print(author)
    author = Authors.query.filter_by(name='Scr2').first()
    print(author.cpf)

def change_author():
    author = Authors.query.filter_by(name='Scr2').first()
    author.name = 'Scr0'
    author.save()

def delete_author():
    author = Authors.query.filter_by(name='Scr').first()
    author.delete()


if __name__ == '__main__':
    #insert_authors()
    #search_author()
    change_author()