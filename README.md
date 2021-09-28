Offensive Cyber Python Project
By Gil Shwartz

This is a mouse movement-based spyware/backdoor program written in Python.
This demo has preset timers, IRL, timers are set randomly, the last timer is 24hrs fixed. 
All terminal output is for the demo only, in a real environment everything is hidden.
When the user clicks on the file for the first time the program starts with establishing persistence and tracking mouse movements while trying to connect to the attacker’s C&C at the same time.
Then, collects the station’s OS/System/Network info and dumps it to a file. 
Stages of attack (Victim side):
    1. Ensure persistence – plant itself on core OS processes such as autorun via registry, update hosts file to avoid AV detection (only if activated as Admin – workaround can         be made from the attacker’s C&C server with other privilege escalation tools).
    2. Connect to attacker’s backdoor.
    3. Track mouse movement / grab initial screenshots every random (N) seconds (to avoid pattern detection).
    4. Activate passive keylogger.
    5. Zip screenshots & dump files to a different folder.
    6. Upload zip folder to attacker’s FTP server every random (N) seconds (to avoid pattern detection).
    7. Delete local files every random (N) seconds (to avoid pattern detection).

Background activity (Victim Side):
    - Mouse tracks position for every (N) second set by the attacker. If (N) time passed and the mouse didn’t change position then the program grabs a few screenshots, zip and         uploads to the attacker’s FTP server.
    - Keylogger still active.
    - A second timer is set that counts for a longer period of (N) seconds, if there wasn’t any mouse movement the program grabs a few screenshots, 
      zip and upload to FTP server.
    - A third and final timer is set to check for mouse movement every 30 minutes for a period of 24 hours while every 30 minutes the program grabs a few screenshots, 
      zip and upload to FTP server.

    • Backdoor connection always alive and trying to connect to the attacker’s C&C by a random choice of port numbers given by the attacker to avoid pattern detection.

Server side activity:
    • A command and control server responsible for handling incoming connections from victims and interact with each connection as a reverse shell or run a Botnet command to all       connected machines.
    • In a real environment the server will be hosted behind a DNS to overcome the IP changes.
    • The server is currently set to listen on 100 ports (set by a designated random loop) between 5000 and 65500.
    • Backdoor is configured to randomly choose a port from the list and connect to the server to avoid pattern detection.
    • A pulse-check runs a ping command and a custom msg set by the attacker to the connected machines every random (N) seconds. If ping is lost or there’s no reply msg from the       target then the connection is closed and the target list updates.
    • If the target machine doesn’t respond to ping but do respond to a poke msg then it stays on the active targets list.
      Targeted shell control:
    • The server has the option to manual control each target.

*** I removed the backdoor code block for security reasons.
