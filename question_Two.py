import httplib2
import re,requests
import bs4
from bs4 import BeautifulSoup
# import re

class Extractor():

    def get_social_links(self, url):

        http = httplib2.Http()
        response, content = http.request(url)

        links = []

        for link in BeautifulSoup(content,'html.parser').find_all('a', href=True):
            links.append(link['href'])
        sm_sites = ['linkedin.com', 'facebook.com']
        social_list = []
        for i in links:
            for j in sm_sites:
                if j in i:
                    social_list.append(i)
        return social_list


    def get_email_id(self,url):
        r = requests.get(url)
        mail_list = []
        EMAIL_Valid = r"^[^@ ]+@[^@ ]+\.[^@ \.]{2,3}$"
        soup = BeautifulSoup(r.content, 'html.parser')
        all_links = soup.find_all('a', href=True)

        for link in all_links:
            if re.findall(EMAIL_Valid, link.attrs['href']):
                mail_list.append(link.attrs['href'])

        return mail_list

    def get_mobile_num(self,url):
        r = requests.get(url)
        phone_list=[]
        phone_regex=r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*(\d{1,2})$"
        soup = BeautifulSoup(r.content, 'html.parser')
        all_links = soup.find_all('a', href=True)
        for link in all_links:
            if re.findall(phone_regex, link.attrs['href']):
                phone_list.append(link.attrs['href'])

        return phone_list


url='https://ful.io/'

myextractor = Extractor()

social_list = myextractor.get_social_links(url)
email_list=myextractor.get_email_id(url)
phone_list=myextractor.get_mobile_num(url)


print("Social Links:")
for i in social_list:
    print(i)
print("")
print("E-Mails:")
for i in email_list:
    print(i)
print("")
print("Contact:")
for i in phone_list:
    print(i)