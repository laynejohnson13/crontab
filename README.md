# crontab


1. Create a new GitHub repo called *crontab*
2. Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters:

* One should pull down data from an API once a day (don’t care about what time)
* One should pull down data every Sunday night at 10:00pm
* And another one (?) should pull down data at the end of every quarter

Report the appropriate cron job command (like in page 12 of this presentation) within the GitHub repo within the markdown file

So repo should contain two files:

- markdown file (.md) with instructions for how the python files were automated using crontab
- a python file (.py) that contains the python code for pulling down the data /// the retrieved data should then be saved locally on that machine where the cron job is running - e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10-10.csv)
