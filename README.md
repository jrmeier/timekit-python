# Timekit Python wrapper

This is an unofficial Python wrapper of the Timekit.io REST API, here's the offical documentation https://developers.timekit.io/reference.
Many features are still missing, feel free to submit a pull request and add what you need!

## Missing Features
 * Dynamic Includes
 * Booking Graphs
 * Calendars
 * Events
 * Booking actions in Bulk

## Requirements
* Python 2.7 or higher, this was written with 2.7 and not tested with anything else 
* AppToken from Timekit
* [requests](http://docs.python-requests.org/en/master/) - v 2.18.4
* tzlocal - v 1.5.1


## Installation
Since this isn't hosted on PyPy yet, clone this [repo](git@github.com:jrmeier/timekit-python.git).

Step 1.

 ```sh
  cd ./timekit/python 
  ```

 Step 2.
Install the requirements

 ```python
 pip install -r requirements.txt
 ```

 
 ## Code Examples

## Resource

 ```python
 from timekit import Resource

app_token = 'YOUR_APP_TOKEN'
client = Resource(app_token)

# create a resource, returns the resource object with metadata
# there are many attributes that can be added, see the offical documenation for more details
new_resource = {
    'name': 'Resource Name'    
}
resource = client.create(new_resource)

# returns an object with all the resources and some metadata
client.list()

# update a client, email cannot be modified after creation, returns True
resource_id = resource['id']
client.update(resource_id, name='Mark Zuckerburg')

# delete a resource. returns True
client.delete(resource_id)
```


## AppClient

 ```python
 from timekit import AppClient

app_token = 'YOUR_APP_TOKEN'

client = AppClient(app_token)

# get the current application info
client.get_current_app()

# invite existing resources to your app
client.invite_resources('joshm@null.net')

```
## Booking
 
 ```python
 from timekit import Booking
import datetime

app_token = 'YOUR_APP_TOKEN'

# setting this for my local UTC offset
now = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
start_time = now + datetime.timedelta(hours=1)
end_time = now + datetime.timedelta(hours=2)

# this is the booking object, check out the timekit official docs for more details
booking_obj = {
    'resource_id':'PREVIOUSLY_CREATED_RESOURCE_ID'
    'customer': {'name':'Customer Name', 'email':'customer@gmail.com'},
    'start':start_time, # since 
    'end': end_time,
    'what': 'Most important meeting',
    'description': 'This is a description of the meeting',
    'where': 'The \"where\" of the meeting',

}

# if successful, it will return a dictionary of the new booking!
client = Booking(app_token)
booking = client.create(booking_obj)

# now we can retrieve that booking
# id is a UUID
booking_id = booking['id']

# if successful, return the booking object
retrieved_booking = client.retrieve(booking_id)

# now we can confirm, decline, or cancel the booking

# returns the confirmed booking object
client.confirm(booking_id)

# returns the declined bookign objectå
client.decline(booking_id)

# returns the canceled booking object
client.cancel(booking_id)
```

## Availability

 ```python
 from timekit import Availability

app_token = 'YOUR_APP_TOKEN'

client = Availability(app_token)

# check for open times
# there's a lot of options, so check the documentaion
resource_id = 'RESOURCE_ID'

client.query(resource_id)
```

## Credentials

 ```python
 from timekit import Credentials

app_token = 'YOUR_APP_TOKEN'

client = Credentials(app_token)

# get credentials for the widget
client.widget()

# get credentials for the specific resource
client.resource('RESOURCE_ID')
```

## Calendar

```python
from timekit import Calendar
app_token = 'YOUR_APP_TOKEN'

client = Credentials(app_token)

# create a calendar
resource_id = "RESOURCE_ID"
name = 'Test Calendar Name'
description = 'Test calendar description'
client.create(resource_id=resource_id, name=name, description=description)

# list all calendars
client.list()

# get calendar by ID
client.retrieve("CALENDAR_ID")

# update calendar by ID
client.update("CALEDAR_ID", name='My new calendar name')

# delete a calendar
client.delete("CALENDAR_ID")
```

## Event

```python
from timekit import Calendar
import datetime
app_token = 'YOUR_APP_TOKEN'

# create an event
now = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
start_time = now + datetime.timedelta(hours=1)
end_time = now + datetime.timedelta(hours=2)

res = client.create(
    start = start_time,
    end = end_time,
    what = 'This is a great time',
    where = 'Your mom\'s house',
    calendar_id=calendar_id,
    resource_id="RESOURCE_ID"
)

# list all events
client.list()