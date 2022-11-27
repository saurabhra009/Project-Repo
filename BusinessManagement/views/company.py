from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = """SELECT id, name, address, city, country, state,zip, website, (SELECT count(id) FROM IS601_MP2_Employees WHERE c.id=company_id GROUP BY company_id)
        as employees from IS601_MP2_Companies as c WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name like %s"
        args.append(f'%{name}%')
        
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %s"
        args.append(f'{country}')
        
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %s"
        args.append(f'{state}')
        
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        if column in ["name","city","country","state"] \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
            
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
        # technically this should follow the same rules as col/order
        # but it seems to work with the placeholder mapping with
        # this connector
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    #print("query",query)
    #print("args", args)
    try:
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        # TODO search-9 make message user friendly
        flash("Sorry, data is not available", "danger")
        
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", resp=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-6 country is required (flash proper error message)
        # TODO add-7 website is not required
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zip")
        website = request.form.get("website", None)
        if name=="":
            flash("Please enter Company's name", "danger")
            return redirect(url_for("company.add"))
        if address=="":
            flash("Please enter Company's address", "danger")
            return redirect(url_for("company.add"))
        if city=="":
            flash("Please enter City", "danger")
            return redirect(url_for("company.add"))
        if state=="":
            flash("Please enter State", "danger")
            return redirect(url_for("company.add"))
        if country=="":
            flash("Please enter Country", "danger")
            return redirect(url_for("company.add"))
        has_error = False # use this to control whether or not an insert occurs
        if not has_error:
            try:
                result = DB.insertOne("""INSERT INTO IS601_MP2_Companies (name, address,city,state,country,zip,website)
                VALUES(%s, %s, %s, %s, %s, %s, %s)"""
                ,name, address,city,state,country,zipcode,website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Company Record has been successfully createdy", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Sorry, Company's data cannot be added", "danger")       
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    row = None
    if id is None:
        flash("Please enter ID", "danger")
        return redirect(url_for("company.search"))
    else: # TODO update this for TODO edit-1

        #if request.method == "POST" and request.form.get("name") and request.form.get("address") and request.form.get("city") and \
            #request.form.get("state") and request.form.get("country"):
        if request.method == "POST":  
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-8 website is not required 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            #data = [name, address, city, state, country, zipcode, website]
            has_error=False
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip",None)
            website = request.form.get("website",None)
            print("Name",name)
            if name=="":
                flash("Company' name cannot be empty", "danger")
                has_error=True
            if address=="":
                flash("Address cannot be empty", "danger")
                has_error=True
            if city=="":
                flash("City's name cannot be empty", "danger")
                has_error=True
            if state=="":
                flash("State cannot be empty", "danger")
                has_error=True
            if country=="":
                flash("Country's name cannot be empty'", "danger")
                has_error=True
            
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            try:
                # TODO edit-9 fill in proper update query
                if not has_error:
                    result = DB.update("UPDATE IS601_MP2_Companies SET name=%s, address=%s, city=%s, state=%s, country=%s, zip=%s, website= %s WHERE id = %s", *data)
                    if result.status:
                        flash("Successfully updated Company's record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash("Sorry, Company's data cannot be updated", "danger")
                
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Company's data cannot be fetched", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    # make a mutable dict
    args = {**request.args}
    if id:
        try:
            query=DB.selectAll("SELECT company_id FROM IS601_MP2_Employees")
            if query.status: 
                rows=query.rows
            companyid_values=[]
            for row in rows:
                if row['company_id'] is not None:
                    companyid_values.append(int(row['company_id']))
            print(companyid_values)
            print(id)
            if int(id) in companyid_values:
                result_employee=DB.update("UPDATE IS601_MP2_Employees SET company_id=NULL WHERE company_id= %s",id) 
                #Delete company by id
                result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
                if result.status and result_employee.status:
                    flash("Deleted record from Company's DB successfully", "success") 
                    #Success message should be flashed if the process worked
            else:
                result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
                if result.status:
                    flash("Sorry, data cannot be deleted from Company's DB", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash("Data cannot be deleted", "danger")
            
        # TODO pass along feedback
        # remove the id args since we don't need it in the list route
        # but we want to persist the other query args
        del args["id"]
    return redirect(url_for("company.search", **args)) 
    #Redirect to company search 
    #All request args (minus id) are passed to the redirect route
