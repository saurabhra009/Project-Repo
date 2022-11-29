from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    company_id = request.args.get("company_id")
    if company_id:
        args=[]
        query="""SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name 
    FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON c.id=e.company_id WHERE 1=1 AND company_id=%s"""
        args.append(company_id)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
        return render_template("list_employees.html", resp=rows)
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name
    FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON c.id=e.company_id WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get("first_name")
    ln = request.args.get("last_name")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND first_name like %s"
        args.append(f'%{fn}%')
        
    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND last_name like %s"
        args.append(f'%{ln}%')
        
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %s"
        args.append(f'%{email}%')
        
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND company_id = %s"
        args.append(int(company))
        
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        print("Column",column)
        print("Order", order)
        if column in ["first_name", "last_name", "email", "company_name"] and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
            
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
        # technically this should follow the same rules as col/order
        # but it seems to work with the placeholder mapping with
        # this connector
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
        
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    else:
        flash("Limit is out of bound", "danger")
        return redirect(url_for("employee.search"))
    #print("query",query)
    #print("args", args)
    try:
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash("Sorry, data is not available", "danger")
        
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", resp=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        fn = request.form.get("first_name")
        ln = request.form.get("last_name")
        company = request.form.get("company",None)
        #company doesn't require a flash and may be empty/None
        email = request.form.get("email")
        if fn=="":
            flash("First name is missing", "danger")
            #first_name is required (flash proper error message)
            return redirect(url_for("employee.add"))
        if ln=="":
            flash("Last name is missing", "danger")
            #last_name is required (flash proper error message)
            return redirect(url_for("employee.add"))
        if email=="":
            flash("Email is missing", "danger")
            #email is required (flash proper error message)
            return redirect(url_for("employee.add"))
        has_error = False # use this to control whether or not an insert occurs
        if not has_error:
            try:
                #Proper INSERT query should be visible
                result = DB.insertOne("INSERT INTO IS601_MP2_Employees (first_name, last_name,company_id,email) VALUES(%s, %s, %s, %s)",fn, ln,company,email) 
                # TODO add-6 add query and add arguments
                #Code should retrieve first_name, last_name, company (id), email
                if result.status:
                    flash("Employee Record has been successfully created", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                #Except block should have a user friendly message flashed and a print() of the exception
                flash("Sorry, Employee's data cannot be added", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    row = None
    if id is None:
        flash("Please enter ID", "danger")
        return redirect(url_for("employee.search"))
    else: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
            has_error=False
            fn = request.form.get("first_name")
            ln = request.form.get("last_name")
            company_id = request.form.get("company", None)
            email = request.form.get("email")
            if fn=="":
                flash("First name cannot be empty", "danger")
                has_error=True
            if ln=="":
                flash("Last name cannot be empty", "danger")
                has_error=True
            if email=="":
                flash("Email cannot be empty", "danger")
                has_error=True
            data = [fn, ln, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                if not has_error:
                    result = DB.update("UPDATE IS601_MP2_Employees SET first_name=%s, last_name=%s, company_id=%s, email=%s WHERE id = %s", *data)
                    if result.status:
                        flash("Successfully updated Employee's record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash("Sorry, Employee's data cannot be updated", "danger")
                
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a company
            result = DB.selectOne("SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name from IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON e.company_id=c.id WHERE e.id = %s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Employee's data cannot be fetched", "danger")
            
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    # make a mutable dict
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
            if result.status:
                flash("Deleted record from Employee's DB successfully", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash("Sorry, data cannot be deleted from Employee's DB", "danger")
        
        # TODO pass along feedback
        # remove the id args since we don't need it in the list route
        # but we want to persist the other query args
        del args["id"]
    return redirect(url_for("employee.search", **args))
