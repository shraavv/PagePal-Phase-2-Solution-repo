## Gopal and his PagePal Phase 2 Evaluation Criteria

**Criteria for the task to be marked as done:**
- If req data ( book title, author, description, year published, language and preview) are properly fetched when the ```/book``` command is executed and returns a csv file. The csv file should contain only the latest genre books.(On typing in a new genre, the old genre details should not be present.)
- The ```/preview``` command should either redirect to the preview link or return the link as a message.
- The reading list should add and delete books properly and should be implemented as a docx. There is no such thing as append (like in csv files) in docx, therefore while testing the reading list command, add and delete the books multiple times to check if the reading list is updated properly (/list and /reading_list could be clubbed together as a single command but should add and delete books as mentioned above)
- The ```/reading_list``` command should be implemented as buttons.
- All the commands listed below should be properly implemented.

**Criteria for the task to be marked as partially done:**
- All the commands except ```/list``` and ```/reading_list``` are implemented properly.


**PagePal, the telegram bot should have the following commands**

- ```/start``` - returns a welcome message to the user 
- ```/book``` - asks the user to type in the genre and returns a csv file with the list of books 
- ```/preview``` - asks for a book name and redirects to preview link 
- ```/list``` - asks the user to type in a specific book name and then it returns a message to execute /reading_list command
- ```/reading_list``` - allows the user to add a book, delete a book or view their reading list 
- ```/help``` - returns the list of all commands with a description to it 

**NOTE: Bonus points if they customised the reading list with different styles.**


