# Train-Reservation-SQLite
Steps to Execute Program (Web-Web):

1.	Bring up the Train-Reservation-SQLite Webapp directory into the IDE PyCharm as a project. 
2.	The server.py has the code for the webserver. Open that file in the IDE. 
3.	The IDE will install any libraries needed (bottle webserver library, pygame library, etc.). Python 3.7 (or higher most likely) may have to be setup under Project Structure (Module Libraries). 
4.	Run server.py to start the webserver. 
5.	Open the link ‘http://localhost:8080/’ that comes up in the IDE’s run window. 
6.	A browser window should open displaying a Welcome page. It comprises of the heading “Book a ticket”and displays 3 input areas (input type is text for all): “Train Number (11 digits)”, “Seat Number”, “Passenger name”. Once the user clicks on the “Submit” button. His/her booking information is displayed below the “Submit” button.


Architecture and Concepts:

The application allows users to Book a Train Ticket. The front-end should consist of an interface
that shows the existing list of reservations and also allows users to input ‘Train Number’, ‘Seat
Number’, and ‘Name of Passenger’ and come back with a confirmation that shows all the
reservations including the newest one – the confirmation should be of the form ‘Train Number
– Seat Number – Passenger Name’. Note: the program should not allow duplicate reservations
– ie, no two confirmations should have the same ‘train number’ and ‘seat number’
combination. The project consists of the following:

1.	Server.py – the file implements a python webserver using the bottle library. Bottle’s static_file return function is used to show the default ‘index.html’ page which in-turn loads the JavaScript file ‘myCode.js’ and the application icon ‘favicon.ico’. 
2.	Index.html – the page downloads the JavaScript code myCode.js that implements a function getBookings() from the webserver. It then calls getBookings() in the body tag’s onload. getBookings() uses AJAX GET request (ajaxGetRequest) using the ‘bookings’ path. The asynchronous code then calls the ajaxGetRequest with “bookings” as the path (also the div id passed in index.html) as well as the function bookingsCallback. 
3.	Server.py handles the ‘bookings’ path by calling the function bookings.get_bookings().
4.	bookings.get_bookings() retrieves the data from local SQLite database “bookings.db" and converts it to JSON and sends it back to the browser. The callback in the javascript code is executed when the data comes back. The ‘bookingsCallback(response)’ function contains the code that modifies ‘index.html’ under the ‘div bookings’ tag.
5.	Note: changing any of the Javascript etc. files that the html accesses can result in the webserver still using the old files due to browser caching. The issue can be avoided by forcing the browser to do a “hard refresh” - Windows: Ctrl+F5, Mac: Cmd+Shift+R, Linux: Ctrl+Shift+R. Also, use “debug=True, reloader=True” as additional bottle.run parameters when developing code.
