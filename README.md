# feedbackup
Backup the Turf-API takeovers

Due to the fact that the TurfAPI only returns takeovers taken the last 30 minutes
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

## readfeed
This service is responsible for reading the takeovers from the Turf API feed endpoint and store them in the local database.
The table for storing the takeovers consist of three columns:
- takeover_time **PK**
- zone_id **PK**
- original_takeover

The original_takeover is the json for this takeover in original format

This service polls the Turf API once a minute

## exportfeed
To be able to read from this backup and make any use of it there are one endpoint `/feed` who take an optional queryparam `after`

If no queryparam is provided it starts with the oldest takerover

The queryparam `after` represents a datetime and specifies to return takeovers after that specified time.
The datetime should be formatted according to ISO 8601

An example
```
http://localhost:8000/feed?after=2025-02-06T13:39:31
```

The response is a json list following the same format as the official Turf API but with **one big difference**.
The takeovers are ordered in natural order according to takeovertime. 
So it begins with the takeover that is closest to the time you specified and continues with takeovers taken later.

It returns 1000 takeovers at most, but two make sure all takeovers for a particular second is returned in one go it can be fewer.

### Usage
This endpoint serves two basic use cases:
- Regular polling
- Catch up missing takeovers

#### Algorithm for Regular polling
- retrieve from your database the takeovertime of your latest takeover
- call endpoint `/feed` with `after` set to that datetime
- save all the takeovers in the response
- save the takeovertime from the last returned takeover in your database
- wait for a minute or so and start from the beginning


#### Algorithm for Catch up missing takeovers
More or less equal to the algorithm above but just adjust the waiting time until the endpoints starts returning
a small amount of takeovers which tells you that you are back on track 


## importfeed - Not implemented yet
More of an admin endpoint that serves the purpose to populate the database with older takeovers taken from an external source 


