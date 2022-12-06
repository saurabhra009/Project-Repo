<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Satyam Adharchandra Pandey (sp2943)</td></tr>
<tr><td> <em>Generated: </em> 12/4/2022 7:20:24 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/sp2943" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205518711-4713f1bd-42d3-41c2-9e71-a6c1ce9d9b23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-mt85 should be updated to DIAR-ucid of the student (in loayout.html)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205518735-cbfa72d6-7077-42e5-b487-b168405a14a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page&#39;s &quot;Brought to you by...&quot; message should be updated to include student&#39;s<br>firstname, ucid, and IS601 section<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205518764-1b27d242-5a02-4bde-a92a-1826ab8ec1ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Companies table should be visible (empty or not)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205518766-1a904141-2b19-43b5-a5ba-a67603f35bdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Employees table should be visible (empty or not)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205518988-b218307e-830e-4257-85f0-91040a75604a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should check if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519001-221e6b53-99da-427f-b3d5-ebd7f17ae23c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file should be read from the provided stream as a dict +<br>Extracted employee data should be append as a dict to the employee list<br>+ Extracted company data should be appneded as a dict to the comapny<br>list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519028-e56431af-2b69-4566-89df-71005d349704.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After each query a flash message should be generated noting how many records<br>were processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519037-8b4456e2-676d-44cb-9646-7c6e88a485b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If a particular list was empty a flash message should note that the<br>particular list wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519278-9d199c1b-ce2f-46e7-bc49-6db31261fbe3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should show the proper success message + Should show the proper count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519297-50ee0ba8-d11e-436f-8c1a-b4c84210e2f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the error message when the file is not a .csv file +<br>Show the error message when the form was submitted without a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519445-04679745-8d6e-4b72-ba1e-57f0e6312807.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519444-7e493521-2d61-4114-b10e-604dbc746d5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519605-d012a70d-57f1-4dbd-8e95-fa5695d3a7ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve first_name, last_name, company (id), email + first_name is required (flash<br>proper error message) + last_name is required (flash proper error message) + company<br>doesn&#39;t require a flash and may be empty/None + email is required (flash<br>proper error message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519606-80f1a60e-a8c8-48d6-99f2-917a1519fe02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible + Except block should have a user<br>friendly message flashed and a print() of the exception + Captions should properly<br>label/identify screenshots<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519802-35f09a44-c604-4c83-90f6-a331c8b693d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission + Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519829-a48fd87e-8227-4dc5-b18c-f7a2f81a5567.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show first_name error message + Show last_name error message + Show email error<br>message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519884-af94d081-3108-4602-aa0b-e632072f70b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid employee data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519951-4fc7a141-44c8-4708-b4d0-e37faaba1a60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should be filled in properly to pull employ id, first_name, last_name,<br>email, company_id, company_name via a LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519947-50c5fcfd-4f61-4a54-86e6-0879560d456c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for fn, ln, email, company, column, order, limit (exact naming<br>is required) + append like filter for first_name if provided + append like<br>filter for last_name if provided + append like filter for email if provided<br>+ append equality filter for company_id if provided + append sorting if column<br>and order are provided and within the allowed columns and order options (asc,<br>desc) allowed_columns = [&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205519949-66d16a04-8e2e-448f-a18a-77065235f1ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append limit (default 10) or limit greater than 1 and less than or<br>equal to 100 + provide a proper error message if limit isn&#39;t a<br>number or if it&#39;s out of bounds + Except block should have a<br>user friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520137-a935bfc5-7ec7-4705-9ab5-6fd176692424.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520139-6cacfac3-8a36-4d78-b931-aba6ddbbecbc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520136-4b4f402e-70ef-4607-9c5e-371b400f0dfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520135-1feefe6e-9645-473d-b6b9-2514a1647bec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520132-e1837c4d-1422-41e2-82eb-ec3d75689316.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520133-46068ed8-2bd0-4c0c-8703-5ebbc0dac373.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520407-6ba259f7-f676-425b-b8d5-674d176971c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form + company doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520408-6000a3ff-8379-4aba-857b-9b515f2a2ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name is required (flash proper error message) + last_name is required (flash proper<br>error message) + email is required (flash proper error message) + Proper UPDATE<br>query should be visible + Except blocks (two) should have a user friendly<br>message flashed and a print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520410-3c4194f0-a70b-4c5a-aef5-fe9f5a162723.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible + Employee data should be passed to<br>the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520588-207f07f7-ad7f-4823-91a4-3a5f410e4cab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit + Show data after an edit (should be<br>different) + Page should show employee data in both scenarios<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520587-cf21521b-6cd3-4baf-b0c2-d7516ed5f6b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed (First name, Last name, Email and company<br>everything has been updated)  + Data should be clearly visible in both<br>screenshots<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520955-04965ce2-f247-4bfd-bfc1-f4ce5a489cff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code should retrieve form data for name, address, city, state, country, zip, website<br>+ name is required (flash proper error message) + address is required (flash<br>proper error message) + city is required (flash proper error message) + state<br>is required (flash proper error message) + country is required (flash proper error<br>message) + website is not required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520959-54c47732-4c66-40ec-9f0b-8f55c0b0b077.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible + Except block should have a user<br>friendly message flashed and a print() of the exception + <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520967-9c195724-a644-4f63-8291-94eb6f408fa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission + Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520969-fa4349c0-f350-411c-b896-68bf3682cb77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show name error message + Show address error message + Show city error<br>message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520971-d5fffc9d-b37b-464c-9d73-c998ce8e1980.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show state error message + Show country error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205520963-37b32ecc-3724-4ccc-9191-b9c4e7779dc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521286-d1aed946-9911-43e2-a98c-3fdb3c1793c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count for the company (likely a sub-query is needed) + Check request args<br>for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521287-b0051149-4f92-4a0f-941b-d8f553e25086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append a LIKE filter for name if provided + append an equality filter<br>for country if provided + append an equality filter for state if provided<br>+ append sorting if column and order are provided and within the allows<br>columsn and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;] + append<br>limit (default 10) or limit greater than 1 and less than or equal<br>to 100 + provide a proper error message if limit isn&#39;t a number<br>or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521290-ccd942a8-95d5-4e5c-b3ff-f91c1a9f6d40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521471-eb1f1f6b-4d11-46e0-869a-41ec19acc9a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521467-acc2d730-ac85-4782-8f87-d4994f7d2138.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521472-60654f16-bdfe-4253-9655-811d1d97a8fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521463-1a1bdd78-ddad-41e7-b561-90abce52ee77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521465-592025ca-d951-4fc7-8631-5ef866ec108e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521845-fa23adf2-e726-4945-a174-8c1a3cc13643.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521846-831bd2b2-da77-4801-bd24-193d19642a31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name is required (flash proper error message) + address is required (flash proper<br>error message) + city is required (flash proper error message) + state is<br>required (flash proper error message) + country is required (flash proper error message)<br>+ Proper UPDATE query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521847-7f85d274-5da3-41db-b2c9-352c536f6f8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (two) should have a user friendly message flashed and a print()<br>of the exception + Proper SELECT query should be visible + Company data<br>should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521851-4d3e76eb-25db-4dad-b993-2b005f23b118.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit + Show data after an edit (should be<br>different) + Page should show company data in both scenarios<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205521850-77e5500b-b21e-4a37-a320-d04cd4ca06d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed (Name and address of the company has<br>been updated) + Data should be clearly visible in both screenshots<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522361-493c6c2c-1d4d-4f4c-aef5-d42c7fd549d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete employee by id + Redirect to employee search + All request args<br>(minus id) are passed to the redirect route + Success message should be<br>flashed if the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522492-ae3666c3-ca48-4105-920d-b2f5f590aafb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearly label before and after (Before) + Success message should be flashed if<br>the process worked<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522488-b6115cf4-4b8c-4a6d-90e2-721ce8fce21c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearly label before and after (After) + Success message should be flashed if<br>the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522597-e5d99145-e18a-4a7a-a161-5f6dbbd5b85b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete company by id + Redirect to company search + All request args<br>(minus id) are passed to the redirect route + Success message should be<br>flashed if the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522671-eb4261a9-058b-445d-a6d2-a79dfcbe6b02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearly label before and after (Before) + Success message should be flashed if<br>the process worked<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522666-454231aa-214f-46ed-a819-59b352485e27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearly label before and after (After) + Success message should be flashed if<br>the process worked<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522836-f83b328d-7743-4630-b81a-1a10e1b417b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Add company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522839-31502d03-bd54-4867-8af7-d505c1d79b6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Add employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522840-02539f4d-841f-47ac-bc2c-f0014e872f74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Edit company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522843-552f02e9-9efb-43e8-bb1c-0d6c73df018c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Edit employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522844-8142c94d-f18d-4c64-b931-d725c0ee9937.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Company (Filter name, country, state)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522846-32e58583-2ba1-4579-92c2-a2e24fcfac41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Company  Sorting (name asc,dsc), (city asc,dsc), (country asc,dsc)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522847-8607018b-c071-4198-a0d2-5ac7693faff2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Company  Sorting (State asc,dsc)   Employee count<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522849-8299175d-0674-47ca-8060-3a936070e13b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Employee (Filter first name, last name, email, company)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522851-55a72c91-9d69-4ccb-aa37-5df17a339e07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Employee  Sorting (company asc,dsc)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522853-69a91238-cf48-4bac-af2c-beb771d65c12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Search Employee  Sorting (first name asc,dsc), (last name asc,dsc), (email<br>asc,dsc)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/205522854-416f5c68-5380-4668-84be-7f53945063b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - Upload CSV<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>In this assignment, we have studied about the integration of Python, SQL, Jinja,<br>flask and HTML to create a website, where we are uploading data from<br>a CSV and, using it to perform few operations like adding, editing, deleting<br>etc. We have also used flash messages to give a user friendly response<br>to the end user in case of any errors. This has a real<br>world implication and, we use these kind of websites on a day to<br>day basis, so knowing the back-end process  it is extremely useful.&nbsp;<div>In particular,<br>we have used HTML pages to create a layout for our website then,<br>we have used SQL using Oracle DB to storing the data by creating<br>two tables; one  employees and another for company data, moreover we have<br>also used python for our back-end operations and, for showing flash messages.</div><div><br></div><div>Few issues<br>which I have faced while implementing this project is listed below along with<br>the resolution to it,&nbsp;</div><div>- Faced issues in running the test cases due to<br>different column names, later resolved it by keeping the same column names.</div><div>- Faced<br>issues in extracting the data exactly using the left join, later resolved it<br>updating the query. (Syntax error initially)</div><div>- Few minor issues like, Test cases were<br>not getting detected automatically, so added the folder to workspace and configured test<br>cases manually.&nbsp;</div><div>- DB table hasn&#39;t got created by running the DB file, so<br>I ran both the table queries manually to resolve this issue after activating<br>the connection.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/sp2943" target="_blank">Grading</a></td></tr></table>