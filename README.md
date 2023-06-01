This is my primary Django folder, including several different pages with different functions.
To run the code, write "python3 manage.py runserver" in a terminal window once you are inside the folder.
Paste the given URL (likely http://127.0.0.1:8000/) into a browser tab.
The four different pages within the wider server are as follows:
1. challenges (URL http://127.0.0.1:8000/challenges/)
This was the first django webpage I wrote, working with links to navigate between different pages.
2. subjects (URL http://127.0.0.1:8000/subjects/)
This is an assignment page simulator, enabling a user to navigate between subjects to see assignments and due dates.
3. MusicDatabase (URL http://127.0.0.1:8000/MusicDatabase/) NONFUNCTIONAL: EMPTY DATABASE
This page draws from a SQL database and can sort albums by artist name, album name, or date released. If a user were to click on an author
name, it would give the author's discography. If they were to click on an album name, they would see a lost of songs in the album, including
song name and length. The database that this page functioned off of was provided by the school and has been taken down, so the current
page that appears will be empty.
4. chatbot (URL http://127.0.0.1:8000/chatbot/) NONFUNCTIONAL: INVALID KEY
This page requires a ChatGPT key in order to function, so it may give an error if the provided key is invalid. The current key that is in
the program has run out of uses, but the initial page will appear. When a user enters a question or prompt into the text box on the page,
it will return either the answer to a question using the Davinci-003 AI model or an image based on a prompt using the DALL-E model. The 
user can choose whether they would like to enter a question or image prompt, as well as the size of their returned image.
