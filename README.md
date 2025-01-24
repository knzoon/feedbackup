# feedbackup
Backup the Turf-API takeovers

Due to the fact that the TurfAPI only returns takeovers taken the last 15 minutes
it is important to have full redundancy of the takeovers to be sure you don't miss out on any takeovers.

This is a fully plug and play dockerized solution that with a minimum of configuration
should get your takeovers safe in no time.

## Installation
Just clone the repository and modify the values in the .env file

Then run `docker compose up`
