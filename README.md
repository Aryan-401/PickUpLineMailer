# Pickup Line Emailer

* Pretty self-explanatory.
* Uses the [Pickup Line API](https://getpickuplines.herokuapp.com) to get a random pickupline everyday
* Email is sent at required time using Windows Task Scheduler (or cron on Linux)

# Environment Variables

* <b>EMAIL </b> : Personal Email Address
* <b>PASSWORD</b> : Password of Email Address mentioned in `EMAIL`
* <b>LUCKY_GUY</b> : Email Addresses seperated by commas to whom you want to send the pickup lines to
* <b>SECONDARY_EMAIL</b> : An additional Recipient who will be BCC-ed


NOTE: Google will no longer Less Secure Means of Logging in Gmail from 30th May 2022. This program will not work then.