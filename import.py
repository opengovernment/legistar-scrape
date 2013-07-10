from legistar.scraper import LegistarScraper
from legistar.config import Config, DEFAULT_CONFIG
import pymongo
import datetime

# Configure and create a scraper

config = Config(
  hostname = 'phila.legistar.com',
).defaults(DEFAULT_CONFIG)
scraper = LegistarScraper(config)

# connect to a mongo DB
# http://api.mongodb.org/python/current/tutorial.html
from pymongo import MongoClient
client = MongoClient()
db = client.opengovernment_local


# -----------------Agendas---------------------

# Example agenda object returned from the scraper
# {
#   u'Meeting Date': {
#     'url': u'javascript:void(0);', 
#     'label': datetime.datetime(2013, 6, 20, 0, 0)
#   }, 
#   u'Meeting Time': u'9:00 AM', 
#   u'Name': u'Committee of the Whole', 
#   u'Meeting Location': u'Room 400', 
#   'fulltext': 'Public Hearing NoticeCity of PhiladelphiaThe Committee of the Whole of the Council of the City of Philadelphia will hold a Public Hearing on Thursday, June 20, 2013, at 9:00 AM, in Room 400, City Hall, to hear testimony on the following items:Resolution appointing Mjenzi Traylor to the Board of Directors of the Germantown Special Services District of Philadelphia.130504Resolution appointing Matt Canno to the Board of Directors of the Germantown Special Services District of Philadelphia.130505Resolution appointing Joseph Martin to the Board of Directors of the Germantown Special Services District of Philadelphia.130506Resolution appointing Joseph Waldo to the Board of Directors of the Germantown Special Services District of Philadelphia.130507Resolution appointing Joseph Corrigan to the Board of Directors of the Germantown Special Services District of Philadelphia.130508Resolution appointing Greg Peil to the Board of Directors of the Germantown Special Services District of Philadelphia.130509Resolution appointing Barbara Hogue to the Board of Directors of the Germantown Special Services District of Philadelphia.130510Copies of the foregoing items are available in the Office of the Chief Clerk of the Council, Room 402, City Hall.Immediately following the public hearing, a meeting of the Committee of the Whole, open to the public, will be held to consider the action to be taken on the above listed items.Michael DeckerChief ClerkCity of Philadelphia- 1 -\x0c', 
#   u'Agenda': {
#     'url': u'View.ashx?M=A&ID=248602&GUID=2D23A8B0-4FB3-4EF2-A957-C6FD8FF9BDAA', 
#     'label': u'Agenda'
#   }, 
#   u'Minutes': u'Not available'
# }

# get a handle on the collection
council_agendas = db.council_agendas

print 'clearing out existing agendas'
council_agendas.remove({"Municipality": "Philadelphia"})

# get all agenda items
agenda_list = scraper.councilCalendar('all')

for event in agenda_list:
  event['Municipality'] = 'Philadelphia'
  event['Created Date'] = datetime.datetime.utcnow()
  event['Updated Date'] = datetime.datetime.utcnow()

  council_agenda_id = council_agendas.insert(event)
  print 'saving', event['Meeting Date'], council_agenda_id