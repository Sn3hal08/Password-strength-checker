from flask import Flask,render_template,request
import re
app=Flask(__name__)

def check_pass_strength(password):
    strength=0
    suggestions=[]
    common_passwords = ["123456", "password", "qwerty","abcdef"]

    if password.lower() in common_passwords:
        suggestions.append("This is a very common password!")

    if len(password)>=8:
        strength+=1
    else:
        suggestions.append("Password must be atleast of 8 characters")

    if re.search(r"[A-Z]",password):
        strength +=1
    else:
        suggestions.append("Add Uppercase letters")

    if re.search(r"[a-z]",password):
        strength +=1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]",password):
        strength +=1
    else:
        suggestions.append("Should have atleast one number")

    if re.search(r"[!@#$%^&*()<>,.?/:;|}{]",password):
        strength +=1
    else:
        suggestions.append("Add specialcharacters")

    if strength <=2:
        result="Weak"
    elif strength<=4:
        result="Medium"
    else:
        result ="Strong"

    return result,suggestions

@app.route('/',methods=['GET','POST'])
def index():
    result=""
    suggestions=[]

    if request.method=='POST':
        password=request.form['password']
        result,suggestions=check_pass_strength(password)

    return render_template('index.html',result=result,suggestions=suggestions)

if __name__ == "__main__":
   app.run(debug=True)


