
class Colleges(db.Model):
    __tablename__="colleges"
    College_ID = db.Column(db.Integer,primary_key=True)
    College_Name = db.Column(db.String(60))
    University = db.Column(db.String(60),nullable=False)
    Director_Name = db.Column(db.String(60),nullable=False)

#TABLE FOR AUTHORITY
class AuthorityLogin(db.Model):
    __tablename__="authority_login"
    Email = db.Column(db.Integer,primary_key=True)
    Password = db.Column(db.String(60))
    Type = db.Column(db.String(60),nullable=False)
    University = db.Column(db.String(60),nullable=True)
    College = db.Column(db.String(60),nullable=True)
 