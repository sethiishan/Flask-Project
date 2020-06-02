from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/database'
db = SQLAlchemy(app)

class Employess(db.Model):
    serialnumber = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    designation = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

@app.route("/" , methods = ['GET', 'POST'])
def employess():
	if(request.method=='POST'):
		name = request.form.get('name')
		designation = request.form.get('designation')
		address = request.form.get('address')
		phone = request.form.get('phone')
		entry = Employess( name = name, designation = designation, address = address, phone = phone )
		db.session.add(entry)
		db.session.commit()
	return render_template('index.html')



	    

    


