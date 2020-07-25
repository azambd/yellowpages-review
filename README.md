yellowpages.com Review Basic scraper
=====================================

### About

Spider built with [Scrapy](http://scrapy.org/). Scrapes/Extract Reviews from [yellowpages.com](https://www.yellowpages.com/dayton-oh/mip/the-original-pancake-house-17684150) and gets all review with relevant basic information available of this YP Profile. From here it is possible to get results into `csv`, `json` and `xml` files that Scrapy can generate.

Export in CSV file, use this command
```
scrapy crawl yp_reviews -o sampleDataYp.csv
```
Export in JSON file, use this command
```
scrapy crawl yp_reviews -o sampleDataYp.json
```
> Further scope is develop pipelines and to add back-end SQL DB tables [ Example: `master_reviews` & `master_surveys` ] OR MongoDB and Log files in "logs" folder , log info table to track activities in `log_history` table, email notification etc features can be added.

### Data fields
+ name
+ total_review
+ ratings
+ reviewer_name
+ reviews
+ review_date
+ hash_key
+ sourceURL

### Installation and Running
```
git clone https://github.com/azambd/yellowpages-review.git
cd yellowpages
scrapy crawl yp_reviews
```
### Folder Structure
```
→ tree -l -v
.
├── LICENSE
├── README.md
├── sampleDataYp.csv
├── sampleDataYp.json
├── scrapy.cfg
└── yellowpages
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── __init__.py
        └── yp-reviews.py

2 directories, 12 files

```
### Note

If you need any help to upgrade this spider to a production version, shoot an email at [azam@wscraper.com] - I'll help you.
