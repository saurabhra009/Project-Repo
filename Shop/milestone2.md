<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project Sp2943</td></tr>
<tr><td> <em>Student: </em> Satyam Adharchandra Pandey (sp2943)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 2:12:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/sp2943" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208374798-fd9e8eed-f003-440e-9b99-7d632f2aafea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users with admin or shop owner will be able to add products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208374801-93e18e48-f58c-4bb8-8613-dd3aca192f52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of populated Products table clearly showing the columns<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div>WTF Forms is a tool that enables the creation of forms with various<br>fields, including name (a string data type), description (a text area field), category<br>(also a text area field), stock (a numerical data type), unit price (another<br>numerical data type), a picture field, a visibility field, and a submit button.<br>These fields are accompanied by appropriate validators to ensure that the entered data<br>adheres to the specified format for a particular product.</div><div>Upon submission of the form,<br>an If-else block is utilized to generate code for either updating or creating<br>a new product. If the form request includes no id (indicating the creation<br>of a new product), the form data is inserted into the products table<br>using an SQL Insert command. If the insertion is successful, a flash message<br>is displayed indicating the successful insertion of the new record, and the form<br>data is cleared. If the insertion fails, a flash message indicating an error<br>is displayed.</div><div>Form helpers, which are used to simplify the process of constructing HTML<br>files for forms and processing the different fields, are implemented in HTML. These<br>helpers are capable of handling various field types, including form-control and boolean, and<br>utilize Jinja templates to obtain the layout file, header, and input form text.<br>The render field function is utilized to build input fields for all the<br>necessary columns.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/64">https://github.com/sp2943/IS-601-005/pull/64</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/admin/item">https://is601-sp2943-prod2.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375838-1d78e324-ed60-4343-bfd4-2ef4527bd529.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375842-e4c6072c-df97-4505-9e4e-98a165b195f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied<br>(should be more than 1 sample product) - Limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375844-93547c41-1434-4938-bd75-504f5a353c32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied<br>(should be more than 1 sample product) - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375845-40054799-da59-461f-8d24-8575f7c60a69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied<br>(should be more than 1 sample product) - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375833-d8ee87c9-abf4-4e39-98b0-889514102689.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the filter/sort logic from the code - HTML<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208375837-6e102e5c-4494-43f2-8c2c-ba13c8c86e69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>The product search form includes various select fields that allow users to apply<br>filters to their search queries. These filters are applied by adding conditions to<br>the WHERE clause of the SELECT statement used to retrieve products from the<br>database. The form includes fields for filtering by name and category, with the<br>name field allowing for partial matching and the category field requiring an exact<br>match.</div><div>Upon submitting the form with the chosen filters, a select query is executed<br>using the specified conditions in the WHERE clause. This query retrieves a list<br>of products that match the specified filters, and displays the relevant information for<br>each product in a table. The table includes columns for the name, description,<br>category, stock, unit price, and visibility status of each product.</div><div>Users have the option<br>to sort the results in either ascending or descending order based on the<br>price, with a default limit of 10 results per page. This limit can<br>be adjusted as desired. Additionally, there is a reset button provided to clear<br>the current search results and start a new search. This allows users to<br>easily find and view specific products based on their desired criteria.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/65">https://github.com/sp2943/IS-601-005/pull/65</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/shop">https://is601-sp2943-prod2.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208377822-5dabb736-965b-4204-bcad-690a73734afd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>When a customer wants to add an item to their shopping cart, they<br>can do so by navigating to the product page and clicking on the<br>"Add to Cart" button. This will add the item to their cart and<br>update the cart total. The customer can then continue shopping or proceed to<br>the checkout page.</div><div>On the checkout page, the customer will see a summary of<br>the items in their cart, including the name, quantity, and price of each<br>item. The customer can adjust the quantity of an item by using the<br>plus and minus buttons or by manually entering the desired quantity. If the<br>customer wants to remove an item from their cart, they can click on<br>the "delete" button next to the item.</div><div>Once the customer is ready to complete<br>their purchase, they can click on the "Proceed to Payment" button. This will<br>bring them to the payment page, where they can enter their payment information<br>and complete the transaction.</div><div>Overall, the shopping cart feature allows customers to easily add,<br>delete, and update items as they shop, making the online shopping experience more<br>convenient and efficient.</div><div><div>This is a SQL query that is selecting data from a<br>table called "IS601_Products". The query is asking the database to retrieve all rows<br>from the table, and to only return the values in the columns with<br>the names "id", "name", "description", "category", "stock", "unit_price", "visibility", and "image". The "LIMIT<br>25" clause at the end of the query tells the database to only<br>return the first 25 rows of the results.</div><div>The query uses the SELECT statement<br>to specify which columns to return, and the FROM clause to specify which<br>table to retrieve the data from. The LIMIT clause is used to limit<br>the number of rows returned by the query.</div><div>This query will return a result<br>set containing the requested data for the first 25 rows in the "IS601_Products"<br>table. The result set will contain one row for each returned row in<br>the table, and each row will have the values for the specified columns.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/66">https://github.com/sp2943/IS-601-005/pull/66</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/admin/items">https://is601-sp2943-prod2.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208378475-a114f52b-182f-4518-9db6-d361df4d6c41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208378473-7be39c9a-ae87-42c3-b76b-92cfec517a18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208378470-3be495b6-3d63-481b-ace0-82468c2fbd65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page (The admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208378469-7563f29e-1407-479b-8767-465b590f566f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Editing a Product via the Admin Edit Product Page - Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208378460-ac28fe03-406b-4109-b4fa-4b1abb57ee73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Editing a Product via the Admin Edit Product Page - After<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>The form in question is utilized for the purpose of updating an existing<br>product in the products table of a database, as specified by the id<br>provided in the form request. This is achieved through the execution of a<br>SQL Update command, which updates the product in the database with the new<br>data inputted in the form. Upon the successful submission of the form, a<br>flash message is displayed to confirm the update and the form data is<br>cleared. If the query fails for any reason, an error message is displayed<br>instead.</div><div>Upon the completion of this process, the Admin user is redirected back to<br>the Shop page, where they can view the updated product. Additionally, the Admin<br>has the option to further edit the product by clicking on the edit<br>button, which brings up the form with the current data for that product<br>pre-filled. This allows for the easy modification of the product and the subsequent<br>resubmission of the form.</div><div>The implementation of this feature is facilitated by the use<br>of WTF Forms and Jinja templates, which streamline the creation and rendering of<br>the form. To ensure the accuracy and efficiency of the updates made to<br>the products table, various validators and SQL commands are employed. Overall, the form<br>and associated processes enable the Admin to efficiently update or add new products<br>to the database and view the changes on the Shop page.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/67">https://github.com/sp2943/IS-601-005/pull/67</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/admin/item?id=1">https://is601-sp2943-prod2.herokuapp.com/admin/item?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208379844-33b3bb96-82f7-4480-92fe-ee274bb1d192.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208379845-6567ecb8-fcfb-4c97-b635-80a25e5ebfbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the result of the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>The Product Details Page serves as a comprehensive overview of a specific product<br>for users to view. It includes various details such as the product's name,<br>description, category, stock availability, unit price, and image. The page is generated through<br>a process flow that involves retrieving the necessary product data from a database<br>using an SQL Select statement.</div><div>The Select statement specifically targets the product in question<br>by using its unique identifier, the product id, in the WHERE clause. The<br>resulting data is then passed to a Jinja template, which is responsible for<br>rendering the HTML for the Product Details Page. Jinja is a templating engine<br>that allows developers to insert variables and logic into a template file, enabling<br>the creation of dynamic HTML pages.</div><div>In this case, the Jinja template contains placeholder<br>variables for the product's name, description, category, stock, unit price, and picture. These<br>placeholders are replaced with the actual values retrieved from the database when the<br>template is rendered, ensuring that the Product Details Page displays the most up-to-date<br>information about the product. Overall, the process flow for generating the Product Details<br>Page involves retrieving the relevant product data from the database and rendering an<br>HTML template with that data.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/68">https://github.com/sp2943/IS-601-005/pull/68</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/productdetail?id=11">https://is601-sp2943-prod2.herokuapp.com/productdetail?id=11</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208380463-1d5a1f80-de51-471d-afdb-eaacce1176d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208380462-eae9140e-eb2c-4747-bf98-e4df05f35ba3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the error message of adding to cart (i.e., when not logged<br>in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208380459-e5031478-1bae-48c8-b784-31f8a1762105.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <div>In order to implement the functionality for adding items to a cart and<br>updating the cart on website, it is necessary to utilize various methods and<br>techniques. The first step in this process is to retrieve the product ID<br>and quantity of the desired item, which can be achieved through the use<br>of the request.form.get method. The user's ID can be determined through the use<br>of the current_user.get_id() function.</div><div>Once the necessary information has been gathered, it is possible<br>to update the cart with this information. This can be achieved through the<br>use of SQL queries, such as SELECT and INSERT statements. The SELECT query<br>can be used to retrieve the items that are already in the cart,<br>while the INSERT query can be used to add new items to the<br>cart. These queries can be linked to the appropriate tables through the use<br>of a join command, which allows for the appropriate data to be retrieved<br>or added based on the product ID and user ID.</div><div>If any errors occur<br>during this process, such as attempting to set the quantity of an item<br>to a negative value, a flash message can be displayed to alert the<br>user. This helps to ensure that the cart remains accurate and up-to-date, and<br>that the user is aware of any issues that may arise. Additionally, if<br>the quantity of an item is set to 0, it can be deleted<br>from the cart to keep the cart organized and efficient. Overall, the process<br>of adding items to a cart and updating the cart on a website<br>involves the use of various methods and techniques to ensure the accuracy and<br>efficiency of the cart.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>To facilitate the process of adding items to a shopping cart, a "Add<br>to Cart" button is implemented on the product page. Upon clicking this button,<br>an HTTP POST request is sent to the server. Alternatively, users can also<br>add items to their cart directly from the shop page by utilizing an<br>INSERT query to insert the relevant information, such as the product ID, quantity,<br>unit price, and user ID, into the cart.</div><div>In order to update the cart<br>in the database, a new row is added to the cart_items table, containing<br>the product_id, quantity, and price of the item being added. The total cost<br>of the cart is calculated by multiplying the quantity and price of each<br>item in the cart and summing them up.</div><div>If any errors occur during this<br>process, a flash message is displayed to the user to alert them. The<br>cart also displays the current number of items in it and the total<br>value of the items.</div><div>Overall, the process of adding items to the cart involves<br>the creation of a form, validation and insertion of the form data into<br>the database, and updating of the cart in the database with the added<br>items. This process is facilitated through the use of various libraries and frameworks<br>such as WTF Forms, Jinja, and SQL commands.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/69">https://github.com/sp2943/IS-601-005/pull/69</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208381568-ab988b2f-f347-4d3e-9dcf-a94cd8fa1a07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div>Upon the addition of a product to a user's cart, the relevant information,<br>such as the product name, quantity, and price, is stored in the cart<br>database. This database utilizes a namespace, or a logical grouping of related variables,<br>to calculate the total value of the items in the cart. The subtotal<br>for each product is determined by multiplying the quantity of the product by<br>its price.</div><div>The Jinja template code is then utilized to display the contents of<br>the cart on the website. This code iterates through the rows in the<br>cart table, retrieving the relevant information for each product and displaying it in<br>a table format. This allows the user to easily view the products in<br>their cart, as well as the corresponding quantities and prices. Overall, the integration<br>of the cart database and Jinja template code allows for the efficient and<br>user-friendly management and display of products in a user's cart.</div><div><div>The subtotal for each<br>product in the cart is determined by multiplying the unit price of the<br>product by the quantity of the product. This value is then stored in<br>a variable and added to a running total, which represents the overall subtotal<br>for the entire cart. This process is implemented using a for loop that<br>iterates through the session dictionary, which contains the necessary information about each product<br>in the cart.</div><div>After the subtotal and total for the cart have been calculated,<br>they are displayed on the website using Jinja template code. This code utilizes<br>a for loop to iterate through the session dictionary and display the subtotal<br>and total for each product in the cart. The subtotal and total are<br>displayed in a table format, with the subtotal and total for each product<br>in separate cells.</div><div>Finally, the user has the option to proceed to the checkout<br>page by clicking on the checkout button. This will take the user to<br>a page where they can enter their shipping and payment information and complete<br>their purchase. The checkout process is facilitated by the use of secure servers<br>and encrypted data transmission to ensure the safety and privacy of the user's<br>personal and financial information.</div></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/70">https://github.com/sp2943/IS-601-005/pull/70</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/cart">https://is601-sp2943-prod2.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208382460-3ae90448-b973-4040-9b92-fc6d10b02d38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show a before and after screenshot of Cart Quantity update - Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208382458-68251182-2415-4983-83dd-f81bfbc62288.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show a before and after screenshot of Cart Quantity update - After<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208382463-bb1e9ada-5d13-4a28-975a-405dc35dbd95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show a before and after screenshot of setting Cart Quantity to 0 -<br>Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208382461-5a242a78-cdf4-4312-885f-8ab96532942e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show a before and after screenshot of setting Cart Quantity to 0 -<br>After<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208382464-ba377cf5-24b2-4bf9-81b1-01e9ff13361b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show how a negative quantity is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>To update a product in the database, a form request must be submitted<br>that includes the unique identification of the product to be updated, also known<br>as the id. This id is used to locate the relevant entry in<br>the products table. If the form request includes a stock value of 0,<br>the product is deleted from the table using the DELETE command in Structured<br>Query Language (SQL). A message is displayed to the user to confirm that<br>the product has been removed from the cart.</div><div>If a user attempts to submit<br>a form with a negative quantity for the stock of a product, the<br>form's validators will intercept this error and prevent the form from being submitted.<br>A message will be displayed to inform the user that they must enter<br>a positive quantity. If the form has already been submitted and the product<br>is already in the products table, the code will need to handle the<br>scenario in which the user decides to change the stock quantity to a<br>negative number. In this case, an If-else block is used to check the<br>new quantity. If it is negative, a message is displayed to inform the<br>user that they cannot enter a negative quantity and the stock quantity is<br>not updated.</div><div>However, if the new quantity is positive, the code will utilize an<br>SQL Update command to update the stock quantity in the products table. If<br>the query is successful and the stock quantity is updated, a message is<br>displayed to confirm the update. In the event that the query fails, a<br>message is displayed to inform the user of the error.</div><div>Overall, the process flow<br>for handling negative quantities in WTF Forms includes the implementation of validators to<br>prevent negative quantities from being submitted, as well as an If-else block and<br>SQL Update command to handle updating the stock quantity in the products table<br>if a negative quantity is entered. This ensures that only positive quantities are<br>allowed and accurately reflected in the products table.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/71">https://github.com/sp2943/IS-601-005/pull/71</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208384179-8edec8e2-6fdc-4cc1-8cea-e164792879f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of deleting a single item from the Cart - Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208384178-76a955c8-55eb-40cf-b482-2deefd6bf6ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of deleting a single item from the Cart - Before<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208384177-4544b243-b509-41b0-b3a9-dbc0cb99aacd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of clearing the cart - Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/208384174-69d99f4c-b7eb-4e2a-8806-b18b11827cd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of clearing the cart - After<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>The process of deleting a single item from the cart begins with the<br>user initiating the action by clicking on the "Delete" button associated with the<br>item they wish to remove. This generates a request to the server to<br>delete the item from the cart.</div><div>Upon receipt of the request, the server will<br>retrieve the item from the cart data structure and delete it. The server<br>will then send a response back to the user, indicating that the item<br>has been successfully removed from the cart.</div><div>The cart data structure will be updated<br>to reflect the removal of the item, and the total cost of the<br>items remaining in the cart will be recalculated. If the user's cart is<br>now empty, it means that the item deleted was the only item in<br>the cart. If there are items remaining in the cart, the user can<br>continue shopping or proceed to checkout to complete their purchase.</div><div>It is important to<br>note that the process of deleting an item from the cart involves the<br>interaction between the user and the server, with the server handling the manipulation<br>of the cart data structure and the transmission of relevant information back to<br>the user.</div><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/72">https://github.com/sp2943/IS-601-005/pull/72</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>During the completion of this milestone, we encountered several issues that required resolution.<br>One of the primary issues pertained to the validation of form data. It<br>was imperative that the data input into the form was in the correct<br>format and met specific requirements, such as the name field being a string<br>and the stock field being a number. To address this issue, we implemented<br>various validators to verify the data entered by the user.</div><div>Additionally, we encountered issues<br>with the submission of the form. On occasion, the form would not submit<br>properly, leading to errors in the database. To fix this issue, we had<br>to debug the code and determine the root cause, which was often attributed<br>to incorrect data input or missing fields.</div><div>Despite these challenges, we gained valuable insights<br>and knowledge during this milestone. We learned about the significance of form validation<br>and how to effectively implement it. We also developed a stronger understanding of<br>how to troubleshoot issues with form submission and debug code to identify the<br>root cause of problems.</div><div>In conclusion, this milestone allowed us to expand our knowledge<br>of forms and their role in collecting and processing data in a web<br>application. Through our efforts, we were able to create a functional form that<br>can be utilized to add and update products in a database.</div><gwmw style="display:none;"></gwmw><gwmw style="display:none;"></gwmw><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod2.herokuapp.com/login">https://is601-sp2943-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/sp2943" target="_blank">Grading</a></td></tr></table>