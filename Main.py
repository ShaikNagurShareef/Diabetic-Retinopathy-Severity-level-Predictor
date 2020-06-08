from flask import Flask, render_template, request
import DBHandler as db
import os

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html', methods=['POST', 'GET'])

@app.route("/", methods=['POST'])
def authentication():
    uid = request.form['UserId']
    pwd = request.form['Password']
    users = db.retrieveUsers()
    #print(users)
    for i in users:
        if uid==i[0] and pwd ==i[1]:
            return render_template('patient_details.html', uid = i[0])
    return render_template('invalid_login.html')
    
@app.route("/getData", methods=['POST'])
def getData():
    name = request.form['Name']
    mobile = request.form['Ph_No']
    gender = request.form['Gender']
    age = request.form['Age']
    test = request.form['Test']
    img_path = request.form['img_path']
    s0 = "--None--"
    s1 = "Maintain Controlled Blood Sugar Levels, Cholestrol & BP"
    s2 = "Use Hyvet Eye drops twice a day"
    s3 = "Use Lubimoist Eye drops twice a day"
    s4 = "Go for Laser Treatment"
    s5 = "Use Lubimoist Eye drops twice a day"
    s6 = "Use Nexthane Opthalmic Solution twice a day"
    s7 = "Go for Severity Test"

    if test=='binary':
        os.system("python BinaryClassTesting.py -l \""+img_path+","+str(name)+","+str(mobile)+","+str(gender)+","+str(age)+"\"")
        details = db.retrieveReport(name=str(name))
        if(details[0][0]=="DR Positive"):
            R1=s1
            R2=s7
        else:
            R1=s0
            R2=s0
        return render_template('report.html', name=name, mobile=mobile, gender=gender, age=age, img_path=img_path, file_name="./static/Reports/"+name+".pdf",details = details,r1=R1,r2=R2)
    else:
        os.system("python MultiClassTesting.py -l \""+img_path+","+str(name)+","+str(mobile)+","+str(gender)+","+str(age)+"\"")
        details = db.retrieveReport(name=str(name))
        print(details)
        if(details[0][1]=="No DR"):
            r1=s0
            r2=s0
        elif(details[0][1]=="Mild DR"):
            r1=s1
            r2=s2
        elif(details[0][1]=="Moderate DR"):
            r1=s1
            r2=s3
        elif(details[0][1]=="Severe DR"):
            r1=s3
            r2=s4
        else:
            r1=s5
            r2=s6
        return render_template('report.html', name=name, mobile=mobile, gender=gender, age=age, img_path=img_path, file_name="./static/Reports/"+name+".pdf",details = details,r1=r1,r2=r2)
		
if __name__ == "__main__":
    app.run(debug=True)