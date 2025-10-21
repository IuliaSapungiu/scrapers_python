# This repository contains Python-based web scrapers developed for PeViitor.ro
###### This website is a Romanian job aggregation platform. The scrapers are integrated into PeViitor’s internal data collection system and are not intended for standalone execution.

### Project Overview
Each scraper programmatically extracts structured job data (such as job title, location, company, and link) from individual company career pages and outputs it in a JSON format compatible with PeViitor’s ingestion pipeline. These scrapers automate the process of gathering job listings across multiple Romanian employers, ensuring that PeViitor’s platform remains accurate, up-to-date, and data-consistent.

The data collection process involves sending HTTP requests, parsing HTML structures, handling dynamic content when necessary, and normalizing the extracted data before submission to PeViitor’s internal database.

### Technologies
Developed using:
  - Requests – HTTP requests to fetch webpage content
  - BeautifulSoup – Parsing and extracting data from HTML
  - Selenium – Handling dynamic content loaded via JavaScript
  - Postman – Testing API endpoints for integration 

### Features and Functionality

- Error handling → your code catches exceptions like requests.exceptions.RequestException, handles 404 pages, or skips missing elements.
- Standardized schema → all your scrapers output JSON with the same field names (e.g. company, job_title, location, link).
- Automated normalization → you clean/standardize data (e.g. trimming spaces, formatting locations).
- Integration hooks → your script sends or saves data directly into PeViitor’s system (e.g. through an API call or shared directory
