from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    """
    UCID: sp2943
    Date: 28th November 2022
    Subquery is built to collect count of id from the workers database matching the two tables 
    based on the id and grouping by business id.
    """
    query = """SELECT id, name, address, city, country, state,zip, website, (SELECT count(id) FROM IS601_MP2_Employees 
    WHERE c.id=company_id GROUP BY company_id) as employees from IS601_MP2_Companies as c WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    """
    UCID: sp2943
    Date: 28th November 2022
    ORDER BY is used to sort the list of firm data depending on the column and order specified. request.args is used to get the 
    relevant data, and then appropriate adjustments are made to query to filter according to the name, nation, state" Limit is 
    also introduced to display the list of firms.
    """
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
    if limit and int(limit) > 0 and int(limit) <= 100:
        # technically this should follow the same rules as col/order
        # but it seems to work with the placeholder mapping with this connector
        
        query += " LIMIT %s"
        args.append(int(limit))
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
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
        
        # TODO search-9 make message user friendly
        """
        UCID: sp2943
        Date: 28th November 2022
        In the event that the data is not accessible for selection, a user-friendly flash message is displayed.
        """
        flash("Unfortunately, data is not available", "danger")
    
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", resp=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zip")
        website = request.form.get("website", None) # TODO add-7 website is not required
        """
        UCID: sp2943
        Date: 28th November 2022
        Request.form.get is used to obtain the needed set of data from the form.
        If the needed set of values is lacking, a flash message is displayed and the user is routed to the add page.
        """
        # TODO add-2 name is required (flash proper error message)
        if name=="":
            flash("Company's name is not there, please enter Company's name", "danger")
            return redirect(url_for("company.add"))
        
        # TODO add-3 address is required (flash proper error message)
        if address=="":
            flash("Address is not there, please enter Address", "danger")
            return redirect(url_for("company.add"))
        
        # TODO add-4 city is required (flash proper error message)
        if city=="":
            flash("City is not there, please enter City", "danger")
            return redirect(url_for("company.add"))
        
        # TODO add-6 country is required (flash proper error message)
        if country=="":
            flash("Country is not there, please enter Country", "danger")
            return redirect(url_for("company.add"))
        
        # TODO add-5 state is required (flash proper error message)
        if state=="":
            flash("State is not there, please enter State", "danger")
            return redirect(url_for("company.add"))
        
        has_error = False # use this to control whether or not an insert occurs
        
        """
        UCID: sp2943
        Date: 28th November 2022
        If the has error flag check returns FALSE, insert data into the businesses database and display a successful insertion flash message.
        """
        if not has_error:
            try:
                result = DB.insertOne("""INSERT INTO IS601_MP2_Companies (name, address,city,state,country,zip,website)
                VALUES(%s, %s, %s, %s, %s, %s, %s)"""
                ,name, address,city,state,country,zipcode,website) # <-- # TODO add-8 add query and add arguments
                if result.status:
                    flash("Company record has been created successfully", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                """
                UCID: sp2943
                Date: 28th November 2022
                A user-friendly flash message has been added. If no company data is entered, there is a processing issue.
                """
                flash("Unfortunately, company data cannot be added, there is some error", "danger")       
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    """
    UCID: sp2943
    Date: 28th November 2022
    Request.args is used to retrieve the ID, and if there is none, a flash message is displayed and the user is sent to the company search page.
    """
    id = request.args.get("id")
    row = None
    if id is None:
        flash("ID is not there, please enter ID", "danger")
        return redirect(url_for("company.search"))
    else: # TODO update this for TODO edit-1
        """
            UCID: sp2943
            Date: 28th November 2022
            If request.method=POST is being used, data is received from the form using request.form.get.
            If the needed set of values is not present, a flash message is displayed and has error is set to True.
            If the error is FALSE, the company table is updated using the UPDATE query, and a flash message is displayed.
            If there is a mistake in processing and the update statement is not operating, a flash message is displayed.
        """
        if request.method == "POST":  
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            #data = [name, address, city, state, country, zipcode, website]
            
            has_error=False
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip",None)
            website = request.form.get("website",None) # TODO edit-8 website is not required 
            
            # TODO edit-3 name is required (flash proper error message)
            if name=="":
                flash("Company's name is not there, please enter Company's name", "danger")
                has_error=True
                
            # TODO edit-4 address is required (flash proper error message)
            if address=="":
                flash("Address is not there, please enter Address", "danger")
                has_error=True
                
            # TODO edit-5 city is required (flash proper error message)
            if city=="":
                flash("City is not there, please enter City", "danger")
                has_error=True
            
            # TODO edit-6 state is required (flash proper error message)
            if state=="":
                flash("State is not there, please enter State", "danger")
                has_error=True
            
            # TODO edit-7 country is required (flash proper error message)
            if country=="":
                flash("Country is not there, please enter Country", "danger")
                has_error=True
            
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            try:
                # TODO edit-9 fill in proper update query
                """
                    UCID: sp2943
                    Date: 28th November 2022
                    The update query is used to update the data in the businesses table.
                """
                if not has_error:
                    result = DB.update("UPDATE IS601_MP2_Companies SET name=%s, address=%s, city=%s, state=%s, country=%s, zip=%s, website= %s WHERE id = %s", *data)
                    if result.status:
                        flash("Company record has been updated successfully", "success")
                        
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash("Unfortunately, company' data cannot be updated", "danger")
        try:
            """
            UCID: sp2943
            Date: 28th November 2022
            The choose query is used to prefill the data based on the specified id, and if there is a problem in query processing, 
            a flash message is presented.
            """
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP2_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Sorry, data cannot be fetched", "danger")
    
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    """
    Request.args is used to retrieve the ID and create a mutable dictionary.
    """
    id = request.args.get("id")
    # make a mutable dict
    args = {**request.args}
    """
    If id is retrieved, SELECT all company ids from the Employees database and add all company ids from the table to a list.
    If the id retrieved exists in the company id values, change the company id to None for those workers in the employee database and remove the company data from the businesses table.
    If the queries are successful, a flash message will be displayed. If the id does not exist in the company id values, remove the company record from the companies database.
    In the event of a processing error, a flash message is displayed.
    """
    if id:
        try:
            query=DB.selectAll("SELECT company_id FROM IS601_MP2_Employees")
            if query.status: 
                rows=query.rows
            companyid_values=[]
            for row in rows:
                if row['company_id'] is not None:
                    companyid_values.append(int(row['company_id']))
                    
            # TODO delete-1 delete company by id (unallocate any employees)
            # TODO delete-2 redirect to company search
            # TODO delete-3 pass all argument except id to this route
            if int(id) in companyid_values:
                result_employee=DB.update("UPDATE IS601_MP2_Employees SET company_id=NULL WHERE company_id= %s",id)
                result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
                if result.status and result_employee.status:
                    # TODO delete-4 ensure a flash message shows for successful delete
                    flash("Successfully deleted company record from Company's DB", "success")
            else:
                result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id = %s", id)
                if result.status:
                    flash("Successfully deleted Company record from Company's DB", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash("Company data record cannot be deleted", "danger")
        # TODO pass along feedback
        # remove the id args since we don't need it in the list route but we want to persist the other query args
        """
        Remove id from the args and give the rest to the firm. page of search.
        """
        del args["id"]
    return redirect(url_for("company.search", **args))
    