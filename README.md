# Expense-Tracker

## Importance
We have daily expenses, from groceries to clothing to bills. There are so many expenses that it’s normal to lose track of them and keep spending till we’re almost out of cash. A tracker can help people watch their expenses.

This is where the expense tracker comes in. An expense tracker is a software tool that allows users to keep track of their expenses. It can also analyze the expenses, depending on how advanced it is, but let’s keep it simple for now.

With the expense tracker, users can set a budget and track their spending so as to make better financial decisions.

## Technical Details
The main objective of this project is to keep track of the user’s expenses. Some statistical analysis has to be done to be able to give users correct information on their expenses and help them spend better.

While tracking the expenses is the key thing, a good interface is also important. With PySimpleGUI, you can create a unique interface to improve the experience of the users.

PyData libraries such as pandas and matplotlib can be helpful for building the expense tracker.

The pandas library can be used for the data analysis, and the matplotlib library can be used for plotting graphs. Graphs will give the users a visual representation of their expenses, and a visual representation is usually easier to understand.

The application will receive data from the users. The data here is the inputted expenses. So, you’ll have to store the expenses in a database. The SQLite database is a good database choice for this project since it can be set up quickly. You can use sqlite3 module for the SQLite database.

## Extra Challenge
For your users to benefit from this project, they’ll have to input their expenses regularly, which might slip their mind. It could be useful for you to implement a reminder feature. So the application will send a notification at certain times of the day or the week, reminding them to make use of the expense tracker.
