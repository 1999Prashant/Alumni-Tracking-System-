from flask import Flask
from flask import render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from flask_login import logout_user
from flask import flash
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user
from flask import session

app = Flask(__name__)
 
app.config['SECRET_KEY'] = "thisisit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/alumni_system'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return AuthorityLogin.query.get(int(user_id))


# TABLE FOR COLLEGES
class Colleges(db.Model):
    __tablename__="colleges"
    College_ID = db.Column(db.Integer,primary_key=True)
    College_Name = db.Column(db.String(60))
    University = db.Column(db.String(60),nullable=False)
    Director_Name = db.Column(db.String(60),nullable=False)

#TABLE FOR AUTHORITY
class AuthorityLogin(db.Model,UserMixin):
    __tablename__="authority_login"
    id = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(60))
    Password = db.Column(db.String(60))
    Type = db.Column(db.String(60),nullable=False)
    University = db.Column(db.String(60),nullable=True)
    College = db.Column(db.String(60),nullable=True)

# Table for ALUMNI/STUDENT
class AspirantLogin(db.Model,UserMixin):
    __tablename__="aspirant_login"
    id = db.Column(db.Integer,primary_key=True)
    prn = db.Column(db.String(60))
    password = db.Column(db.String(60))
    type = db.Column(db.String(60),nullable=False)
    university = db.Column(db.String(60),nullable=True)
    clg = db.Column(db.String(60),nullable=True)

# Added By Prashant .. Track Alumni/Student Starts here
# Alumni Track Table
class AlumniTrack(db.Model):
    __tablename__="alumni_details"
    PRN = db.Column(db.String(80),primary_key=True)
    Name=db.Column(db.String(30))
    Year= db.Column(db.Integer,nullable=False)
    Branch= db.Column(db.String(40),nullable=True)
    Specialization= db.Column(db.String(40),nullable=True)
    Work_Ex=db.Column(db.String(80),nullable=True)
    College=db.Column(db.String(80),nullable=True)

# Student Track Table
class StudentTrack(db.Model):
    __tablename__="student_details"
    PRN = db.Column(db.String(60),primary_key=True)
    Name=db.Column(db.String(30))
    Year= db.Column(db.Integer,nullable=False)
    Alumni =db.Column(db.String(30))

# TABLE FOR REQUESTS
class Requests(db.Model):
    __tablename__="requests"
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(60))
    PRN =  db.Column(db.String(60))
    
# Routes Addes By Prashant
@app.route('/director/trackstudent')

def trackstudents():
    student=StudentTrack.query.all()
    return render_template("pages/DIR/directortrackstudents.html",student=student)

@app.route('/director/trackstudent',methods=['GET','POST'])
def trackstudents1():
    name=request.form.get('name')
    year=request.form.get('year')
    alumni=request.form.get('alumni')
    print(year,alumni,name)
    if(year!=None and alumni!=None):
        alumni=alumni.upper()
        student=StudentTrack.query.filter_by(Year=year,Alumni=alumni).all()
    elif(year!=None):
        student=StudentTrack.query.filter_by(Year=year).all()
    elif(alumni!=None):
        alumni=alumni.upper()
        student=StudentTrack.query.filter_by(Alumni=alumni).all()
    elif(alumni==None and year==None):
        student=StudentTrack.query.all()
    
    return render_template("pages/DIR/directortrackstudents.html",student=student)


@app.route('/DHE/trackalumni')
@login_required
def trackalumni1():
    alumni=AlumniTrack.query.all()
    return render_template("pages/DHE/dhetrackalumni.html",alumni=alumni)

@app.route('/DHE/trackalumni',methods=['GET','POST'])
def trackalumni13():
    college=request.form.get('college')
    if(college!=None):
        alumni=AlumniTrack.query.filter_by(College=college).all()
    else:
        alumni=AlumniTrack.query.all()
    return render_template("pages/DHE/dhetrackalumni.html",alumni=alumni)
   
@app.route('/director/trackalumni')
def trackalumni():
    alumni=AlumniTrack.query.all()
    return render_template("pages/DIR/directortrackalumni.html",alumni=alumni)

