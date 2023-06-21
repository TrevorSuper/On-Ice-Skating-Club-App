# Instructions to run this program
Step 1 - This program runs on Python version 3.11.3<br>
<br>
Step 2 - You will also need Visual Studio code and the Visual Studio Code Python extension<br>
   - Follow the links below:<br>
   - https://code.visualstudio.com/docs/python/python-tutorial<br>
   - Follow this video until 2:24: https://www.youtube.com/watch?v=L3FwRRx6bqo<br>
   The SQLite plugin in VS Code doesn't install SQLite. It only adds the capability to VS Code to connect to a SQLite database.<br>
<br>
So, yes, you have to -<br>
<br>
Install SQLite in your operating system as that is not installed. To do this, go to the SQLite download page, scroll down to the<br>
section titled Precompiled Binaries for Windows and click on the link which looks like sqlite-tools-win32-x86-3350500.zip. The<br>
description should be something along the lines of - "A bundle of command-line tools for managing SQLite database files, including<br>
the command-line shell program ..."<br>
<br>
After unzipping this. put the files somewhere on your system and add that directory to your PATH environment variable. This will enable 
sqlite3 command line program.<br>
<br>
You can use any of the numerous SQLite DB applications to not only view, but also modify and write complex SQL queries.<br>
My favourite is SQLite Studio<br>
<br>
Finally, if you really want to use the command line, then you can just type -<br>
<br>
sqlite <path to database file><br>
<br>
This will drop you into the sqlite> prompt from where you can perform any SQL queries you want.<br>
<br>
Step 3 - You will need to download MySQL, follow this video tutorial with the deviations below<br>
https://www.youtube.com/watch?v=6xs6-eegIHA&t=19s<br>
<br>
Deviations:<br>
- At 1:22 he will select what MySQL products to download. Ignore what specific products he chooses and download the following<br>
   - MySQL Server Version 8.0.33<br>
   - MySQL Workbench Version 8.0.33<br>
   - MySQL Shell Version 8.0.33<br>
   - Connector/Python Version 8.0.33<br>
   - The Architecture for all of these products are X64<br>
<br>
- At 3:23 he will set the root password as: root<br>
- DO NOT set the root password as root<br>
- Set the root password as: legacyserverwhen<br>
- Or modify the code and add another user to your MySQL database just for this program<br>
<br>
Step 4 - You will need to type:<br>
    pip install pymysql<br>
    Into your Python Command terminal in Visual Studio Code<br>
<br>
Step 5 - You will need the following VSCode Marketplace Extensions<br>
   - Pylance by Microsoft<br>
   - Python by Microsoft<br>
   - SQLite by alexcvzz