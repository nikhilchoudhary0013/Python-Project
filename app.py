from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sweet heaven'

mysql = MySQL(app)

@app.route("/")
def index():
   
    return render_template('index.html')
@app.route("/index")
def home():
    cur = mysql.connection.cursor()
    cur.execute(" select * from homesw")
    ind = cur.fetchall()
    
    cur.execute("select * from hometeam")
    home = cur.fetchall()
    cur.close()        
    return render_template('index.html',home=home,ind=ind)


@app.route("/about")
def about():
    cur = mysql.connection.cursor()
    
    cur.execute("select * from about")
    staff = cur.fetchall()
    
    # cur.Execute("select * from aboutus")
    # aboutimg = cur.fetchall()
    cur.close()
    return render_template('about.html',staff=staff)
    
@app.route("/product")
def product():
    cur = mysql.connection.cursor()
    
    cur.execute("select * from product")
    pro = cur.fetchall()
    cur.close()
    
    return render_template('product.html',pro=pro)
@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/addcontact",methods=['GET','POST'])
def addcontact():
    if (request.method =='POST'):
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']

    cur=mysql.connection.cursor()
    cur.execute("insert into contact(name,email,subject,message)values(%s,%s,%s,%s)",(name,email,subject,message))
    mysql.connection.commit()    
    cur.close()        
    return render_template('contact.html')

@app.route("/service")
def service():
    cur = mysql.connection.cursor()
    cur.execute("select * from service")
    ser= cur.fetchall()
    
    cur.close()
    
    return render_template('service.html',ser=ser)

@app.route("/404")
def ni():
    return render_template('404.html')

@app.route("/team")
def team():
    cur = mysql.connection.cursor()
    
    cur.execute("select * from team")
    team = cur.fetchall()
    cur.close()
    
    return render_template('team.html',team=team)

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')


# Dummy Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route('/ourAdmin')
def dashboard():
    # cur = mysql.connection.cursor() 
    # cur.execute("select * from breakfast")
    # amenu=cur.fetchall()

    # cur = mysql.connection.cursor() 
    # cur.execute("select * from launch")
    # amenu+=cur.fetchall()

    # cur = mysql.connection.cursor() 
    # cur.execute("select * from dinner")
    # amenu+=cur.fetchall()
    return render_template("ourAdmin.html")


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            
            return redirect(url_for('dashboard'))  # Redirect to dashboard
        else:
            return "Invalid Credentials! Try Again."

    return render_template('login1.html')

app.run(debug=True)