## Data Collection

For all venues, I need a dataframe consisting of 
- Venue Name
- Venue Location Lat & Long
- Show Title
- Show Date
- Ages (if available), don't worry if not


whole architecture re-runs a random amount of time offeset from 6am and from 6pm
site wide refresh, whole site is like a composed view that twice daily re-gens itself

### Multi-Venue Sites
- Live Nation (the great satan himself)
  - https://www.livenation.com/search?q=calgary#venue
- Calgary Theatre
  - https://www.calgary-theatre.com/theaters/southern-alberta-jubilee-auditorium/theater.php
- SongKick
  - https://www.songkick.com/metro-areas/27359-canada-calgary  
- ShowPass
  - https://www.showpass.com/discover/calgary/highlights/
- Eventbrite
  - https://www.eventbrite.ca/d/canada--calgary/calgary/?page=2
- JamBase
  - https://www.jambase.com/venues
- Bandsintown


### Sites Per Venue
- The Palace Theatre
  - https://www.thepalacetheatre.ca/events
- Modern Love
  - https://www.ticketweb.ca/venue/modern-love-calgary-ab/539955
- Arts Commons/Jack Singer
  - https://www.artscommons.ca/whats-on
- Palomino
  - https://thepalomino.ca/live-events/
- Dickens
  - https://www.songkick.com/venues/719611-dickens/calendar
  - https://www.ticketweb.ca/venue/dickens-pub-calgary-ab/213154
  - https://www.eventbrite.ca/o/dickens-22927194740
- The Blues Can
  - https://www.thebluescan.com/Events.php
- Festival Hall
  - https://www.calgary-theatre.com/theaters/calgary-folk-music-festival-hall/theater.php
- Commonwealth
  - https://www.commonwealthbar.ca/events
- Cowboy's
  - Looks like a ShowPass shop
- Cafe Gravity
  - Songkick has some Gravity
- King Eddy
  - https://kingeddy.ca/whats-on/
- Ranchman's
  - https://www.ranchmans.ca/events/calendar/category/ticketed-events/
- Whisky Rose
  - https://whiskeyrosesaloon.com/events/
- Bella Concert Hall
  - https://tickets.mru.ca/performancelisting.asp?venuename=Bella+Concert+Hall&venue=2
- Grey Eagle
  - https://www.greyeagleresortandcasino.ca/events/
  - 
- Mac Hall
  - https://www.machallconcerts.com/event/
  - https://www.livenation.com/venue/KovZpaKVpe/macewan-hall-events
- Southern Alberta Jubilee Auditorium
  - https://www.jubileeauditorium.com/calgary/whats-on
- Knox United
  - SongKick, EventBrite should catch these
- Studio Bell
  - https://www.studiobell.ca/whats-on
- Back Alley
  - https://backalleycalgary.com/event-dates/
- Rated Ultra Lounge
  - https://www.ratedultralounge.com/events'
- Sub Rosa
  - https://www.subrosayyc.com/news/
- Fort Calgary
  - EventBrite, SongKick
- Idle Eyes Collective
  - https://www.eventbrite.ca/o/idle-eyes-collective-58363715063
- Mikey's
  - https://www.mikeyson12th.com/events-1


- Visit every website, saving the html

- batch the visiting of every website we have into a job, collect the list of jobs, randomize the list, visit every 5 seconds

## Data Organization

- make a dictionary for each venue, where keys are a list of values that should match to the dictionary object
  - Go through unique venue names in the column of event names
    - unique venue names go into an assigned dictionary print that to a logs message, i can use that to make new mappings of venue names to in-project venue objects

## App Logic


## App Interface

## Post-Deployment Dev-Ops
- Limit traffic to 20 visits a day
  - "I don't feel like doing a more sophisticated strategy to preserve my bandwith, so we have a hard 20 per ip/deviceid/mac/whatever per day cutoff"

