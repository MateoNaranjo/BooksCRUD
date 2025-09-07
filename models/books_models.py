class Books():
    def __init__(self, id, title, author, timestamp):
        self.id = id
        self.title = title
        self.author = author
        self.timestamp = timestamp
    
    def __repr__(self):
        return f'id.{self.id}'
    
    def serialize(self):
        return{
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'timestamp':self.timestamp   
        }