from flask import Flask,render_template,url_for,redirect,request
import csv
app=Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<page_name>')
def about(page_name):
	return render_template(page_name)


def database(data):
	with open('database.txt','a') as db:
		db.write(f'{data} \n')

def database_csv(data):
	email=data['email']
	subject=data['subject']
	message=data['message']
	with open('database.txt','a', newline='') as db:
		csv_writer = csv.writer(db,delimiter=' ',quotechar=' ')
		csv_writer.writerow(f'{email} {subject} {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		try:
			data=request.form.to_dict()
			database_csv(data)
			return render_template('thankyou.html')
		except:
			return 'data didnt get saved to database'			
	else:
		return 'something went wrong'		