import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import csv
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('Please select a file...', "warning")
            return redirect(request.url)
        
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        file_name=file.filename.split('.')
        if file and secure_filename(file.filename) and file_name[1]=='csv':
        #Code should check if the file is a .csv file otherwise reject with a flash
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies 
                        WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            for row in csv.DictReader(stream, delimiter=','):
                
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data            
                if row["company_name"] and row["address"] and row["city"] and row["state"] and row["zip"] and row["web"]:
                    companies.append({"name": row["company_name"], "address": row['address'], "city": row['city'],"country": row["country"], "state": row['state'], "zip": row['zip'], "website": row['web']})

                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data
                if row["first_name"] and row["last_name"] and row["email"] and row["company_name"]:
                    employees.append({"first_name": row["first_name"], "last_name": row["last_name"], "email": row['email'], "company_name": row["company_name"]})
    
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    query=DB.selectOne("SELECT Count(*) as count from IS601_MP2_Companies")
                    if query.status:
                        count = query.row
                    val=count['count']
                    # TODO importcsv-5 display flash message about number of companies inserted
                    flash(f"Successfully inserted {val} records in Company's DB","success")
                except Exception as e:
                    traceback.print_exc()
                    flash("Sorry, there was some error in inserting the data in Company's DB", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                flash("It seems like there is no data to insert in Company's DB, try with another CSV", "info")
                
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    flash(f"Successfully inserted {len(employees)} records in Employee's DB","success")
                except Exception as e:
                    traceback.print_exc()
                    flash("Sorry, there was some error in inserting the data in Employee's DB", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no companies were loaded
                flash("It seems like there is no data to insert in Employee's DB, try with another CSV","info")
        else:
            flash("It seems like this is not a CSV file, please import CSV", "danger")
    return render_template("upload.html")
