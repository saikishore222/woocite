from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
   return render_template("home.html")
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      first_name=request.form['first_name']
      middle_name=request.form['middle_name']
      last_name=request.form['last_name']
      company_name=request.form['company_name']
      mobile=request.form['re_mob']
      email=request.form['re_em']
      dob=request.form['dob_']
      pancard=request.form['pan_card']
      pincode=request.form['pin_code']
      District=request.form['District']
      state=request.form['state']
      city=request.form['city']
      address=request.form['address']
      acard=request.form['afile']
      pcard=request.form['pfile']
      print(first_name)
      print(pincode)
      print(acard)
      conn=sqlite3.connect("formdata.db")
      c=conn.cursor()
      try:
            c.execute("""CREATE TABLE  kyc1
                        (firstname text,
                        middlename text,
                        lastname text,
                        company text,
                        mobile text,
                        email text,
                        dob  text,
                        pancard text,
                        pincode text,
                        district text,
                        state text,
                        city text,
                        address text,
                        acard blob,
                        pcard blob);""")
      except:
               pass
      entities=(first_name,middle_name,last_name,company_name,mobile,email,dob,pancard,pincode,District,state,city,address,acard,pcard)
      c.execute('''INSERT INTO kyc1(firstname,middlename,lastname,company, mobile,email,dob,pancard,pincode,district,state,city,address,acard,pcard) VALUES(?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?)''', entities)
      c.execute("SELECT * FROM  kyc1")
      print(c.fetchall())
      print("saikishore")
      conn.commit()
      return render_template("result.html")
if __name__ == '__main__':
   app.run()
