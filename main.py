from os import path
import requests

from bs4 import BeautifulSoup

from utils import cache_html_file, clean_text_element, get_html_content

python_jobs_url = """
https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=
"""
cached_html_path = "samples/python_jobs.html"
valid_post_dates = ['Posted few days ago', 'Posted today', 'Posted 1 day ago']


if path.exists(cached_html_path):
    print('HTML cache already exists')
    html_text = get_html_content(cached_html_path)
else:
    html_text = requests.get(python_jobs_url).text
    cache_html_file(cached_html_path, html_text)

soup = BeautifulSoup(html_text)

jobs_cards = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")


for job in jobs_cards:
    published_date = clean_text_element(job.find('span', class_="sim-posted").text)

    if published_date in valid_post_dates:
        company_name = clean_text_element(job.find('h3', class_="joblist-comp-name").text)
        position_name = clean_text_element(job.header.h2.a.text)
        skills = clean_text_element(job.find('span', class_="srp-skills").text)
        skills = skills.replace('  ,  ', ', ')
        more_info = job.header.h2.a.get('href')

        print("Company Name:", company_name)
        print("Position Name:", position_name)
        print("Required skills:", skills)
        print("More Info:", more_info)
        print("=" * 100)
