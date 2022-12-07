<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Satyam Adharchandra Pandey (sp2943)</td></tr>
<tr><td> <em>Generated: </em> 12/6/2022 7:01:14 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/sp2943" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045820-56138ed9-1d0e-4ec8-8e59-66d843385c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045821-7db0dc49-3618-4b5d-8d69-81e2489f9887.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045822-aed27ec6-47ab-44b6-b3e9-48f935e4abbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045818-3086aa25-efb7-4a03-964e-de59d8f91c10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045825-dc6b8ae4-dcdd-44c5-83c4-25ed561a468e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045824-fc6a10d3-7ee4-4dd7-9a7a-8a34e0d69c13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206045827-9e9096f5-95bc-4560-a432-bf9232053f4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 should be present in this screenshot.<br>Clearly highlight which row it is.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Explains how the form is handled and behaves<div>We generated a template for<br>form layouts and registered using RegistrationForm.py. To obtain the needed data, we employed<br>a number of validators. We developed a database in our locally for validations,<br>which we utilize to check the data from the registration form and provide<br>login access. We ask the user to input their username, email address, password,<br>and confirmation password, and then they may submit these credentials to create a<br>new user. We display a &#39;Successful creation&#39; message after successful creation.</div><div><br></div><div>2.&nbsp;Explains the validation<br>logic (front-end and back-end)</div><div><div>To obtain the necessary information from the user, we employed<br>a number of validators in our form. If a user has a one-character<br>password, the system will throw an error. Similarly, we employed additional validators.</div><div>When a<br>user enters data that is not the required one, we display a notice<br>that is intelligible by a normal human on the front end. For the<br>front end, we used flash messages. In the back-end, we used validators that<br>we had already established for our convenience. For example, the user cannot leave<br>any box empty since we have set an &#39;InputRequired&#39; validator, which would prompt<br>a flash message if no data is present, and input for password registration<br>should be between (2,30) characters.</div></div><div><br></div><div>3.&nbsp;Explains how the password is handled</div><div>We employed validators to<br>handle our passwords, and we also require the user to input the password<br>twice to eliminate the possibility of error. First, we utilized the &#39;InputRequired&#39; validator<br>so that the user could not leave it empty. Second, it must be<br>inside our set range of characters; if it is outside of that range,<br>an error notice will be displayed. Finally, we are requesting the user to<br>input the password twice, so if the user enters the incorrect password the<br>second time, an error notice will be displayed. So we handle passwords in<br>this manner.<br></div><div><br></div><div>4.&nbsp;Explains how the DB is utilized</div><div>We are storing all of the registered<br>information in our database. We are essentially utilizing four databases, and all registered<br>user data is stored in the &#39;Users&#39; database, where the author can view<br>the user&#39;s email, id, hashed passwords, generated date, edited timestamp, and username. This<br>information will be used later for login validation.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206046892-5d92a44c-8d10-45ff-9c80-5ab89a13b1dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206046894-ab8d8bf8-fdf3-43f3-af09-6a60bb0a8a2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206046889-cd1fc14d-2ad8-4132-aa16-9992e012690c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1.&nbsp;Explains how the form is handled and behaves</div><div>We made a template for form<br>layouts and used LoginForm.py to log in. To obtain the needed data, we<br>employed a number of validators. We developed a database in our locally for<br>validations where we store the registered data and use it for comparison to<br>validate the data from the registration form and provide login access. We are<br>requesting the user to input their username or email address and password, and<br>then they may submit these data to log in. After a successful login,<br>we display a 'Successful login' message and the user may view further information.<br></div><div><br></div><div>2.&nbsp;Explains<br>the validation logic (front-end and back-end)</div><div><div>We already have the data from the signup<br>page in our database, which we use as a validator for login.</div><div>If the<br>data does not match, we display an error message with the appropriate message<br>that the user may readily understand. In the back-end, we simply compare the<br>entered data with the data recorded in our database during the registration process.</div></div><div><br></div><div>3.&nbsp;Explains<br>how the password is handled</div><div>We have employed validators to handle our passwords; essentially,<br>we are using the data supplied during the registration process as a validator.<br>We also used the 'InputRequired' validator, so the user cannot leave it empty.<br>Furthermore, it must be inside our stated range of characters; if it is<br>outside of that range, an error notice will be displayed. If the password<br>does not match the DB password for that account, the error will be<br>thrown and the user will be denied access. We save passwords in hash<br>format. So we handle passwords in this manner.<br></div><div><br></div><div>4.&nbsp;Explains how the DB is utilized</div><div>We<br>are storing all of the registered information in our database. We are essentially<br>utilizing four databases, and all registered user data is stored in the 'Users'<br>database, where the author can view the user's email, id, hashed passwords, generated<br>date, edited timestamp, and username. This information will be used later for login<br>validation.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047679-42bcc2a1-690e-44fe-b1a7-3b35f61b68ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047680-14c10e5f-9296-49f3-b5bc-fe0a6e9c876d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>When the profile form is validated on submission, it creates an is_valid flag<br>with a default value of True. Email and username are taken from the<br>form data. If the collected data matches user data stored in the user<br>database, password hash values ​​are removed for subsequent steps. User roles are retrieved<br>from a table and logged in using the &quot;flask_login&quot; package. User objects are<br>stored as json in the session. Flask sessions are defined as a technique<br>for Flask utilities that act as extensions to provide server-side session support in<br>Flask applications built. Flask&#39;s session has a very similar concept to cookies. Data<br>containing an identifier for recognizing a computer on a network, except that session<br>data is stored on a server using it. To use sessions, you need<br>to set a private key. This private key is the value set for<br>a parameter within the application and is used for anything that requires authentication<br>to protect against attacks and tampering. Session object to set or get session<br>data. When a user uses a session, data is stored as a cookie,<br>which has a unique name called a session cookie. Now that the session<br>cookie has been set, the cookie&#39;s authenticity is checked on each subsequent request<br>to the server. As soon as you log out, Flask-Principal will remove the<br>session key.<gwmw style="display:none;"></gwmw><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047990-1bef4d8b-8dcf-4695-a4bd-01bb2eb30e25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047998-60bc5333-d69c-4e0d-a5c5-721199a96cd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not having proper role or permission (i.e., different<br>than the not logged in message)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047995-28740e4e-984f-4491-b4b9-2f19b16fedab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206047989-919535ae-1c48-45b9-b67c-7e563382bea2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the UserRoles table with valid data (Caption which is your admin<br>user)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The flask Principal system is used to establish permissions and roles for the<br>application.</div><div>Admin is specified, and permission is produced as an admin permission object that<br>may be imported into other routes. In main.py, two additional methods are added<br>to render templates for two files: 403 (access forbidden) and 404. (page not<br>found). These pages facilitate user navigation. Flask's register error handler() is used for<br>403 and 404, as well as mapping to their corresponding methods.</div><div><br><gwmw style="display:none;"></gwmw></div><div>Login Protected<br>Pages: Certain pages are only available after logging in, and we cannot access<br>them without proper credentials.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The flask Principal system is used to establish permissions and roles for the<br>application.</div><div>Admin is specified, and permission is produced as an admin permission object that<br>may be imported into other routes. In main.py, two additional methods are added<br>to render templates for two files: 403 (access forbidden) and 404. (page not<br>found). These pages facilitate user navigation. Flask's register error handler() is used for<br>403 and 404, as well as mapping to their corresponding methods.</div><div><div><br><gwmw style="display:none;"></gwmw><gwmw style="display:none;"></gwmw></div><div>Pages<br>with Role Protection: Some pages are only available to specific authorized users. For<br>example, Admin has access to all roles and can assign privileges and make<br>changes to the app. As a result, without admin credentials, it is impossible<br>to access the assigned privileges page.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206048545-ba09a80f-1432-43ff-8752-947e03a90f94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206048543-0ad50255-ac8f-45b9-81fb-2f70fe13ad2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206048547-da7d0168-005b-45da-a268-03e07f330aa2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI should be clean and not have my &quot;hideous&quot; example CSS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206048542-05e02e42-7518-4e9e-9833-120a166dcd67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output should be in a clean manner (i.e., table, row/cols, list groups,<br>etc) Basically not exactly like dumped plaintext<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206048544-6ec759fb-e6af-40e5-b53c-43d848de029b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>To make styling easier, all styling is done with Bootstrap capabilities. Various elements<br>may be found in the navbar code.</div><div>The backdrop is styled, and the container<br>fluid class is used to set the margins and grid lines.</div><div>Nav: A light<br>background color is utilized for navigation, and expansion is used for responsive collapse.<br>For your specific project, the Navbar brand is employed.</div><div>.navbar-toggler is a class that<br>may be used with our collapse plugin and other navigation toggling behaviors.</div><div>The margin<br>and padding may be modified to show the navbar responsively depending on screen<br>size. For Samples and Roles, a drop-down menu is generated.</div><div><div>Layout: We're describing our<br>layouts with headers and footers so that the form fits in our window<br>and we don't have to scroll. We also utilized it in our body<br>to define the text area and other boxes.</div><div>Flash: We utilized flash to display<br>the validation error wherever it was needed.</div><div>Add Sample: We used this to add<br>key-value pairs.</div><div>Edit Sample: We used it to modify key-value pairs.</div><div>Dropdowns: We used to<br>display options in a dropdown way; when the user clicks on the dropdown,<br>many related alternatives are displayed to the user.</div></div><div><div>List Sample: We utilized this to<br>list our key-value pairs, and we also provide you the choice of sorting<br>it in ascending or descending order.</div><div>403 and 404: We use 403 and 404<br>to display problems. 403, indicating insufficient access, and 404, for page not foun</div></div><gwmw<br>style="display:none;"></gwmw><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049030-31a1c8b7-fdca-4f0a-b629-66f7e3dde960.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages. + Show<br>at least 3 different &quot;error&quot; messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>Flash messages are used to handle technical communications and are designed to be<br>user-friendly in order to give users the necessary amount of information.</div><div>They give feedback<br>or alerts to the user, and the majority of them are provided via<br>session storage on the server or local storage in the browser.</div><div>There is something<br>called flash.html, which gets flashed messages, retrieves the session's queued messages, and displays<br>them in queued order, emptying the queue with each message.</div><div>By looping over all<br>of the messages, the required template is presented. Using the include keyword, this<br>is inserted into the layout after the navbar.</div><div>Flash("message", "bootstrap color") is used to<br>display all error/response messages.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049257-6a0ecc64-8151-4de6-8577-558a31a44267.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username should prefill properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>In the profile method, the user id is retrieved using the current user<br>and the flask login library, which has been loaded.</div><div>If the profile form is<br>verified upon submission, the flag is valid and is set to True by<br>default.</div><div>The email and username are retrieved via the completed Profile Form, which includes<br>the username, email, current password, password, confirm, and submit buttons.</div><div>If the username does<br>not meet the regex criteria, the valid flag is set to False and<br>a flash message indicating "Invalid Username" is shown.</div><div>Password changes are processed only if<br>the ProfileForm has values for the current password, password, and confirmation.</div><div>The current password<br>is matched using the password from the result row returned when the user<br>id is matched.</div><div><div>If the current password matches that in the SQL table, the<br>hash value for the new password is changed in the table; otherwise, flash<br>messages are created.</div><div>If all of the prerequisites for the profile form are met<br>and is valid is still True, the email and username are modified.</div><div>The database<br>is updated with the most recent data for email and username, and the<br>session for this user is updated to be the current user. Otherwise, a<br>flash message is generated.</div><div>Finally, display the profile.html template to see the page with<br>the email and username prefilled form fields.</div></div><gwmw style="display:none;"></gwmw><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049521-d0f86ad5-21e1-4e31-a2e7-885d92b9568d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049514-b2d367f1-b3c3-4632-b90c-ce417f1fccdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049518-79fbf79d-dbf1-4074-adca-6900f6535dc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049517-69ec79c3-0a57-4a07-b777-075af5f7a832.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049512-687e28ff-069f-477a-892e-2f2eb97c5dac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/206049510-681b94d3-c2cd-457b-9f1c-1660c4d164f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of the Users table when a user edits their profile + It<br>should be highlighted or note which record changes between both screenshots along with<br>what changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/58">https://github.com/sp2943/IS-601-005/pull/58</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>Depending on the current user, a user ID is generated, and the data<br>supplied in the profile form is confirmed upon submission. If validation is true,<br>an is valid flag check with the default value of True is produced.<br>Once all of the password values have been submitted, it attempts to obtain<br>the same value from the users database and checks the current password by<br>matching the hash value using the check password hash function. If this is<br>true, new password hash values are updated when the user database is updated.<br>&quot;Your password has been changed,&quot; a flash message will show on the screen.<br>Otherwise, an error flash message appears. Try updating your username and password if<br>is valid.&nbsp;Even if no password value is specified, this will throw. The most<br>recent information is gathered, and the session data is updated. Otherwise, an exception<br>is raised.<div>Username: Usernames are verified via regular expression matching. Lowercase letters, digits 0-9,<br>underscores, and hyphens are the only characters permitted. If the client/user-supplied value does<br>not match the regular expression, a validation error is thrown. Email: The specified<br>function validate email throws an error because @ does not appear in the<br>user&#39;s email address.</div><div>Password: Validators offered by libraries and packages are used to validate<br>passwords. The password matching component contains DataRequired() to indicate that if all three<br>are not given, the password can be modified, and a message is presented<br>to confirm that it can be altered. Furthermore, the length is defined in<br>the range (2, 30), therefore any number less than 2 or larger than<br>30 will result in an error.</div><gwmw style="display:none;"></gwmw><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Feature Registration (Username) - An issue was faced when the user was trying<br>to register with capital letters because ideally, it should not accept capital letters,<br>but we modified the file and added a regex and, now it prompts<br>an error when the user tries to use capital letters.</div><div><br></div><div>Feature login - I<br>was facing this issue when I was trying to log in initially, but,<br>after running the __init__dy.py file again and, executing a query a new, the<br>table has been created and everything worked after that. Also, checked the .env<br>file as there were some issues initially, which got fixed later.</div><div><br></div><div></div><gwofw><div>Feature Logout -<br>No issues were faced as such in logout. However, earlier the flash message<br>was not displaying which got resolved by making few changes in the code.</div><div><br></div><div>Feature<br>Security Rules &amp; Roles - Faced an issue initially when I tried to<br>search for 'Assign role' access. Later realized that for the first user we<br>will have to give the admin user in our UserRole table specifically. After<br>mapping the IDs, it worked.</div><div><br></div><div>Feature User friendly messages - A few flash messages<br>were not user-friendly in the beginning, but, changed the code a little bit<br>to make it more user-friendly.</div><div><br></div><div>Feature ProfilePage - Initially, the data was not showing<br>up but, after making a couple of changes in the flask login library,<br>it worked.</div><div>The user id is obtained in the profile function by utilizing the<br>current user and the loaded flask login library. The completed Profile Form, which<br>contains the username, email, current password, password, confirm, and submit buttons, retrieves the<br>email and username.</div><div><br></div><div>Feature Edit ProfilePage - Initially, regex was not working fine to<br>check the username for the capital letters but, fixed it later.</div><div>Then, introduced a<br>validator for the email ID.</div><div>Also, used a character size validator that gives a<br>prompt to the user if the correct length is not used.</div><div><br></div><div>Feature Basic styles/theme<br>applied - Specifically on the Profile page, when I was making a couple<br>of changes, then, the view was not perfect and, the scroller is not<br>there, so I had to reduce the page size to see the update<br>button.</div><div>Will look into it to change the layout and, close this issue.</div></gwofw><div></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod.herokuapp.com/sample/add">https://is601-sp2943-prod.herokuapp.com/sample/add</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/sp2943" target="_blank">Grading</a></td></tr></table>