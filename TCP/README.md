This program is a client and server chat room, using TCP.  It contains a GUI that
the user uses to enter a server IP address and the user's name to connect to the server.
The GUI then shows all users who are connected to the server including itself and
automatically updates when a new user comes or when the user disconnects.  
All messages and emojis are sent to all members. The user either can write a message
and click send or can click on one of emojis and the emoji will be sent.
With the limitation of sending 5 messages in a row without getting an answer.
In that case, even if the user clicks on the send button or emojis message won't be sent.

To execute the program, open a terminal window with the capability of running
python.  Start server.py first then in a different window run as many client.py
as needed. Then fill in the information that is asked for, the IP Address
127.0.0.1 is the local connection.