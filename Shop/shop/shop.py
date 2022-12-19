import traceback
from flask import Blueprint, request, flash, render_template, redirect, url_for,session
from werkzeug.datastructures import MultiDict
from shop.forms import ItemForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
from shop.forms import PaymentForm
from auth.models import User
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

# Deliverable 1: Users with admin or shop owner will be able to add products

@shop.route("/admin/item", methods=["GET","POST"]) #SP2943 December 15, 2022
@admin_permission.require(http_exception=403) 
def item():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    
    # Deliverable 4: Admin/Shop Owner Edit button
    
    type = "Edit" if id else "Create"
    if form.validate_on_submit():
        if form.id.data: # it's an update
            try:
                result = DB.update("UPDATE IS601_Products set name = %s, description = %s, category=%s, stock = %s, unit_price = %s, image=%s, visibility= %s WHERE id = %s",
                form.name.data, form.description.data,form.category.data,form.stock.data, form.unit_price.data, form.image.data,form.visibility.data,form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_Products (name, description, category, stock, unit_price, image, visibility) 
                VALUES (%s,%s,%s,%s,%s,%s, %s)""",
                form.name.data, form.description.data, form.category.data, form.stock.data, form.unit_price.data, form.image.data,form.visibility.data)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, stock, unit_price, image, visibility FROM IS601_Products WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
            traceback.print_exc()
    return render_template("item.html", form=form, type=type)

@shop.route("/admin/items/delete", methods=["GET"]) #SP2943 December 15, 2022
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Products WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item",e)
            flash("Error deleting item", "danger")
    return redirect(url_for("shop.items"))


# Deliverable 3: Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status)

@shop.route("/admin/items", methods=["GET","POST"]) #SP2943 December 15, 2022
@admin_permission.require(http_exception=403)
def items():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, category, stock, unit_price,visibility, image FROM IS601_Products LIMIT 25",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("items.html", rows=rows)


# Deliverable 2: Any user can see visible products on the Shop Page

@shop.route("/shop", methods=["GET","POST"]) #SP2943 December 15, 2022
def shop_list():
    name = request.args.get("name")
    category = request.args.get("category")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    args=[]
    query = "SELECT id, name, description, category, stock, unit_price, image,visibility FROM IS601_Products WHERE stock > 0 AND visibility=true"
    if name:
        query += " AND name like %s"
        args.append(f"%{name}%")
    if category:
        query += " AND category = %s"
        args.append(f"{category}")
    if order in ["asc", "desc"]:
        query += f" ORDER BY unit_price {order}"
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    rows = []
    try:
        print(query)
        print(args)
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    
    return render_template("shop.html", rows=rows)


# Deliverable 5: Product Details Page 

@shop.route("/productdetail", methods=["GET","POST"]) #SP2943 December 15, 2022
def productdetail():
    product_id = request.args.get("id")
    print("id", product_id)
    rows = []
    try:
        result = DB.selectOne("""SELECT id,name,description, category, unit_price, image
        FROM IS601_Products WHERE id = %s
        """, product_id)
        if result:
            print("Yes")
            row = result.row
            print(row)
    except Exception as e:
        print("Error getting details about the product", e)
        flash("Error fetching product details", "danger")
    return render_template("productdetail.html", rows=row)


# Deliverable 6: Add to Cart

@shop.route("/cart", methods=["GET","POST"]) #SP2943 December 15, 2022
@login_required
def cart():
    product_id = request.form.get("product_id")
    id = request.form.get("id", product_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            
            # Deliverable 7: User will be able to see their Cart
            
            try:
                result = DB.selectOne("SELECT id,unit_price,name from IS601_Products WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    unit_price = result.row["unit_price"]
                    name = result.row["name"]
                    if product_id: # update from cart
                        
                        # Deliverable 8: User can update cart quantity 
                        
                        result = DB.insertOne("""
                        UPDATE IS601_Cart SET
                        quantity = %(quantity)s,
                        unit_price = %(unit_price)s
                        WHERE product_id = %(id)s and user_id = %(user_id)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "unit_price":unit_price,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Updated quantity for {name} to {quantity}", "success")
                    else: #add from shop
                        result = DB.insertOne("""
                        INSERT INTO IS601_Cart (product_id, quantity, unit_price, user_id)
                        VALUES(%(id)s, %(quantity)s, %(unit_price)s, %(user_id)s)
                        ON DUPLICATE KEY UPDATE
                        quantity = quantity + %(quantity)s,
                        unit_price = %(unit_price)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "unit_price":unit_price,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete
            if quantity<0:
                flash("Quantity cannot be less than 0","danger")
            try:
                result = DB.delete("DELETE FROM IS601_Cart where product_id = %s and user_id = %s", id, user_id) #Deliverable 9: Cart Item Removal 
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_Cart c JOIN IS601_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)

@shop.route("/clearcart", methods=["GET","POST"]) #SP2943 December 15, 2022

# Deliverable 9: Cart Item Removal 

def clear_cart():
    try:
        result = DB.delete("DELETE FROM IS601_Cart")
        print("Yes")
        if result.status:
            print("No")
            flash("Records deleted successfully","success")
    except Exception as e:
            print("Error deleting items", e)
            flash("Error deleting items from cart", "danger")
    return render_template("cart.html")

@shop.route("/proceed_to_checkout", methods=["GET","POST"]) #SP2943 December 15, 2022
def proceed_to_checkout():
    
# Deliverable 1: Orders will be able to be recorded

    cart = []
    total = 0
    quantity = 0
    order = {}
    # get cart to verify
    result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, i.stock, c.unit_price as cart_unit_price, i.unit_price as item_unit_price, (c.quantity * c.unit_price) as subtotal 
    FROM IS601_Cart c JOIN IS601_Products i on c.product_id = i.id
    WHERE c.user_id = %s
    """, current_user.get_id())
    if result.status and result.rows:
        cart = result.rows
    # verify cart
    has_error = False
    for item in cart:
        if item["quantity"] > item["stock"]:
            flash(f"Item {item['name']} doesn't have enough stock left", "warning")
            has_error = True
        if item["cart_unit_price"] != item["item_unit_price"]:
            value_change=round(((item["item_unit_price"]-item["cart_unit_price"])/item["cart_unit_price"])*100,2)
            new_value=item["item_unit_price"]
            flash(f"Item {item['name']}'s price has changed to {new_value} by {value_change}% , please refresh cart. ", "warning")
            has_error = True
        total += int(item["subtotal"] or 0)
        quantity += int(item["quantity"])
    if request.method == "POST":
        has_error=False
        username = request.form.get("username")
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        address = request.form.get("address")
        apartment = request.form.get("apartment")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zipcode")
        payment_method=request.form.get("payment_method")
        money_received=request.form.get("money_received")


        if username=="":
            flash("Username is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if email=="":
            flash("Email is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if firstname=="":
            flash("First Name is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if lastname=="":
            flash("Last Name is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if address=="":
            flash("Address is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if city=="":
            flash("City is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if state=="":
            flash("State is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if country=="":
            flash("Country is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if zipcode=="":
            flash("Zipcode is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if payment_method=="":
            flash("Payment Method is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        if money_received=="":
            flash("Value for money to be paid is missing", "danger")
            return redirect(url_for('shop.proceed_to_checkout'))
        
        try:
            DB.getDB().autocommit = False # make a transaction
            
            # create order data
            order_id = 1
            if not has_error:
                value=address+" , "+apartment+" , "+city+" , "+state+" , "+country+" , "+zipcode
                print(value)
                result = DB.insertOne("INSERT INTO IS601_Orders (total_price,number_of_items,address, user_id,first_name,last_name,payment_method,money_received) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)", total, quantity,value, current_user.get_id(),firstname,lastname,payment_method,money_received)
                if not result.status:
                    flash("Error generating order", "danger")
                    DB.getDB().rollback()
                    has_error = True
                elif int(money_received)!=int(total):
                    flash("Please enter the correct amount","danger")
                    DB.getDB().rollback()
                    has_error = True
                else:
                    order_id = int(DB.db.fetch_eof_status()["insert_id"])
                    order["order_id"] = order_id
                    order["total"] = total
                    order["quantity"] = quantity
                    print (order)
            # record order history
            if order_id > -1 and not has_error:
                # Note: Not really an insert 1, it'll copy data from Table B into Table A
                result = DB.insertOne("INSERT INTO IS601_OrderItems (quantity, unit_price, order_id, product_id, user_id) SELECT quantity, unit_price, %s, product_id, user_id FROM IS601_Cart c WHERE c.user_id = %s",
                order_id, current_user.get_id())
                if not result.status:
                    flash("Error recording order history", "danger")
                    has_error = True
                    DB.getDB().rollback()
            # update stock based on cart data
            if not has_error:
                result = DB.update("UPDATE IS601_Products set stock = stock - (select IFNULL(quantity, 0) FROM IS601_Cart WHERE product_id = IS601_Products.id and user_id = %(uid)s) WHERE id in (SELECT product_id from IS601_Cart where user_id = %(uid)s)", {"uid":current_user.get_id()} )
                if not result.status:
                    flash("Error updating stock", "danger")
                    has_error = True
                    DB.getDB().rollback()
            # empty the cart
            if not has_error:
                result = DB.delete("DELETE FROM IS601_Cart WHERE user_id = %s", current_user.get_id())
            if not has_error:
                details = f"Spent {total} on {quantity}" # TBD
                #current_user.account.remove_points(-total, reason="purchase", details=details)
                DB.getDB().commit()
                flash("Purchase successful!", "success")
                return redirect(url_for("shop.purchase",id=order_id))
            else:
                return redirect(url_for("shop.cart"))
        except Exception as e:
            print("Transaction exception", e)
            flash("Something went wrong", "danger")
            traceback.print_exc()
    try:
        result = DB.selectOne("""SELECT username,email FROM IS601_Users WHERE id = %s""", current_user.get_id())
        if result.status:
            row = result.row
    except Exception as e:
        # TODO edit-9 make this user-friendly
        flash("Data cannot be fetched", "danger")
    return render_template("proceed_to_checkout.html",row=row)


@shop.route("/purchase", methods=["GET","POST"]) #SP2943 December 15, 2022
@login_required
def purchase():
    orderid = request.args.get("id")
    cart=[]
    order={}
    shipping=[]
    try:
        result = DB.selectOne("""SELECT id as order_id, total_price as total, number_of_items as quantity,payment_method,address FROM IS601_Orders WHERE id=%s""", orderid)
        if result.status and result.row:
            order = result.row
        itemresult= DB.selectAll("""SELECT name, oi.quantity as quantity, (oi.quantity*oi.unit_price) as subtotal FROM IS601_Products p JOIN IS601_OrderItems oi ON 
        oi.product_id=p.id WHERE oi.order_id=%s""",orderid)
        print(itemresult.status)
        if itemresult.status and itemresult.rows:
            print("Itemrow true")
            cart=itemresult.rows
    except:
        flash("Something went wrong","danger")
        traceback.print_exc()
    return render_template("order_summary.html", rows=cart, order=order)

@shop.route("/orders", methods=["GET"]) #SP2943 December 15, 2022
@login_required
def orders():
    
# Deliverable 1: Orders will be able to be recorded

    rows = [] 
    try:
        if current_user.has_role("Admin"):
            result = DB.selectAll("""
            SELECT user_id,u.username,o.id, total_price, number_of_items,o.created FROM IS601_Orders o JOIN IS601_Users u ON o.user_id=u.id ORDER BY id DESC
            """)
        else:
            result = DB.selectAll("""
            SELECT id,total_price, number_of_items,created FROM IS601_Orders WHERE user_id = %s ORDER BY id DESC LIMIT 10 
            """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            print(rows[0])
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
        traceback.print_exc()
    return render_template("orders.html", rows=rows)

@shop.route("/order", methods=["GET"]) #SP2943 December 15, 2022
@login_required
def order():
    
# Deliverable 1: Orders will be able to be recorded

    rows = []
    total = 0
    ship=[]
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        if current_user.has_role("Admin"):
            # locking query to order_id and user_id so the user can see only their orders
            result = DB.selectAll("""
            SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal FROM IS601_OrderItems oi JOIN IS601_Products i on oi.product_id = i.id WHERE order_id = %s
            """, id)
        else:
            result = DB.selectAll("""
            SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal FROM IS601_OrderItems oi JOIN IS601_Products i on oi.product_id = i.id WHERE order_id = %s ANd user_id = %s
            """, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
        shipresult=DB.selectOne("""SELECT address, payment_method FROM IS601_Orders WHERE id=%s""",id)
        if shipresult.status and shipresult.row:
            ship=shipresult.row
            ship["id"]=id
            print(rows)
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
    return render_template("order.html", rows=rows, total=total,ship=ship)

