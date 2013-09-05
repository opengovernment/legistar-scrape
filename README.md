OpenGovernment.org Legistar Importer 

Uses [Legistar Scraper](https://github.com/fgregg/legistar-scrape) - a python library for scraping [Legistar sites](http://www.granicus.com/Legistar/Product-Overview.aspx) 
-- legislation management sites hosted by by [Granicus](http://www.granicus.com/Streaming-Media-Government.aspx).

## Installation

```console
git clone git://github.com/opengovernment/opengovernment-legistar-scrape.git
cd opengovernment-legistar-scrape
pip install -r requirements.txt
```

Copy over the settings file and update with your parameters
```console
cp settings.py.example settings.py
```

## Usage

Save Council Agendas and Council Members to opengovernment_import mongo collection
```console
python import.py
```