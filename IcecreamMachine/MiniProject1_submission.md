<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Satyam Adharchandra Pandey (sp2943)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2022 10:43:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/sp2943" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197428188-ddaa0d10-f743-4a13-97ad-2e76b690a37f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Method should calculate the proper value of the inprogress_icecream array (the costs<br>are defined as part of the given data and should not be modified)<br>    #3 The calculated value should be returned from the<br>function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197428388-d165582f-18e1-49e4-a623-81698b931591.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 The input() message should properly display the value in currency format (this<br>should be present in one of the screenshots)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197428466-5d042402-acf5-4da6-aae5-4a3a3a4330e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Captions should highlight what each screenshot is attempting to show<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>#1&nbsp;<div><ul><li><span style="color: rgb(156, 220, 254); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; white-space: pre;">First of all, we are checking the container type, if it&#39;s<br>a waffle cone, then, the value should be $1.5 else it should be<br>$1.</span></li><li><font color="#9cdcfe">Then, we are taking the price of the flavor and toppings, after<br>that, we are checking that, how many flavors and toppings the user is<br>selecting by subtracting the remaining scoops from Max scoops, similarly for toppings as<br>well.</font></li><li><font color="#9cdcfe">Then, finally, we are calculating the total cost by adding the price<br>of the container plus consumed scoops multiplied by its price plus consumed toppings<br>multiplied by its price.</font></li><li><font color="#9cdcfe">Then we are returning the total_cost.</font></li></ul><div style="background-color: rgb(30, 30,<br>30); font-family: Consolas, &quot;Courier New&quot;, monospace; line-height: 19px; white-space: pre;"><div style=""><font color="#9cdcfe"><br></font></div><div style="">&lt;font<br>color=&quot;#9cdcfe&quot;&gt;#2 First, we have added the currency value in the input prompt, so<br>user gets an idea about the currency. </font></div><div style=""><font color="#9cdcfe">Later, we are formatting<br>it to not accept any other values other than the exact matching value<br>with the currency. If the value is not exact, then it keeps prompting<br>again and again, thus user has to enter the correct value only.</font></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429436-ae419e44-712e-4c85-919d-a33d4d595e0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Container Out of Stock - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429540-8e1690b9-900d-4d62-a6c8-27741c96cae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Flavor Out of Stock - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429595-a855b08d-89ec-43a2-9e48-7d67782d8fb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Toppings Out of Stock - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429653-84146960-06da-4a81-aea5-2ff05e6bda6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Container Out of Stock - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429721-5a83ee36-b083-421f-ba5f-d48f6f321ef5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Flavor Out of Stock - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429782-9c1c1f8c-f847-4468-9711-4915b8a330a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Toppings Out of Stock - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197429964-3f46958c-7aad-4523-b95b-909cb6017b02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Needs Cleaning - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430025-001d5abf-cf27-4911-b0b0-548afc0f03ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Needs Cleaning - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430220-ef2e9a26-a53c-4ffa-9392-7acbcbaeb9c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Container Invalid Choice - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430252-c24a481f-bf3d-4071-a949-593ab5fb5f27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Flavor Invalid Choice - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430288-dd45c643-acaf-499c-964b-adff8c36c667.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Toppings Invalid Choice - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430391-2452b2cb-9f2a-436e-a494-202029c1c92c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Invalid Choice - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430489-652588ec-3f72-48a4-a5bf-088dfc09c5e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Exceeded Remaining Choice - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430537-d5b8a635-11ad-4792-8d26-7f6eef75e14f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Exceeded Remaining Choice - Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430661-66e217f7-0aec-49c7-a3af-36e13b6095d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Invalid Payment Exception - Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197430727-aca9e545-053b-4f63-9cdc-f2be8b435f0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Invalid Payment Exception - Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">OutOfStockException - We are using this exception when we are running<br>out of stock for either container, flavors, or toppings. If we don&#39;t use<br>the exception, then our code will crash when we run out of stock,<br>hence we are using these exceptions. If we assume that, for flavors we<br>have ran out of &#39;vanilla&#39; then our code will no longer show the<br>option of vanilla  flavors until we stock it back, in this way<br>we can run our program even if we don&#39;t have all the items.&nbsp;</span><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<br></span><div><span style="font-size: 13px;">NeedsCleaningException - After a few servings, we usually clean our<br>system. Similarly, in our program, we have set that after delivering 100 flavors,<br>our machine should be cleaned. Hence, we are raising this exception, if we<br>don&#39;t clean it then, it will not allow us to take the ice<br>creams.&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">InvalidChoiceException - We are providing a few choices for<br>containers, flavors, and toppings, if the user is selecting anything apart from the<br>available option, then our program is telling the user to select the available<br>options and calls the function again via an exception.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">ExceededRemainingChoicesException<br>-&nbsp; We are only allowing 3 flavors and 3 toppings for each ice<br>cream, after the user adds the maximum amount of flavor and topping, our<br>program tells the user that they reached the maximum and, jumps to another<br>function.&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">InvalidPaymentException - After all the selections, our program tells<br>the total bill to the user, which the user has to enter correctly,<br>else it won&#39;t checkout and prompts again to enter the exact value.&nbsp;</span></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432059-ba084a99-f0c2-472e-872c-b331db967ce6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 1 - container must be the first selection (can&#39;t add flavors/toppings without<br>a container choice)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432128-f84be878-15bd-4548-819b-3b5036808d6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 - can only add flavors if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432254-a95e5b65-e5b6-4d47-9eb0-7ab6fcb58b5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 3 - can only add toppings if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432318-1bfc6027-1cea-45f6-8fcd-f20f97127372.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 - Can add up to 3 flavors/scoops<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432360-67c06358-d463-4a5e-b161-88ca1db94e78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 - Can add up to 3 toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432397-9b420041-af0a-46bc-9bd7-9ec5a5d0ae34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 - cost must be calculated properly based on the choices (check<br>for currency format as part of this) (test case should have a few<br>permutations of choices)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432456-234bb04a-cd17-4729-bbbc-46c69a570c04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 - Total Sales (sum of costs) must be calculated properly (test<br>case should included a few icecream combinations/purchases)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432506-3cc32796-1e9e-4f63-900f-6d43be2ed321.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 - Total icecreams should properly increment for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197432551-a7134931-d1e6-40e5-926e-d24b8604a74c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show all Tests 1-8 passing and any relevant output (it should be clear<br>which test case is which)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test case 1 - Here, we are creating a unit test to check<br>that the first choice should be a container and, we cannot add flavor<br>or toppings before selecting the container.<div><br><div>Test case 2 - Here, we are creating<br>a unit test to check that we can add flavors only when it<br>is in stock, for this, we have changed the quantity of flavors to<br>2 and trying to exceed the available quantity, where that test case fails.<br></div><div><br></div><div>Test<br>case 3 - Here, we are creating a unit test to check that<br>we can add toppings only when it is in stock, for this, we<br>have changed the quantity of toppings to 2 and trying to exceed the<br>available quantity, where that test case fails.<br></div><div><br></div><div>Test case 4 - Here, we are<br>creating a unit test to check that we can add flavors only up<br>to 3 times, which is the maximum amount permitted. If we will try<br>to add more than 3 flavors, the test case will fail.&nbsp;<br></div><div><br></div><div>Test case 5<br>- Here, we are creating a unit test to check that we can<br>add toppings only up to 3 times, which is the maximum amount permitted.<br>If we will try to add more than 3 toppings, the test case<br>will fail.&nbsp;<br></div><div><br></div><div>Test case 6 - Here, we are checking that cost should be<br>calculated according to our choices, like container&#39;s choice, flavor&#39;s choice and topping&#39;s choice.<br>If the cost is not correct then the test case will fail.&nbsp;<br></div><div><br></div><div>Test case<br>7 -Here, we are trying to calculate the sum of cost (total sales)<br>by asserting the cost of individual sales, if the final cost doesn&#39;t match<br>to the overall cost of individual ice cream, then this test case will<br>fail.&nbsp;<br></div><div><br></div><div>Test case 8 - Here, we are checking our number of sales, where<br>we are asserting the count after each sale. At the end, we are<br>checking the total number of icecream, if it doesn&#39;t match, then this test<br>will fail.&nbsp;<br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sp2943/IS-601-005/pull/6">https://github.com/sp2943/IS-601-005/pull/6</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Learning - In this project, we learned to set up test cases which<br>is very beneficial for unit testing. In this we can test individual functions<br>and, we do not have to test the entire code. Moreover, we also<br>learned about arithmetic operations.&nbsp;<div>Furthermore, we learned about exception handling which is very useful,<br>if we do not handle exceptions then our code will crash and we<br>cannot work on it, we also learned about recursive functions.&nbsp;</div><div>We also learned about<br>gitignore file.</div><div><br></div><div>Issues/ Dificulties -&nbsp;</div><div>Initially, I was facing issues while setting up test cases,<br>it was not getting automatically, which got resolved after changing the naming convention.</div><div>I<br>was also facing a few issues with exception handling where it was not<br>working properly but, then I used recursion and, it worked.&nbsp;</div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197436290-a1007d12-7d99-468b-96a1-c35774cc00c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful program execution 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197436390-4be5f480-b96b-47a4-8996-9a794e0a1e4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful program execution 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113465437/197436414-fe7a50b6-588e-4e3a-9eb8-5193976717d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful program execution 3<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/sp2943" target="_blank">Grading</a></td></tr></table>