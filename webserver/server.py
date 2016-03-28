#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import time
from datetime import date
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following uses the sqlite3 database test.db -- you can use this for debugging purposes
# However for the project you will need to connect to your Part 2 database in order to use the
# data
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@w4111db.eastus.cloudapp.azure.com/username
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@w4111db.eastus.cloudapp.azure.com/ewu2493"
#
DATABASEURI = "postgresql://ln2334:WTRZDC@w4111db.eastus.cloudapp.azure.com/ln2334"


#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)


#
# START SQLITE SETUP CODE
#
# after these statements run, you should see a file test.db in your webserver/ directory
# this is a sqlite database that you can query like psql typing in the shell command line:
# 
#     sqlite3 test.db
#
# The following sqlite3 commands may be useful:
# 
#     .tables               -- will list the tables in the database
#     .schema <tablename>   -- print CREATE TABLE statement for table
# 
# The setup code should be deleted once you switch to using the Part 2 postgresql database
#
engine.execute("""DROP TABLE IF EXISTS test;""")
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  name text PRIMARY KEY
);""")
engine.execute("""INSERT INTO test VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")
#
# END SQLITE SETUP CODE
#



@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print request.args


  #
  # example of a database query
  #
  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  
  #transfer contenxt to html file
  context = dict(data = names)

  return render_template("index.html", **context)

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another
#
# notice that the functio name is another() rather than index()
# the functions for each app.route needs to have different names
#
@app.route('/another')
def another():
  return render_template("anotherfile.html")

@app.route('/books')
def books():
  cursor = g.conn.execute("""SELECT r.id, r.author, b.uni, b.time FROM readings r, borrow b where r.id=b.id""")
  
  names = []
  for result in cursor:
    names.append(result[0]+ "                    " +result[1]+ "                    " +result[2])  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("""SELECT r.id, r.author FROM readings r where r.id NOT IN (Select id from borrow)""")

  for result in cursor:
    names.append(result[0]+ "                    " +result[1]+           "          available")  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = names)

  return render_template("books.html", **context)



@app.route('/suppliers')
def suppliers():
  cursor = g.conn.execute("""SELECT name, addr FROM suppliers""")

  names = []
  for result in cursor:
    names.append(result[0]+ "                    " +result[1])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = names)

  return render_template("suppliers.html", **context)





@app.route('/searchbysupplier', methods=['POST'])
def searchbysupplier():
  name = request.form['name1']
  cursor = g.conn.execute('SELECT r.id, r.author, s.name FROM readings r, add a, suppliers s where r.id = a.id and s.name = a.name and s.name = %s',name)
  names = []
  for result in cursor:
    names.append(result[0]+" "+result[1]+ " " + result[2])  # can also be accessed using result[0]
  cursor.close()
  context = dict(data = names)
  return render_template("searchbysupplier.html", **context)

@app.route('/searchallbooks', methods=['POST'])
def searchallbooks():
  name = request.form['name3']
  cursor = g.conn.execute('SELECT b.id, b.name, p1.name FROM books b, publish p1, publishers p2 where b.id = p1.id and p1.name = p2.name and b.name = %s',name)
  names = []
  for result in cursor:
    names.append(result[0]+" "+result[1]+ " " + result[2])  # can also be accessed using result[0]
  cursor.close()
  context = dict(data = names)
  return render_template("searchallbooks.html", **context)


@app.route('/searchallpapers', methods=['POST'])
def searchallpapers():
  name = request.form['name2']
  cursor = g.conn.execute('SELECT p.id, p.title, c.name, c.addr FROM papers p, accept a, conferences c where p.id = a.id and c.name = a.name and p.title = %s',name)
  names = []
  for result in cursor:
    names.append(result[0]+" "+result[1]+ " " + result[2])  # can also be accessed using result[0]
  cursor.close()
  context = dict(data = names)
  return render_template("searchallpapers.html", **context)

