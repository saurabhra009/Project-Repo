from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    """
    UCID: sp2943
    Date: 28th November 2022
    Request.args.get is used to obtain the company id. If it exists, perform a select query to pick the needed data for a given 
    company id, then join the two databases using LEFT JOIN with company id as the linking column. 
    """
    company_id = request.args.get("company_id")
    if company_id:
        args=[]
        query="""SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name 
    FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON c.id=e.company_id WHERE 1=1 AND company_id=%s LIMIT 10"""
        args.append(company_id)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
        return render_template("list_employees.html", resp=rows)
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    """
    UCID: sp2943
    Date: 28th November 2022
    The select query retrieves the relevant data from the company and employee databases by utilizing a left join that connects 
    the two datasets based on the business id field.
    """
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name as company_name
    FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON c.id=e.company_id WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company"]
    
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    """
    UCID: sp2943
    Date: 28th November 2022
    Using request.args.get, query to filter based on the name, nation, and state" ORDER BY is used to sort the list of 
    employee data depending on the column and order specified. Limit is also introduced to display the list of firms.
    """
    fn = request.args.get("fn")
    ln = request.args.get("ln")
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
        if column in ["first_name", "last_name", "email", "company_name"] and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        # technically this should follow the same rules as col/order but it seems to work with the placeholder mapping with this connector
        query += " LIMIT %s"
        args.append(int(limit))
    
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    else:
        flash("Limit is out of bound", "danger")
        return redirect(url_for("employee.search"))

    print("query",query)
    print("args", args)
    try:
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        """
        UCID: sp2943
        Date: 28th November 2022
        In the event that the data is not accessible for selection, a user-friendly flash message is displayed.
        """
        flash("Unfortunately, data is not available", "danger")
    
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", resp=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        """
        UCID: sp2943
        Date: 28th November 2022
        Request.form.get is used to obtain the needed set of data from the form.
        If the needed set of values is lacking, a flash message is displayed and the user is routed to the add page.
        """
        fn = request.form.get("first_name")
        ln = request.form.get("last_name")
        company = request.form.get("company",None) # TODO add-4 company (may be None)
        email = request.form.get("email")
        
        # TODO add-2 first_name is required (flash proper error message)
        if fn=="":
            flash("First name is not there, please enter first name", "danger")
            return redirect(url_for("employee.add"))
        
        # TODO add-3 last_name is required (flash proper error message)
        if ln=="":
            flash("Last name is not there, please enter last name", "danger")
            return redirect(url_for("employee.add"))
        
        # TODO add-5 email is required (flash proper error message)
        if email=="":
            flash("Email is not there, please enter email", "danger")
            return redirect(url_for("employee.add"))
        
        has_error = False # use this to control whether or not an insert occurs
        """
        UCID: sp2943
        Date: 28th November 2022
        If the has_error flag check returns FALSE, insert data into the businesses database and display a successful insertion flash message.
        """
        if not has_error:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP2_Employees (first_name, last_name,company_id,email) VALUES(%s, %s, %s, %s)",fn, ln,company,email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Employee record has been created successfully", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                """
                UCID: sp2943
                Date: 28th November 2022
                A user-friendly flash message has been added. If no company data is entered, there is a processing issue.
                """
                flash("Unfortunately, employee data cannot be added, there is some error", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    """
    UCID: sp2943
    Date: 28th November 2022
    Request.args is used to retrieve the ID, and if there is none, a flash message is displayed and the user is routed to the employee search page. 
    """
    id = request.args.get("id")
    row = None
    if id is None:
        flash("ID is not there, please enter ID", "danger")
        return redirect(url_for("employee.search"))
    else: # TODO update this for TODO edit-1
        """
            UCID: sp2943
            Date: 28th November 2022
            If request.method=POST is used, data is received from the form using request.form.get.
            If the needed set of values is not present, a flash message is displayed and has error is set to True.
            If the error is FALSE, the employee table is updated using the UPDATE query, and a flash message is displayed.
            If there is a mistake in processing and the update statement is not operating, a flash message is displayed.
        """
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            
            has_error=False
            fn = request.form.get("first_name")
            ln = request.form.get("last_name")
            company_id = request.form.get("company", None) # TODO edit-4 company may be None
            email = request.form.get("email")
            
            # TODO edit-2 first_name is required (flash proper error message)
            if fn=="":
                flash("First name is not there, please enter first name", "danger")
                has_error=True
            
            # TODO edit-3 last_name is required (flash proper error message)
            if ln=="":
                flash("Last name is not there, please enter last name", "danger")
                has_error=True
            
            # TODO edit-5 email is required (flash proper error message)
            if email=="":
                flash("Email is not there, please enter email", "danger")
                has_error=True
            data = [fn, ln, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                """
                    UCID: sp2943
                    Date: 28th November 2022
                    The update query is used to update the data in the workers table.
                    If there is a mistake in the processing, a flash message is displayed.
                """
                if not has_error:
                    result = DB.update("UPDATE IS601_MP2_Employees SET first_name=%s, last_name=%s, company_id=%s, email=%s WHERE id = %s", *data)
                    if result.status:
                        flash("Employee record has been updated successfully", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash("Unfortunately, company' data cannot be updated", "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a company
            """
            UCID: sp2943
            Date: 28th November 2022
            The select query is used to prefill the data depending on the id that was chosen. The IF statement is used to display the firm name; if NULL, then 'N/A' is displayed.
            If there is a problem in query processing, a flash message is displayed.
            """
            result = DB.selectOne("""SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') as company_name 
            from IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON e.company_id=c.id WHERE e.id = %s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Sorry, data cannot be fetched", "danger")
    
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    """
    UCID: sp2943
    Date: 28th November 2022
    Request.args is used to retrieve the ID and create a mutable dictionary 
    """
    id = request.args.get("id")
    # make a mutable dict
    args = {**request.args}
    """
    UCID: sp2943
    Date: 28th November 2022
    If the id is obtained, remove the employee data from the businesses table. If the queries are successful, a flash message will be displayed.
    In the event of a processing fault, a flash message is displayed.
    """
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
            if result.status:
                # TODO delete-4 ensure a flash message shows for successful delete
                flash("Successfully deleted Employee record from Company's DB", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash("Employee data record cannot be deleted", "danger")
        # TODO pass along feedback
        # remove the id args since we don't need it in the list route but we want to persist the other query args
        """
        UCID: sp2943
        Date: 28th November 2022
        Remove id from the args and send the remainder to the EMPLOYEE.search page.
        """
        del args["id"]
    return redirect(url_for("employee.search", **args))