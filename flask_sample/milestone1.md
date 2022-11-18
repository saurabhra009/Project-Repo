<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Satyam Adharchandra Pandey (sp2943)</td></tr>
<tr><td> <em>Generated: </em> 11/18/2022 3:44:50 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/sp2943" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202618436-c3ab3e91-f744-42ac-af0e-62bbad447a00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202618510-64451dba-686f-4b1b-8dd4-6eb5b20878fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid email validation1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202618809-39c2327e-e301-4e76-9a16-efde4b7e737d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202618889-e11efe5d-987d-4eaf-96c9-f382a5bb278a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202619076-19bd2b96-087d-4c3d-8773-f82a0a8c0ea1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202619189-8230d248-243d-433f-8a08-ee3d48880d82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202619242-0e9e19cd-9bd4-4eba-bbd9-9c3d429e1b29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202619243-acc73f61-aca1-4d98-8430-1178b0fdd1d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 should be present in this screenshot.<br>Clearly highlight which row it is.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Explains how the form is handled and behaves<div>We generated a template for<br>form layouts and registered using RegistrationForm.py. To obtain the needed data, we employed<br>a number of validators. We developed a database in our locally for validations,<br>which we utilize to check the data from the registration form and provide<br>login access. We ask the user to input their username, email address, password,<br>and confirmation password, and then they may submit these credentials to create a<br>new user. We display a &#39;Successful creation&#39; message after successful creation.</div><div><br></div><div>2.&nbsp;Explains the validation<br>logic (frontend and backend)</div><div><div>To obtain the necessary information from the user, we employed<br>a number of validators in our form. If a user has a one-character<br>password, the system will throw an error. Similarly, we employed additional validators.</div><div>When a<br>user enters data that is not the required one, we display a notice<br>that is intelligible by a normal human on the front end. For the<br>front end, we used flash messages. In the backend, we used validators that<br>we had already established for our convenience. For example, the user cannot leave<br>any box empty since we have set an &#39;InputRequired&#39; validator, which would prompt<br>a flash message if no data is present, and input for password registration<br>should be between (2,30) characters.</div></div><div><br></div><div>3.&nbsp;Explains how the password is handled</div><div>We employed validators to<br>handle our passwords, and we also require the user to input the password<br>twice to eliminate the possibility of error. First, we utilized the &#39;InputRequired&#39; validator<br>so that the user could not leave it empty. Second, it must be<br>inside our set range of characters; if it is outside of that range,<br>an error notice will be displayed. Finally, we are requesting the user to<br>input the password twice, so if the user enters the incorrect password the<br>second time, an error notice will be displayed. So we handle passwords in<br>this manner.<br></div><div><br></div><div>4.&nbsp;Explains how the DB is utilized</div><div>We are storing all of the registered<br>information in our database. We are essentially utilizing four databases, and all registered<br>user data is stored in the &#39;Users&#39; database, where the author can view<br>the user&#39;s email, id, hashed passwords, generated date, edited timestamp, and username. This<br>information will be used later for login validation.<br></div><div><br></div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202619964-4d18af24-7be1-450f-b2ba-fc9f19ee67b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202620058-f82a7b0d-f1f4-4eb1-8b7d-4ece4aac849c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202620549-c14730b7-19eb-40aa-9f10-320faec97b83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot of successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1.&nbsp;Explains how the form is handled and behaves</div><div>We made a template for form<br>layouts and used LoginForm.py to log in. To obtain the needed data, we<br>employed a number of validators. We developed a database in our locally for<br>validations where we store the registered data and use it for comparison to<br>validate the data from the registration form and provide login access. We are<br>requesting the user to input their username or email address and password, and<br>then they may submit these data to log in. After a successful login,<br>we display a 'Successful login' message and the user may view further information.<br></div><div><br></div><div>2.&nbsp;Explains<br>the validation logic (frontend and backend)</div><div><div>We already have the data from the signup<br>page in our database, which we use as a validator for login.</div><div>If the<br>data does not match, we display an error message with the appropriate message<br>that the user may readily understand. In the backend, we simply compare the<br>entered data with the data recorded in our database during the registration process.</div></div><div><br></div><div>3.&nbsp;Explains<br>how the password is handled</div><div>We have employed validators to handle our passwords; essentially,<br>we are using the data supplied during the registration process as a validaor.<br>We also used the 'InputRequired' validator, so the user cannot leave it empty.<br>Furthermore, it must be inside our stated range of characters; if it is<br>outside of that range, an error notice will be displayed. If the password<br>does not match the DB password for that account, the error will be<br>thrown and the user will be denied access. We save passwords in hash<br>format. So we handle passwords in this manner.<br></div><div><br></div><div>4.&nbsp;Explains how the DB is utilized</div><div>We<br>are storing all of the registered information in our database. We are essentially<br>utilizing four databases, and all registered user data is stored in the 'Users'<br>database, where the author can view the user's email, id, hashed passwords, generated<br>date, edited timestamp, and username. This information will be used later for login<br>validation.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202620841-7fc19cb0-6da1-427f-9249-a9f82b2c583d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202621560-b93cac3e-3ecf-46b1-898b-5c780d946a1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>When the profile form is validated on submission, it creates an is_valid flag<br>with a default value of True. Email and username are taken from the<br>form data. If the collected data matches user data stored in the user<br>database, password hash values ​​are removed for subsequent steps. User roles are retrieved<br>from a table and logged in using the &quot;flask_login&quot; package. User objects are<br>stored as json in the session. Flask sessions are defined as a technique<br>for Flask utilities that act as extensions to provide server-side session support in<br>Flask applications built. Flask&#39;s session has a very similar concept to cookies. Data<br>containing an identifier for recognizing a computer on a network, except that session<br>data is stored on a server using it. To use sessions, you need<br>to set a private key. This private key is the value set for<br>a parameter within the application and is used for anything that requires authentication<br>to protect against attacks and tampering. Session object to set or get session<br>data. When a user uses a session, data is stored as a cookie,<br>which has a unique name called a session cookie. Now that the session<br>cookie has been set, the cookie&#39;s authenticity is checked on each subsequent request<br>to the server. As soon as you log out, Flask-Principal will remove the<br>session key.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202622298-f27fa86b-1c4c-4281-960a-19198a23340e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202622899-efdf9ed1-24b1-4c42-8440-b5efa46ba4c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not having proper role or permission (i.e., different<br>than the not logged in message)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202623802-6c54c3fb-9043-408a-a4e3-e233332f26ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Must have at least one valid record from the lessons (i.e., Admin)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202623658-9740df59-366b-4fc9-845d-b7bd8dfd6374.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Caption which is your admin user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202624647-791cd49e-bd9e-4040-bde7-17815811f561.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Caption which is your admin user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The flask Principal system is used to establish permissions and roles for the<br>application.</div><div>Admin is specified, and permission is produced as an admin permission object that<br>may be imported into other routes. In main.py, two additional methods are added<br>to render templates for two files: 403 (access forbidden) and 404. (page not<br>found). These pages facilitate user navigation. Flask's register error handler() is used for<br>403 and 404, as well as mapping to their corresponding methods.</div><div><br></div><div>Login Protected Pages:<br>Certain pages are only available after logging in, and we cannot access them<br>without proper credentials.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The flask Principal system is used to establish permissions and roles for the<br>application.</div><div>Admin is specified, and permission is produced as an admin permission object that<br>may be imported into other routes. In main.py, two additional methods are added<br>to render templates for two files: 403 (access forbidden) and 404. (page not<br>found). These pages facilitate user navigation. Flask's register error handler() is used for<br>403 and 404, as well as mapping to their corresponding methods.</div><div><div><br></div><div>Pages with Role<br>Protection: Some pages are only available to specific authorized users. For example, Admin<br>has access to all roles and can assign privileges and make changes to<br>the app. As a result, without admin credentials, it is impossible to access<br>the assigned privileges page.</div></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202624793-c927a566-c8e9-40ab-8174-19ec47a962a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202624875-b2bbc46f-8910-4dee-a24c-8f195bb8d18c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled-Login<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202625448-a785c930-0d5b-4d22-bc71-8ffe6a151ca2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled-Register<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202625780-e952c814-2d38-4448-94fd-d61f8dbc00e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI should be clean and not have my &quot;hideous&quot; example CSS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626011-f3ccc5f9-7809-4415-93b3-7519f84a7adf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output should be in a clean manner (i.e., table, row/cols, list groups,<br>etc) Basically not exactly like dumped plaintext<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>To make styling easier, all styling is done with Bootstrap capabilities. Various elements<br>may be found in the navbar code.</div><div>The backdrop is styled, and the container<br>fluid class is used to set the margins and grid lines.</div><div>Nav: A light<br>background color is utilized for navigation, and expansion is used for responsive collapse.<br>For your specific project, the Navbar brand is employed.</div><div>.navbar-toggler is a class that<br>may be used with our collapse plugin and other navigation toggling behaviors.</div><div>The margin<br>and padding may be modified to show the navbar responsively depending on screen<br>size. For Samples and Roles, a drop-down menu is generated.</div><div><div>Layout: We're describing our<br>layouts with headers and footers so that the form fits in our window<br>and we don't have to scroll. We also utilized it in our body<br>to define the text area and other boxes.</div><div>Flash: We utilized flash to display<br>the validation error wherever it was needed.</div><div>Add Sample: We used this to add<br>key-value pairs.</div><div>Edit Sample: We used it to modify key-value pairs.</div><div>Dropdowns: We used to<br>display options in a dropdown way; when the user clicks on the dropdown,<br>many related alternatives are displayed to the user.</div></div><div><div>List Sample: We utilized this to<br>list our key-value pairs, and we also provide you the choice of sorting<br>it in ascending or descending order.</div><div>403 and 404: We use 403 and 404<br>to display problems. 403, indicating insufficient access, and 404, for page not found</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626790-e82b49dc-a73b-4aa6-9305-92ecf63f99b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - Email<br>not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626791-380e528c-1e81-4f2c-8451-01ae9c1af521.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - <br>Invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626792-7339afe9-8dad-4801-89e4-2d3a9acdc67f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - Password<br>Mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626793-75bbf6a0-a86e-4858-a73f-363b5bf3cfd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - Password<br>Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626794-c1b68317-6df8-40d3-a33f-76f6c373c499.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - Username<br>not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202626795-902d7b53-dba1-4240-a84b-9f180ad4039a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages - Non<br>existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>Flash messages are used to handle technical communications and are designed to be<br>user-friendly in order to give users the necessary amount of information.</div><div>They give feedback<br>or alerts to the user, and the majority of them are provided via<br>session storage on the server or local storage in the browser.</div><div>There is something<br>called flash.html, which gets flashed messages retrieves the session's queued messages, and displays<br>them in queued order, emptying the queue with each message.</div><div>By looping over all<br>of the messages, the required template is presented. Using the include keyword, this<br>is inserted into the layout after the navbar.</div><div>Flash("message", "bootstrap color") is used to<br>display all error/response messages.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202627679-a4a1a0d6-50b7-4435-9ebb-2ef115179986.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username should prefill properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>In the profile method, the user id is retrieved using the current user<br>and the flask login library, which has been loaded.</div><div>If the profile form is<br>verified upon submission, the flag is valid and is set to True by<br>default.</div><div>The email and username are retrieved via the completed Profile Form, which includes<br>the username, email, current password, password, confirm, and submit buttons.</div><div>If the username does<br>not meet the regex criteria, the valid flag is set to False and<br>a flash message indicating "Invalid Username" is shown.</div><div>Password changes are processed only if<br>the ProfileForm has values for the current password, password, and confirmation.</div><div>The current password<br>is matched using the password from the result row returned when the user<br>id is matched.</div><div><div>If the current password matches that in the SQL table, the<br>hash value for the new password is changed in the table; otherwise, flash<br>messages are created.</div><div>If all of the prerequisites for the profile form are met<br>and is valid is still True, the email and username are modified.</div><div>The database<br>is updated with the most recent data for email and username, and the<br>session for this user is updated to be the current user. Otherwise, a<br>flash message is generated.</div><div>Finally, display the profile.html template to see the page with<br>the email and username prefilled form fields.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202627989-127cfcb7-d62e-4e16-b436-442cbb12c2ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202628133-8837eaa7-db5c-4835-bcb1-72d66c83006a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202628199-0ecf1dea-bc1a-4785-96fa-422657b93818.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202628333-150366a0-6767-4250-a0ee-54dd6023c293.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202628415-31cce2ef-296d-4fc1-a821-49c29cacb53b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202628543-9426bf56-bee6-4a86-8edf-ef5841a305b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It should be highlighted or note which record changes between both screenshots along<br>with what changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202629254-7aeb112a-0735-4680-b1d7-2f6fde9ce001.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Final Screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/28">https://github.com/sp2943/IS-601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>Depending on the current user, a user ID is generated, and the data<br>supplied in the profile form is confirmed upon submission. If validation is true,<br>an is valid flag check with the default value of True is produced.<br>Once all of the password values have been submitted, it attempts to obtain<br>the same value from the users database and checks the current password by<br>matching the hash value using the check password hash function. If this is<br>true, new password hash values are updated when the user database is updated.<br>&quot;Your password has been changed,&quot; a flash message will show on the screen.<br>Otherwise, an error flash message appears. Try updating your username and password if<br>is valid.&nbsp;Even if no password value is specified, this will throw. The most<br>recent information is gathered, and the session data is updated. Otherwise, an exception<br>is raised.<div>Username: Usernames are verified via regular expression matching. Lowercase letters, digits 0-9,<br>underscores, and hyphens are the only characters permitted. If the client/user-supplied value does<br>not match the regular expression, a validation error is thrown. Email: The specified<br>function validate email throws an error because @ does not appear in the<br>user&#39;s email address.</div><div>Password: Validators offered by libraries and packages are used to validate<br>passwords. The password matching component contains DataRequired() to indicate that if all three<br>are not given, the password can be modified, and a message is presented<br>to confirm that it can be altered. Furthermore, the length is defined in<br>the range (2, 30), therefore any number less than 2 or larger than<br>30 will result in an error.<br></div><div><br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Issues and Project Board </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing which issues are done/closed (project board) Incomplete Issues should not be closed</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657671-34e260e8-4a58-4be9-9def-1016386e0ad4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657674-8a653f4f-6b5d-4084-a6ee-e3ce86ec580c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657676-4096aa1e-51ab-4e6c-b2f2-712129bac3a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657677-9deb1138-9cf1-4472-bbee-40093313df7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657679-bc498c27-9c45-4743-9599-8133a38c6f65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657681-441e7f20-104f-4be9-be3a-f669eb9c5844.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657682-930f4bd3-deb4-4ec4-b994-85306e5b377b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657686-1d926246-6bee-49c9-9d60-e0deb0676e90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Issue item per Milestone feature 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/202657668-d2c7d2ae-4ad7-4d47-8eca-543aed5fdf39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All projects<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include a direct link to your Project Board</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/users/sp2943/projects/1">https://github.com/users/sp2943/projects/1</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sp2943-prod.herokuapp.com/sample/add">https://is601-sp2943-prod.herokuapp.com/sample/add</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/sp2943" target="_blank">Grading</a></td></tr></table>