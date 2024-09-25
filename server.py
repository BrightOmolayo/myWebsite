from flask import Flask,render_template,  request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        message = data['message']
        subject = data['subject']
        email = data["email"]
        test = data["test"]

        file = database.write(f'\n {name},{subject},{email},{test},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        firstname = data['firstname']
        lastname = data['lastname']
        subject = data['subject']
        email = data["email"]
        test = data["test"]
        message = data['message']

        csv_writer = csv.writer( database2, delimiter= ',',   quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname,lastname,subject,email,test,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
           data = request.form.to_dict()
           write_to_csv(data)
           return redirect('/thank-you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
    







































# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# @app.route("/blog")
# def blog():
#     return "<p>This is my python server</p>"

# @app.route("/blog/2020/chickens")
# def blog2():
#     return "<p>Hi, My name is Bright bsdhjjjjjjjjjjj</p>"

# @app.route("/favicon.ico")
# def blog():
    return "<p>This is my python server</p>"