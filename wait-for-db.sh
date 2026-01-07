#!/bin/sh
# wait-for-db.sh
# Wait until MySQL is ready before running commands

set -e

# First argument is the host, rest is the command to run
host="$1"
shift
cmd="$@"

# Loop until MySQL is ready
until mysql -h "$host" -u root -e "SELECT 1"; do
  echo "Waiting for database at $host..."
  sleep 2
done

# Run the command
exec $cmd
