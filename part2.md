# Project 1, Part 2

* Assigned: 2/11
* Due: 2/25 8:40AM Electronically
* Value: 25% of Project 1 grade


In this part of the project, you will revise your design based on the staff's feedback on [part 1](./proj1.md). You will implement the database tables (including all constraints), populate the database, and write some queries.

* [Project overview](./README.md)
* If your teammate has dropped the class, [see the contingency plan](./README.md#contingency)
* For any questions about collaboration, [see the Syllabus](http://github.com/w4111/syllabus#cheating)
* If there are questions of general interest, please post to Piazza.


# Logistics

Project mentor

* The TA that graded your part 1 will be your project mentor for the rest of your project -- 
  this is likely the TA that you discussed part 1 with.  He or she will be your main contact for 
  the project, though the rest of  the staff are of course available for questions or concerns.

Azure Pass

* Get an azure pass code from [the google spreadsheet](https://docs.google.com/spreadsheets/d/1nsDzE5HYoWpef5Z6uCKz6xrraoJgg0scI9wJJfTYUeo/edit#gid=0)
* Go to [https://www.microsoftazurepass.com/](https://www.microsoftazurepass.com/) and fill out the information


Computing and Databases

* We recommend that you create a new Azure VM using the new Azure Pass subscription, and go through the same setup process in [homework 0](http://github.com/w4111/hw0). You can then use this new VM to complete the assignment and all future assignments that require a VM. This is a relatively easy way to switch from the Free Trial subscription to the Azure Pass subscription. There is a [method](http://blogs.msdn.com/b/laurelle/archive/2015/10/01/how-to-move-azure-vm-between-subscriptions.aspx) that allows you to transfer your Free Trial VM from hw0 to the new subscription, but it can be more work than simply creating a new one. Note that when creating your new VM, be sure to choose the Azure Pass subscription instead of the Free Trial one. Otherwise the VM won't be accessible once your Free Trial expires.
* You are welcome to setup PostgreSQL on your VM, or use the databases that the staff 
  is running for you.  Instructions at [setuppostgres.md](https://github.com/w4111/project1/blob/master/setuppostgres.md).

# Procedures

Preliminaries

1. Pick up your graded Part 1 starting on **2/11**, and revise your design based on its feedback.
  * You will be graded based on how well you addressed the project mentor's comments. 
    In general, listen to your project mentor's suggestions.
2. Familiarize yourself with the [PostgreSQL documentation](http://www.postgresql.org/docs/9.3/interactive/index.html)!
   We will use PostgreSQL 9.3 (the minor version .3 doesn't matter so much).


Make the database

1. Connect to your database (only one team member needs to do this database part)
  * `ssh` into your azure machine (recall [HW0](http://github.com/w4111/hw0))
  * connect using `psql` 

          psql -U <your uni> -h w4111db.eastus.cloudapp.azure.com

  * it will ask for your password.  Your password should have come back with your graded project 1 part 1.  If not, send us a private piazza message.
  * if the database cannot handle the number of connections, we may create a second database server (we will let you know!)

1. Create the SQL tables based on your revised schema.
  * include all key, type constraints
  * the PostgreSQL documentation for [CREATE TABLE](http://www.postgresql.org/docs/9.3/static/sql-createtable.html)
    and [data types](http://www.postgresql.org/docs/9.3/static/datatype.html) may help

1. Create the CHECK constraints that you need to express the rest of your real-world constraints.
  * Note: PostgreSQL's CHECK constraints are limited ([see the documentation](http://www.postgresql.org/docs/9.4/static/ddl-constraints.html)), so do what you can.
  * Note: PostgreSQL doesn't support CREATE ASSERTION statements. but does support triggers.
    However, you are not required to implement constraints that require triggers

Populate the tables

1. Insert at least 10 realistic/real tuples into each table in your database.
  * This should be based on your description in part 1

Run some queries

1. Run 3 interesting queries.
   The three queries, together, should include multi-table joins, WHERE clauses, and aggregation (e.g. COUNT, SUM, MIN, etc). Each
   query does not need to include all of those SQL features.



# Submission
<a name="submit"></a>

Since you created the database on the course database machine, we have access to your database and populated tables, so you are almost done!

Go to [the google docs form](https://docs.google.com/a/columbia.edu/forms/d/1bHF3wnlPJIMMPtOh6GV18uhnQFvV75BGy6W2i3BkTp8/viewform?usp=send_form) and fill it out.  
You can edit your submission until the due date (be careful, since if you submit afterwards it will be counted as late).  
We will use the google docs submission timestamp.

Finally, turn in the _graded_ ER diagram from part 1 at the beginning of class (this is part of the assignment, so late days will be in effect).

<!--

1. Create a folder named `<YOUR UNI>-proj1part2`, where `<YOUR UNI>` is replaced with the UNI of one teammate 
   e.g., `ew2493-proj1part3` for the Prof Wu.

1. If your ER diagram is in electronic form, gereate a PDF and place it into your directory.

1. Export your database into a file called `database.ddl` and put the file into your directory

        pg_dump -f database.ddl -h <YOURHOST> -U <YOURUSERNAME> <DATABASE>

        # for example
        pg_dump -f database.ddl -h localhost -U eugenewu mydatabase

1. create a file named `queries.txt` and put it into your directory
    * The file contains three interesting queries and their descriptions.  
      The three queries, together, should include multi-table joins, aggregation, WHERE clauses (each
      query does not need to include all of those SQL features).
   
    * The format of the files should be exactly one (possibly long) line of description 
      followed by exactly one (possibly long) line of SQL query, and so on.  For example

          this is a description for query 1
          SELECT * FROM foo join bar on foo.id = bar.id
          this is the second description for query 2
          SELECT 1
          this is the third description
          SELECT 0

1. create a file named `teammates` and put it in your directory
    * The file contains the teammates' UNIs, one per line.  For example

          ew2493
          zz1234

1. `tar`, `gzip`, or `zip` your directory

1. Submit the compressed file on courseworks under "Project 1, Part 2"

-->



# Grading 
<a name="grading"></a>

Grading depends on the following:

* how well you incorporated your mentor's feedback (important)
* Quality of the SQL schema and implementation:  how well it conforms with the ER diagram and constraints
* Your SQL statements: are they reasonable application queries and do they use the SQL features as requested?
* Quality of the data: is it realistic?  


