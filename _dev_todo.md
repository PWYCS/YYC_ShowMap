## Data Collection

For all venues, I need a dataframe consisting of 
- Venue Name
- Venue Location Lat & Long
- Show Title
- Show Date
- Ages (if available), don't worry if not


whole architecture re-runs a random amount of time offeset from 6am and from 6pm
site wide refresh, whole site is like a composed view that twice daily re-gens itself



- Visit every website, saving the htmlgit

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

