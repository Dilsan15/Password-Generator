<h2>Summary</h2>
<p>It is a readable password generator which is very light-weight and creates secure passwords to use on the web and anywhere else. Takes user input to determine length of the password and certain characters in the password. Uses Python libraries such as requests (for API communication) to accomplish task. Open source and free to use by anyone!</p>

<h2>Purpose</h2>
<p>Developed to complete a two week long project for a CS 10, 2022 high school course</p>


<h2>Processes</h2>

<ol>
  <li>Creates applicaiton interface (Window --> User Input Feilds --> User Output Feild)</li>
  <li>After the user submits input, conducts error checking of the input submitted. Gives feedback if an error is detected</li>
  <li>if no error is detected, it collects the data of the user input and contacts the API, telling it to return words based on the data received </li>
  <li>Computes a suitable, readable and secure password based on the words returned by the API</li>
  <li>Displays the password to the window, and allows foe easy copying</li>
</ol>

<h2>Files</h2>

<ul>
  <li>gen_main_app: responsible for displaying input feilds and output on screen. Acts as a connector between multiple classes</li>
  <li>gen_error: Checks if user input has any errors, and displays warnings if an error is found/li>
  <li>gen_creation: Creates password from words which it gets from gen_api and input received from main_app</li>
  <li>gen_api: Talks to API, receives random words which are filtered by user input values </li>
</ul>

<h2>Versions</h2>

<ul>
  <li>Python: 3.10.5</li>
  <li>Pyglet: 1.5.26</li>
<ul>

