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
        # If the user does not select a file, the browser doesn't submits an empty file without a filename.
        if file.filename == '':
            flash('It seems like no file has been selected, please select a file', "warning")
            return redirect(request.url)
        
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        #try:
        """
        UCID: sp2943
        Date: 28th November 2022
        We are splitting the file name using '.' as seperator and check if filename is csv or not in the if statement itself, 
        if it isn't and other conditions satisfy then flash message is displayed accordingly.  
        """
        file_name=file.filename.split('.')
        if file and secure_filename(file.filename) and file_name[1]=='csv':
            
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, 
                        state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies 
                        WHERE name = %(company_name)s LIMIT 1)) ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies 
                        WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            """
            UCID: sp2943
            Date: 28th November 2022
            csv. DictReader is utilized to read a csv file stream as a dictionary using commas as delimiters.
            """
            for row in csv.DictReader(stream, delimiter=','):
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                """
                UCID: sp2943
                Date: 28th November 2022
                Data for the company and employees is appended to the appropriate tables as a dictionary, with the key being 
                the column name and the value being the one obtained from the rows received from the csv file stream.
                """
                if row["company_name"] and row["address"] and row["city"] and row["state"] and row["zip"] and row["web"]:
                    companies.append({"name": row["company_name"], "address": row['address'], "city": row['city'],"country": row["country"], 
                    "state": row['state'], "zip": row['zip'], "website": row['web']})

                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data

                if row["first_name"] and row["last_name"] and row["email"] and row["company_name"]:
                    employees.append({"first_name": row["first_name"], "last_name": row["last_name"], "email": row['email'], "company_name": row["company_name"]})
            
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    """
                    UCID: sp2943
                    Date: 28th November 2022
                    The length of the businesses table allows us to calculate the number of records added and the flash message id shown correspondingly.
                    """
                    query=DB.selectOne("SELECT COUNT(*) as count FROM IS601_MP2_Companies")
                    if query.status: 
                        count=query.row
                    flash(f"Inserted {count['count']} records in Company's table","success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error processing the records in Company's table, please try again", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                """
                UCID: sp2943
                Date: 28th November 2022
                If no company data has been loaded, or if the list is blank, a flash message will appear.
                """
                flash("There is no data in the selected file","info")
            if len(employees) > 0:
                """
                    UCID: sp2943
                    Date: 28th November 2022
                    The length of the employees table allows us to calculate the number of records entered and 
                    the flash message id shown correspondingly.
                """
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    flash(f"Inserted {len(employees)} records in Employee's table","success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error processing the records in Employee's table, please try again", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no companies were loaded
                """
                UCID: sp2943
                Date: 28th November 2022
                If no employees data were loaded, or if the list is empty, a flash message is displayed.
                """
                flash("There is no data in the selected file","info")
        else:
            """
                    UCID: sp2943
                    Date: 28th November 2022
                    If the file format is incorrect, such as csv, a flash notice is displayed.
            """
            flash("File format is not supported, please select a CSV file", "danger")
    return render_template("upload.html")

