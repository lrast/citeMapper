# script for setting up the server environment

# activate virtual env
source ./serverEnv/bin/activate

# location of webserver
export FLASK_APP=run

# start up the database server
pg_ctl start -D ~/Databases -l ./logs/dbLog