@app.route('/director/trackalumni',methods=['GET','POST'])
def trackalumni12():
    year =  request.form.get('year')
    branch =  request.form.get('branch')
    specialization =  request.form.get('specialization')
    work_ex =  request.form.get('work-ex')
    if(year!=None and branch !=None and specialization !=None and work_ex !=None):
        alumni=AlumniTrack.query.filter_by(Year=year,Branch=branch,Specialization=specialization,Work_Ex=work_ex).all()
    elif(year!=None and branch!=None and specialization!= None ):
        alumni=AlumniTrack.query.filter_by(Year=year,Branch=branch, Specialization=specialization).all()
    elif (branch!=None and specialization!= None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Branch=branch,Specialization=specialization,Work_Ex=work_ex).all()
    elif (year!=None and branch!=None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Year=year,Branch=branch,Work_Ex=work_ex).all()
    elif (year!=None and specialization!= None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Year=year,Specialization=specialization,Work_Ex=work_ex).all()
    elif(year!=None and branch!=None):
        alumni=AlumniTrack.query.filter_by(Year=year,Branch=branch).all()
    elif(year!=None and specialization!=None):
        alumni=AlumniTrack.query.filter_by(Year=year,Specialization=specialization).all()
    elif(branch!=None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Branch=branch,Work_Ex=work_ex).all()
    elif(branch!=None and specialization!=None):
        alumni=AlumniTrack.query.filter_by(Branch=branch,Specialization=specialization).all()
    elif(specialization!=None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Specialization=specialization,Work_Ex=work_ex).all()
    elif(branch!=None and work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Branch=branch,Work_Ex=work_ex).all()
    elif(year!=None):
        alumni=AlumniTrack.query.filter_by(Year=year).all()
    elif (branch!=None):
        alumni=AlumniTrack.query.filter_by(Branch=branch).all()
    elif (specialization!=None):
        alumni=AlumniTrack.query.filter_by(Specialization=specialization).all()
    elif (work_ex!=None):
        alumni=AlumniTrack.query.filter_by(Work_Ex=work_ex).all()
    elif (year==None and branch==None and specialization==None and work_ex==None):
        alumni=AlumniTrack.query.filter_by().all()
    print(year,branch,specialization,work_ex)
    return render_template("pages/DIR/directortrackalumni.html",alumni=alumni)
# ENds Here

@app.route('/')
def login_normal():
    return render_template('input.html')

@app.route('/',methods=['GET','POST'])
def login():
    usertype =  request.form.get('usertype')
    if usertype == "DHE":
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthorityLogin.query.filter_by(Email = email).first()
        if not user or (password!=user.Password):
            flash("Invalid Email or Password")
            return redirect(url_for('login'))
        login_user(user)
        session['key']="DHE"
        return redirect(url_for("trackalumni1"))
    # Director Login    
    elif usertype=="DIR":
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthorityLogin.query.filter_by(Email = email).first()
        if not user or (password!=user.Password):
            flash("Invalid Email or Password")
            return redirect(url_for('login'))
        login_user(user)
        session['key']="Director"
        return redirect(url_for("dashboarddirector"))

    # Alumni
    elif usertype=="alumni":
        prn = request.form.get('prn')
        password = request.form.get('password')
        clg = request.form.get('clgselect')
        university = request.form.get('universityselect')

        user = AspirantLogin.query.filter_by(prn = prn).first()
        print(prn,password,clg,university)
        print(user.prn,user.password,user.clg,user.university)
        if user.type=="student" or user.type=="pending":
            if not user or (password!=user.password) or university!=user.university or clg!=user.clg:
                print("Entered")
                flash("Invalid Details")
                return redirect(url_for('login'))
            else:
                if user.type == "student":
                    data = db.engine.execute("SELECT s.name,s.prn from aspirant_login a INNER JOIN student_details s where a.PRN=s.PRN and a.prn={}".format(prn))
                    
                    for i in data:
                        db.session.add(Requests(Name=i[0],PRN=i[1]))
                        break
                    
                user.type="pending"
                db.session.commit()
                login_user(user)
                return render_template("pages/alumni/dashboardalumni_disabled.html")

        elif user.type=="alumni":
            if not user or (password!=user.password) or university!=user.university or clg!=user.clg or usertype!=user.type:
                flash("Invalid Details")
                return redirect(url_for('login'))
        
            login_user(user)
            return render_template("pages/alumni/dashboardalumni.html")

    # Student
    elif usertype=="student":
        prn = request.form.get('prn')
        password = request.form.get('password')
        clg = request.form.get('clgselect')
        university = request.form.get('universityselect')

        user = AspirantLogin.query.filter_by(prn = prn).first()
        # print(user.prn,user.password,user.university,user.clg,user.type)
        # print(prn,password,university,clg,usertype)
        if clg is None:
            if not user or (password!=user.password) or university!=user.clg or usertype!=user.type:
                print("entered")
                flash("Invalid Details")
                return redirect(url_for('login'))
            else:
                # print("PRashant")
                login_user(user)
                return render_template("pages/student/studentprofile.html")
        else:
            if not user or (password!=user.password) or university!=user.university or clg!=user.clg or usertype!=user.type:
                flash("Invalid Details")
                return redirect(url_for('login'))
            else:
                print("Furkhan MGM")
                login_user(user)
                return redirect(url_for("schedulesstudents"))
        print(user)
        
        
            

        
