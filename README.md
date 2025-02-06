# feedbackup
Backup the Turf-API takeovers

Due to the fact that the TurfAPI only returns takeovers taken the last 15 minutes
it is important to have full redundancy of the takeovers to be sure you don't miss out on any takeovers.

This is a fully plug and play dockerized solution that with a minimum of configuration
should get your takeovers safe in no time.

## Installation
Just clone the repository and modify the values in the .env file

### Configuration
In the project root create a .env file with the following environment variables and your own values for passwords
```
DB_ROOT_PASSWD=yourSecretPasswordForDBRoot
DB_USER_PASSWD=yourSecretPasswordForDBUser
```
The .env file is of course ignored by git

### Running
Then run `docker compose up`
