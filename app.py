from flask import Flask, render_template, request
import ibm_db

app= Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb; HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; PORT=30875; UID=fqd48971; PASSWORD=l8W5crGrzgaLYU5e; SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;", '','')
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        uname=request.form['username']
        pword = request.form['password']
        print(uname, pword)
        sql = 'SELECT * FROM  REGISTER WHERE USERNAME=?'
        stmt=ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, uname)
        ibm_db.bind_param(stmt, 2, pword)
        ibm_db.execute(stmt)
        out=ibm_db.fetch_assoc(stmt)
        print(out)
        if out == 'flase':
            msg = "Invalid Credentails"
            return render_template("login.html", login_message = msg)
        else:
            role= out ['ROLE']
            if role == 0:
                return render_template("profile.html")
            elif role ==1:
                return render_template("")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
