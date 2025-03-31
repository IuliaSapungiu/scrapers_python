#
#
#  Basic for scraping data from static pages
#
# ------ IMPORTANT! ------
# if you need return soup object:
# you cand import from __utils -> GetHtmlSoup
# if you need return regex object:
# you cand import from __utils ->
# ---> get_data_with_regex(expression: str, object: str)
#
# Company ---> verifone
# Link ------> https://www.verifone.com/en/global/careers/jobs?title=&departments=All&locations=686
#
#
from __utils import (
    GetStaticSoup,
    get_county,
    get_job_type,
    Item,
    UpdateAPI,
)


def scraper():
    '''
    ... scrape data from verifone scraper.
    '''
    soup = GetStaticSoup("https://www.verifone.com/en/global/careers/jobs?title=&departments=All&locations=686")

    job_list = []
    for job in soup.find_all('div', class_='view-id-jobs-content accordion__item'):
        link = job.find('a')['href'].strip()
        locatie = job.find('td', class_='views-field views-field-field-offices')
        
        if locatie:  
            locations = [loc.strip() for loc in locatie.text.split(',')]
        
            if "Bucharest" in locations:  # Only keep jobs in Bucharest
                location="Bucuresti"

                location_finish = get_county(location=location)
            #print(location_finish)
        # get jobs items from response
        job_list.append(Item(
            job_title=job.find('a').text.strip(),
            job_link=link,
            company='Verifone',
            country='Romania',
            county= location_finish[0] if True in location_finish else None,
            city='all' if location.lower() == location_finish[0].lower()\
                        and True in location_finish and 'bucuresti' != location.lower()\
                            else location,
            remote='hybrid',
        ).to_dict())

    return job_list
    #print(job_list)

def main():
    '''
    ... Main:
    ---> call scraper()
    ---> update_jobs() and update_logo()
    '''

    company_name = "Verifone"
    logo_link = "https://datasym.co.uk/wp-content/uploads/2017/09/verifone-logo-300x120.png"

    jobs = scraper()
    
    #print(jobs, len(jobs))
    # uncomment if your scraper done
    UpdateAPI().update_jobs(company_name, jobs)
    UpdateAPI().update_logo(company_name, logo_link)


if __name__ == '__main__':
    main()
