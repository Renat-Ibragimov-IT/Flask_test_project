# Flask_test_project

The purpose of this task is to acquire skills in working with the program.
We need to create 3 pages `/`, `/login`, `/logout`:
- The main page `/` will display how many times the user opened the page and 
  which user logged in to the site (added to the session).
- The `/login` page will accept two types of GET and POST requests, 
  when we just open the page, a form for entering a username should appear, 
  after the user has entered the nickname form and clicked "Submit", 
  the system should add this user to the session, 
  and display the result in template.
- Example: "User logged in as username".
- If the user wants to go to this page again, and he is logged in, 
  then instead of the form the same text should appear: 
  "The user logged in as a username"
- The `/logout` page should clear the session if the user is logged in to the
  system.