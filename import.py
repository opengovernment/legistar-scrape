from legistar.scraper import LegistarScraper
from legistar.config import Config, DEFAULT_CONFIG
import pymongo

#__________________________________________________________________________
#
# Configure and create a scraper

config = Config(
  hostname = 'phila.legistar.com',
).defaults(DEFAULT_CONFIG)
scraper = LegistarScraper(config)

agenda_list = scraper.councilCalendar('all')

for event in agenda_list:
  print event['Name']


# connect to a mongo DB
# http://api.mongodb.org/python/current/tutorial.html

# from pymongo import MongoClient
# client = MongoClient()
# db = client.opengovernment_local

# #__________________________________________________________________________
# #
# # Get a summary listing of all of the legislation

# all_legislation = scraper.searchLegislation('')

# #__________________________________________________________________________
# #
# # Get more detail for a particular piece of legislation

# for legislation_summary in all_legislation:
#   (legislation_attrs, legislation_history) = \
#     scraper.expandLegislationSummary(legislation_summary)
#   break
# # NOTE: searchLegislation returns an iterator; you may not use subscript
# # indexing (e.g., all_legislation[0]). You may, however, achieve the same
# # thing with all_legislation.next()

# #__________________________________________________________________________
# #
# # Get details about legislation history, such as voting results

# for history_summary in legislation_history:
#   (history_detail, votes) = scraper.expandHistorySummary(history_summary)
#   print history_detail
#   print votes