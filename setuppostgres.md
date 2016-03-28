# Setup Help

THis document describes ho to setup your own postgresql server on Azure and connect to the staff 
database.


## Setting up your own PostgreSQL

These instructions are for setting up PosgreSQL locally on your Azure VM 
after following the [HW0](../../hws/hw0/README.md) instructions.
Part of these instructions are to make setup easy for you and not for
setting up the most secure deployment.
Also, if you try these instructions anywhere else (e.g., your laptop), all bets are off!

1. **Stop postgres** It turns out `apt-get` automatically starts postgresql under the
   user `postgres`, so let's kill that

        sudo -u postgres bash -c 'killall postgres'

1. **Set environment variables** PostgreSQL stores its database files
   in a directory and is connected to through a _port_.  
   We will define this information in `~/.bashrc`.
   The file contains a bunch of gooblygook, don't worry about it and
   add the following to the top of the file:

        # this goes into ~/.bashrc
        export PGDATA=/home/<YOUR USERNAME>/pgdata
        export PGPORT=5432

        # this makes sure the installed posgresql tools are available in the shell 
        export PATH=/usr/lib/postgresql/9.3/bin:$PATH

   All of its environment variables are in the [documentation](http://www.postgresql.org/docs/9.3/static/plpython-envar.html)

1. reload your bashrc file:

        source ~/.bashrc

1. We now need to allocate the files that PostgreSQL will use into the
   `$PGDATA` directory. 

        initdb -D $PGDATA

1. Check that the directory has been created

        ls $PGDATA

1. By default, the client `psql` program communicates with the
  PostgreSQL backend using OS sockets.  This can be annoying
  for connecting remotely, so let's change it to use TCP instead.
  Edit `$PGDATA/postgresql.conf` at aronud line 59 from:

  
        #listen_addresses = 'localhost'         # what IP address(es) to listen on;
                                                # comma-separated list of addresses;
                                                # defaults to 'localhost'; use '*' for all
                                                # (change requires restart)
        #port = 5432                            # (change requires restart)

  by uncommenting the two options:

        listen_addresses = 'localhost'         # what IP address(es) to listen on;
                                                # comma-separated list of addresses;
                                                # defaults to 'localhost'; use '*' for all
                                                # (change requires restart)
        port = 5432                            # (change requires restart)

1. PostgreSQL makes sure that only one server can run for a given
   port by creating a special lock file in `/var/run/postgresql/`.
   We should make sure we own it so that our postgresql process can
  write to the directory

        sudo chown -R <YOURUSERNAME> /var/run/postgresql
 
1. OK, now we're ready to start the DBMS backend!

        pg_ctl start

   You should see output like:

        LOG:  database system was shut down at 2015-08-20 22:45:28 UTC
        LOG:  MultiXact member wraparound protections are now enabled
        LOG:  database system is ready to accept connections
        LOG:  autovacuum launcher started

### Create and connect to the database

1. So far, we have gotten a DBMS to run, but we need to create some databases.
  The following will create a database named `test`

        createdb test

1. `psql` is the PostgreSQL client program.  Lets use it to connect to our new database:

        psql test

   You should see the psql prompt:

        psql (9.3.9)
        Type "help" for help.

        test=# ^D\q

1. Type a simple query to see that it really works!
   (queries need to be ended with a `;`)

      SELECT 1;



## Connect to staff database

The staff is running several database instances on Amazon, and if you have completed
hw0, then you should have an account on these databases.  

You can connect to any of them using the following `psql` command:

        psql -h w4111db.eastus.cloudapp.azure.com –U <YOUR UNI>  -W w4111

That's it!  Try it out
