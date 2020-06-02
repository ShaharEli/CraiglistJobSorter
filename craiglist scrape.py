from bs4 import BeautifulSoup
import requests
import os
url=input("Enter craiglist url to scrape for jobs: ")
web=requests.get(url)
web=web.text
soup=BeautifulSoup(web,"html.parser")
file_name=soup.find("a",{"class":"reset"}).text+" list:"
lolz=soup.find_all("p")
import io
f=io.open("list.txt", "w", encoding="utf-8")
f.write(file_name+"\n--------------------\n\n")
x=0
while True:
    for job in lolz:
        x+=1
        lop=job.find("a","result-title")
        try:
            link=lop.get("href")
        except:
            link="link unavailable"
        try:
            job_name=lop.text
        except:
            job_name="job name unavailable"
        checker=0
        location4=""
        try:
            location4=job.find("span","result-hood").text
            checker=1
        except:
            pass
        try:
            date=job.find("time","result-date").text
        except:
            date="date unavailable"
        if checker==0:
            pop=("the job is: "+job_name+"\nthe date is: "+date+"\nlink : "+link+"\n-----------------\n")
            f.write(pop)
        else:
            pop=("the job is: "+job_name+"\nthe date is: "+date+"\nthe location is: {}".format(location4)+"\nlink : "+link+"\n-----------------\n")
            f.write(pop)
        del location4
    try:
        next_page=soup.find("a",{"title":"next page"})
        next_page=next_page.get("href")
        web=requests.get("https://boston.craigslist.org"+next_page)
        web=web.text
        soup = BeautifulSoup(web, "html.parser")
        lolz = soup.find_all("p")
    except:
        break
job_found="total jobs found: {}".format(x)
f.write(job_found)
f.close()
