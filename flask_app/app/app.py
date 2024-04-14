from flask import Flask, render_template, request
from pymysql import connections
import os

from utils import get_key_from_s3_uri, get_bucket_name_from_s3_uri, download_image_from_s3, get_filename_with_extension_from_s3_uri

app = Flask(__name__)

DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "passwors"
DATABASE = os.environ.get("DATABASE") or "employees"
DBPORT = int(os.environ.get("DBPORT")) or 3306
S3_IMAGE_URI = os.environ.get("S3_IMAGE_URI") or "s3://clo835testbucketerccardiel/unpath/bg_1.jpg"
GROUP_NAME = os.environ.get("GROUP_NAME") or "Mexindian Squad"
GROUP_SLOGAN = os.environ.get("GROUP_SLOGAN") or "Generic slogan"
# Create a connection to the MySQL database
db_conn = connections.Connection(
    host= DBHOST,
    port=DBPORT,
    user= DBUSER,
    password= DBPWD,
    db= DATABASE
)
output = {}
table = 'employee';
image_name = get_filename_with_extension_from_s3_uri(S3_IMAGE_URI)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('addemp.html', image_name=image_name, group_name=GROUP_NAME, group_slogan=GROUP_SLOGAN)

@app.route("/about", methods=['GET','POST'])
def about():
    return render_template('about.html', image_name=image_name, group_name=GROUP_NAME, group_slogan=GROUP_SLOGAN)

@app.route("/addemp", methods=['POST'])
def add_employee():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    primary_skill = request.form['primary_skill']
    location = request.form['location']
    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql,(emp_id, first_name, last_name, primary_skill, location))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('addempoutput.html', name=emp_name, image_name=image_name, group_name=GROUP_NAME, group_slogan=GROUP_SLOGAN)

@app.route("/getemp", methods=['GET', 'POST'])
def get_employee():
    return render_template("getemp.html", image_name=image_name, group_name=GROUP_NAME, group_slogan=GROUP_SLOGAN)


@app.route("/fetchdata", methods=['GET','POST'])
def fech_data():
    emp_id = request.form['emp_id']

    output = {}
    select_sql = "SELECT emp_id, first_name, last_name, primary_skill, location from employee where emp_id=%s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(select_sql,(emp_id))
        result = cursor.fetchone()
        # Add No Employee found form
        output["emp_id"] = result[0]
        output["first_name"] = result[1]
        output["last_name"] = result[2]
        output["primary_skills"] = result[3]
        output["location"] = result[4]
    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render_template("getempoutput.html", id=output["emp_id"], fname=output["first_name"],
                           lname=output["last_name"], interest=output["primary_skills"], location=output["location"], image_name=image_name, group_name=GROUP_NAME, group_slogan=GROUP_SLOGAN)

if __name__ == '__main__':
    bucket = get_bucket_name_from_s3_uri(S3_IMAGE_URI)
    key = get_key_from_s3_uri(S3_IMAGE_URI)
    output_file_path = f"static/{image_name}"
    download_image_from_s3(bucket, key, output_file_path)
    app.run(host='0.0.0.0',port=81,debug=True)