@app.route('/editlibrarians', methods=['POST'])
def editlibrarians():
  adminid = request.form['name4']
  adminpw = request.form['name5']
  libid = request.form['name6']
  libpw = request.form['name7']
  if len(libpw)<8:
    return render_template("tooshortpw.html")
  cursor = g.conn.execute("SELECT * FROM admin where login = %s and password = %s", (adminid, adminpw))
  print cursor.rowcount
  if cursor.rowcount==0:
    return render_template("wrongpassword.html")
  else:
    cursor = g.conn.execute("SELECT * FROM librarians where uni = %s", libid)
    if cursor.rowcount==0:
      return render_template("nosuchlib.html")
    else:
      cursor = g.conn.execute("UPDATE librarians SET password = %s WHERE uni = %s", (libpw, libid))
  return redirect('/')

@app.route('/borrowbooks', methods=['POST'])
def borrowbooks():
  libid = request.form['name8']
  libpw = request.form['name9']
  userid = request.form['name10']
  rid = request.form['name11']
  cursor = g.conn.execute("SELECT * FROM librarians where uni = %s and password = %s", (libid, libpw))
  print cursor.rowcount
  if cursor.rowcount==0:
    return render_template("wrongpassword.html")
  else:
    cursor = g.conn.execute("SELECT * FROM readers where uni = %s", userid)
    if cursor.rowcount==0:
      return render_template("nosuchreader.html")
    else:
      cursor = g.conn.execute("SELECT * FROM readings where id = %s", rid)
      if cursor.rowcount==0:
        return render_template("nosuchreading.html")
      else:
        cursor = g.conn.execute("SELECT * FROM borrow where id = %s", rid)
        if cursor.rowcount==0:
          print "borrowbooks"
          print date.today()
          g.conn.execute('INSERT INTO borrow VALUES (%s,%s,%s);', (rid, userid, date.today()))
        else:
          return render_template("hasbeenborrow.html")
  return redirect('/')


@app.route('/returnreadings', methods=['POST'])
def returnreadings():
  libid = request.form['name12']
  libpw = request.form['name13']
  userid = request.form['name14']
  rid = request.form['name15']
  cursor = g.conn.execute("SELECT * FROM librarians where uni = %s and password = %s", (libid, libpw))
  print cursor.rowcount
  if cursor.rowcount==0:
    return render_template("wrongpassword.html")
  else:
    cursor = g.conn.execute("SELECT * FROM readers where uni = %s", userid)
    if cursor.rowcount==0:
      return render_template("nosuchreader.html")
    else:
      cursor = g.conn.execute("SELECT * FROM readings where id = %s", rid)
      if cursor.rowcount==0:
        return render_template("nosuchreading.html")
      else:
        cursor = g.conn.execute("SELECT * FROM borrow where id = %s and uni = %s", (rid, userid))
        if cursor.rowcount==1:
          print "borrowbooks"
          print date.today()
          g.conn.execute('DELETE FROM borrow WHERE id = %s', rid)
        else:
          return render_template("notborrow.html")
  return redirect('/')


@app.route('/checkmyinfo', methods=['POST'])
def checkmyinfo():
  uni = request.form['name16']
  pw = request.form['name17']

  cursor = g.conn.execute("SELECT * FROM readers where uni = %s", uni)
  print cursor.rowcount
  if cursor.rowcount==0:
    return render_template("nosuchreader.html")
  else:
    cursor = g.conn.execute("SELECT * FROM readers where uni = %s and password = %s", (uni, pw))
    if cursor.rowcount==0:
      return render_template("wrongpw.html")
    else:
      names = []
      for result in cursor:
        names.append(result[0]+" "+result[1]+ " " + result[2])  # can also be accessed using result[0]
      cursor = g.conn.execute("SELECT id FROM borrow where uni = %s", uni)
      names1 = []
      for result in cursor:
        names1.append(result[0])  # can also be accessed using result[0]
      
      cursor.close()
      context = dict(data = names, data1 = names1)
      return render_template("myinfo.html", **context)

  return redirect('/')


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
