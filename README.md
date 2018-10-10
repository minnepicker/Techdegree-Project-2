# Techdegree-Project-2

You have volunteered to be the Coordinator for your town’s youth soccer league. As part of your job you need to divide the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have played soccer before, and their guardians’ names. You'll take a list of these children, divide them into teams and output a text file listing the three teams and the players on them. There are three main tasks you'll need to complete to get this done:
In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type so that it can be used in the next task.
Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team should also be the same.
Finally, the program should output a text file named -- teams.txt -- that contains the league roster listing the team name, and each player on the team including the player's information: name, whether they've played soccer before and their guardians' names.
To complete each part of this project, use ONLY the concepts and techniques we have covered in the courses so far.

* Before you start *

To prepare for this project you'll need to make sure you complete and understand these steps.

Have a GitHub account and know how to create a new repository and upload files to it. As with the previous projects, you'll submit your finished working using GitHub.
If you need a reminder on how to use GitHub and GitHub desktop to create a new repository check out the workshop 'Share Your Projects wIth GitHub Desktop' in the Project Resources, or the GitHub in Workspaces Workshop.
Download the supplied CSV file -- soccer_players.csv by clicking the Project Files link on this page. This file contains the players' information.
Read the instructions carefully - we suggest twice, at least.
Download the player data spreadsheet.
You’ll certainly need your computer to complete the project, but you may want to begin by sketching out your ideas/code with a pencil and paper.

* Project Instructions *

To complete this project, follow the instructions below. If you get stuck, ask a question on Slack or in the Treehouse Community.

Create a script named league_builder.py.
Make sure the script doesn't execute when imported; put all of your logic and function calls inside of an if __name__ == "__main__": block.
Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors. Make sure the teams have the same number of players on them, and that the experience players are divided equally across the three teams.
Create a text file named teams.txt that includes the name of a team, followed by the players on that team. List all three teams and their players.
In the list of teams include the team name on one line, followed by a separate line for each player. Include the player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each bit of player information by a comma. For example, the text file might start something like this:
Sharks
Frank Jones, YES, Jim and Jan Jones
Sarah Palmer, YES, Robin and Sari Washington
Joe Smith, NO, Bob and Jamie Smith
Before you submit your project for review, make sure you can check off all of the items on the Student Project Submission Checklist. The checklist is designed to help you make sure you’ve met the grading requirements and that your project is complete and ready to be submitted!
If you are stuck on how to get started with this project, have a look at the Project-01 Study Guide.

* Extra Credit *

To get an "exceeds" rating, you can expand on the project in the following ways:

Create 18 text files ("welcome" letters to the players' guardians). You'll create 1 text file for each player. Use the player’s name as the name of the file, in lowercase and with underscores and ending in .txt. For example, kenneth_love.txt.
Make sure that each file begins with the text "Dear" followed by the guardian(s) name(s). Also include the additional required information: player's name, team name, and date & time of first practice.
NOTE:
To get an "Exceeds Expectations" grade for this project, you'll need to complete each of the items in this section. See the rubric in the "How You'll Be Graded" tab above for details on how you'll be graded.
If you’re shooting for the "Exceeds Expectations" grade, it is recommended that you mention so in your submission notes.
Passing grades are final. If you try for the "Exceeds Expectations" grade, but miss an item and receive a “Meets Expectations” grade, you won’t get a second chance. Exceptions can be made for items that have been misgraded in review.
