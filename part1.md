# Project 1, Part 1

* Assigned: 1/21
* Due: 2/4 beginning of class, hard copy
* worth 25% of overall Project 1 grade

In Part 1, you will propose an interesting web application of your choosing,
that will be the basis of the rest of Project 1.  You will design the entity-relationship diagram
and schema of the database, and do some setup for Part 2.

These directions are long, but please read them carefully before you start.

**Note**: If you observe holidays that overlap with this part of the project, please email the instructor to arrange for alternative deadlines.

* [FAQs](#frequently-asked-questions)
* [Project overview: Read this carefully before starting](http://github.com/w4111/project1)
* [IA Meeting Signup Link](https://calendar.google.com/calendar/selfsched?sstoken=UU43X2NkLTFneDNifGRlZmF1bHR8NmZmOTM3Mjc4ZmI4OTgzODFkMzcwZjM3YTBhOTA0YmE): Meet as a team to discuss the project with an IA. We want to make sure the scope is appropriate. Please make sure you have completed Step 1 below before your meeting.


# Overview 

This assignment consists of multiple steps.  At a high level, you will

1. Find a team mate -- go make new friends! (Or [post on Piazza](https://piazza.com/class/ijk4fyuhr8v38q?cid=5))

1. Select an application and write a short proposal.

1. Meet with a course staff member as a team to get feedback on your proposal: [Signup Link](https://calendar.google.com/calendar/selfsched?sstoken=UU43X2NkLTFneDNifGRlZmF1bHR8NmZmOTM3Mjc4ZmI4OTgzODFkMzcwZjM3YTBhOTA0YmE)

1. Revise your proposal, and create the entity-relationship diagram and schema for the database.


If you're having trouble thinking of an application, take a look
at any pretty much any web site. They all have a similar
themes and can be reduced to an appropriate scope for the project.  
For example, social networks (e.g., instagram, reddit, twitter), e-commerce (e.g., overstock,
etsy, amazon), or content sites (e.g. The New York Times, Yahoo Finance) can all work.
For example, shopping websites usually have products, users, orders, shopping carts etc.

You will ultimately submit the following as hard-copies:

1. **Required** Application Proposal

  * Describe the general "domain" of your application, construct an Entity-Relationship
  diagram, and map it to a relational schema using the mapping technique 
  that we will cover in class. 

  * Pick an application with a schema that is relatively substantial, but not too large. 
    * E/R design should have ~5-10 entity sets and a ~5-10 relationship sets. 
      You will get a sense if your design is too simple or too complex as diagram it.
      Discuss this with a TA during your advising session if you are in doubt.

    * Try to make your application interesting, including a variety of different kinds of attribute 
      domains (e.g., strings, integers, etc.) and relationships with different key and 
      participation constraints.

  * Include as many relevant constraints for your application from the 
    real world as possible in your E/R diagram.

1. <a name="contingency"></a> **Optional but strongly recommended: Contingency plan for two-person teams**:
  Since students may drop classes, and to prevent last-minute surprises, we suggest that you 
  write a "contingency plan" in case a team-mate drops the class  later in the semester. 

  * The contingency plan should indicate how you will make the project simpler, so that it is appropriate for a single person to complete. 

  * As general guidelines, your ER design for a one-person project should have around 3-7 
    entity sets and 3-7 relationship sets.

  * If your team-mate drops the class, rather than finding a new team-mate,
    you will complete the "downgraded" version of your original project. 

  * **If you choose not to submit this plan when you submit Part 1 and your team-mate drops the class later, you will have to complete the original project. No exceptions will be made at that point.**



## Step 1: Prepare for meeting with course staff

1. Find a team-mate. There's no need to notify us about your team. You will simply indicate who your team-mate is when you submit Part 1.

1. You will use Azure virtual machines to work on and deploy the project. If your team doesn't have a machine that can `ssh` to Azure, get a CS account.

1. Decide on an application for your project and write an informal one-paragraph description of the application (less than 20 lines). Highlight interesting and challenging parts. The more concrete your written description, the more efficient and useful the meeting with the class staff will be. This paragraph should include:

  1. A high-level description of the general domain of the application. 

  1. Examples of entities and relationship sets, attributes and constraints you will have.
    This does not to be final, but will make your meeting with the staff substantially better and is strongly
    encouraged.

  1. What data you will use to populate your database.

  1. Provide details about how users will interact with the site. 
    For example, if your website is based on the Internet Movie Database, 
    your description might describe the general "entities" that are involved, 
    and what types of operations users can perform (e.g., find the actors for a movie,
    add new movies, etc).

  1. Write a short description of your contingency plan (see above).
 
 
# Step 2: Revise and complete Part 1
 
1. Meet with a TA or the instructor during the week of January 25th-29th to discuss your design and make sure that it is appropriate (i.e., challenging enough, but not unrealistically so). 
    * This 10 minute meeting is required.
    * We will have expanded office hours during that week.
    * It is better if both team members can attend, but it is acceptable if only one can make it.
    * Bring two copies of the written materials for yourself and the staff.
    * **It is a good idea to come earlier in the week.**  If you choose to come later and it is too crowded, then you will be unhappy.

1. After a TA or the instructor has approved your proposal:
    * Modify the description based on the feedback.
    * Draw the ER diagram with as many of the real-world constraints for your application as possible. 
    
1. Map your E/R diagram into a relational schema in SQL, preserving the constraints.

1. Submit a hard copy of the following on the due date:
    1. Revised one-paragraph description of the application
    2. Entity-relationship diagram
    3. Resulting SQL schema
    4. Revised contingency plan (optional)
 
1. Keep a copy of all these materials for yourselves, since you will need them for Parts 2 and 3 of the project.


# Grading

Your grade will be split as follows:

* Meeting with class staff: 7 points.

  * If you come to the meeting prepared with your written description, you can expect to get all points, even if you are asked to  make changes or revisions to your proposal.

* Quality of final one-paragraph description of your application: 6 points.

   * We will evaluate the overall quality of your final hard-copy one-paragraph description of your application, including how thoroughly you incorporated any revisions suggested during your meeting with the staff.

* Quality of E/R diagram: 6 points.

    * We will evaluate how well your E/R diagram models your proposed application, including how well you modeled any relevant real-world constraints.

* Quality of your SQL schema: 6 points.

    * We will evaluate how well you mapped your E/R diagram, including constraints, into a SQL schema using the technique that we covered in class.


# Frequently-Asked Questions
<a name="faq"></a>

* I have an idea that requires that I work alone. Can I?
    * No, sorry. Please modify your project idea so that it becomes appropriate for a two-person team. Yes, being forced to work with others is sometimes painful, but I believe that some of the most valuable lessons you learn in University are not the course content.

* Can we have a team of 3, 4, or 12 students?
    * No, sorry. For fairness and to make it possible for us to grade them, the projects need to have similar size and scope.

* Can I use my favorite DBMS instead of PostgreSQL?
    * No, sorry.  We would like to be more flexible but don't have the staff to handle several diverse systems and platforms.

* Can I use Ada (or something that's not Python) for Option 3?
    * No, sorry. Please see the answer to the previous question.