@app.route('/notfound')
def notfound():
    return render_template("/index.html")

@app.route('/student/schedules')
@login_required
def schedulesstudents():
    return render_template('pages/student/studentschedules.html')


@app.route('/alumni/dashboard')
@login_required
def dashboardalumni():
    return render_template("pages/alumni/dashboardalumni.html")

@app.route('/alumni/dashboard_disabled')
@login_required
def dashboardalumnidisabled():
    return render_template("pages/alumni/dashboardalumni_disabled.html")

@app.route('/director/dashboard')
@login_required
def dashboarddirector():
    return render_template("pages/DIR/directordashboard.html")
    

@app.route('/alumni/donation')
@login_required
def aldonatecollegedevlp():
    return render_template("pages/alumni/alumnidonation.html")
 
@app.route('/dhe/dashboard')
@login_required
def dashboarddhe():
    return render_template("pages/DHE/dashboarddhe.html")
  
@app.route('/alumni/profile')
@login_required
def aluminiprofile():
    return render_template("pages/alumni/profile.html")

@app.route('/alumni/www.facebook.com')
def alumnifacebook():
    return redirect("https://www.facebook.com/mgmcen/",code=302)

@app.route('/alumni/www.twitter.com')
def alumnitwitter():
    return redirect("https://www.twitter.com",code=302)

@app.route('/alumni/www.insta.com')
def alumniinsta():
    return redirect("https://www.instagram.com/visiotech_16/?hl=en",code=302)

@app.route('/alumni/www.google.com')
def alumnigoogle():
    return redirect("https://www.google.com",code=302)

@app.route('/student/profile')
@login_required
def alumnistudentprofile():
    return render_template("pages/student/studentprofile.html")

@app.route('/student/events')
@login_required
def studentEvents():
    return render_template("pages/student/studentevents.html")
    
@app.route('/alumni/tablealumni')
@login_required
def table():
    return render_template("pages/alumni/tablealumni.html")

@app.route('/director/managefunddirector')
@login_required
def managefunddirector():
    return render_template("pages/DIR/managefunddirector.html")

@app.route('/director/authentication')
@login_required
def authentication():
    dt = Requests.query.all()
    return render_template("pages/DIR/authentication.html",data = dt)

    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('mainpage'))

@app.route("/alumni/authenticate",methods=['GET','POST'])
def authenticate():
    if request.method=='POST':
        val = request.get_data('data')
        # return val
        user = AspirantLogin.query.filter_by(prn = val).first()
        print("Type class of User ",type(user))
        print("Type of User",user.type)
        user.type="alumni"
        print("PRN",user.prn)
        db.session.commit()
        dt = Requests.query.filter_by(PRN=val).first()
        db.session.delete(dt)
        db.session.commit()
        return "Alumni Approved"

@app.route("/alumni/authenticate/reject",methods=['GET','POST'])
def reject():
    if request.method=='POST':
        val = request.get_data('data')
        # return val
        user = AspirantLogin.query.filter_by(prn = val).first()
        user.type="student"
        db.session.commit()
        return "Request Rejected"

@app.route('/mainpage')
def mainpage():
    return render_template("mainpage.html")

@app.route("/tmp")
def tmp():
    return render_template("tmp.html")
    
if __name__=='__main__':
    app.run(debug=True)