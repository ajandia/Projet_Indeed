import requests, re
from bs4 import BeautifulSoup

# reponse = requests.get("https://fr.indeed.com/emplois?l=Paris%20(75)")
# print(reponse)
# soup = BeautifulSoup(reponse.content, 'html.parser')

def getdata(url):
    r = requests.get(url)
    return r.text


# Get Html code using parse
def html_code(url):
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    # return html code
    return BeautifulSoup(htmldata, 'html.parser')
  
def get_url(soup):
    data_str = "".join(
        item.get_text()
        for item in soup.find_all("a", class_=r"tapItem fs\-unmask result job_[0-9abcde]+ sponsoredJob resultWithShelf sponTapItem desktop")
    )
    print(data_str.split("\n"))

url = "https://fr.indeed.com/emplois?l=Paris%20(75)&radius=10&vjk=e466244b78bf58da"
soup = html_code(url)
get_url(soup)

# filter job data using
# find_all function
def job_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = "".join(
        item.get_text()
        for item in soup.find_all("h1", class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title")
    )
    print(data_str.split("\n"))
    return data_str.split("\n")
  
# filter company_data using
# find_all function
  
def company_data(soup):
    result = ""
    # find the Html tag
    # with find()
    # and convert into string
    data_str = "".join(
        item.get_text() for item in soup.find_all("div", class_="sjcl")
    )
    result_1 = data_str.split("\n")
    return [result_1[i] for i in range(1, len(result_1)) if len(result_1[i]) > 1]
  
# driver nodes/main function
if __name__ == "__main__":
  
    # Data for URL
    # Location = "Paris%20(75)"
    # url = f"https://in.indeed.com/emplois?l={Location}"
    # url = "https://fr.indeed.com/emplois?l=Paris%20(75)&radius=10&vjk=e466244b78bf58da"
    url = "https://fr.indeed.com/viewjob?jk=e466244b78bf58da&tk=1fmul2omsttr2800&from=serp&vjs=3&advn=2228388617598600&adid=379939308&ad=-6NYlbfkN0B3vddu6DRVWT7WLrbDCctBKrqAv7SvNauV7-G6kbfQnrhaO5MzhOe89nt6gBnUiOx28cwlxOr8wPjDziaH3JzSrk-nyUtFjpNl9QRBhkwDj6Jfpfwoonz_MuJszMR2gOIY-XYW-hSG8t0RwzMxadeaFLp4Fw4KCghlYXRdwRLAOFZQ-f8-Okn0-lm3-j0_kG_Pc592RVsQwMH-MeiFNi-yMC74cu1bc3Yn8-H7PORCysnzz4Wnwj7Rjj8Qv6m4zJcK_nDgddO_pC7T111RYF1UFSwD2R_TZlgJ5q73S4W3ktcTw3P-KDzxlO8f20nWlVi2W6QSaqgKqzzPV033sExzgwfalKke_70Lay0Fg2qkng==&sjdu=blopwdXTAU6MV5BxPXztVO-Qei59nuvQX9vnhd_wiCsfA7pUYBx1uKVn7iVrRffzn9A_o5ZcUsHZMyviolylZNkPqwM5PxRT4PEBb0ubpcqNv46KnXOHXJMPGPmEQnfgS3kfjVaUakpMrodgUBdvMHFfTZ5iRY7u2icCkGs259QNsxiTIhn4T2uVhU7XTfsfbDLrPSHNu9UE9vyYMLt85OUFVnorZpF9DcxYGPEjlQwBxKSZnKmr6aJUHGv2geJr3hyzDWDrl8M6JGHtQuzG7E7SBXnu4JgaWaF9htDeAMdMQHPxD_k70Sgq12VNr-Jor66bTU3M3QT_RVduVCCHJ7KPpZQ8c1pBZiE9zZNO-FEmltEtgdEBR5V5ZjZo6wGru8jcYS9k8gII4Bnlf3xXQg"
    # job = "data+science+internship"
    # Location = "Noida%2C+Uttar+Pradesh"
    # url = "https://in.indeed.com/jobs?q="+job+"&l="+Location
  
    # Pass this URL into the soup
    # which will return
    # html string
    soup = html_code(url)
    # print(soup)
  
    # call job and company data
    # and store into it var
    job_res = job_data(soup)
    com_res = company_data(soup)
  
    # Traverse the both data
    temp = 0
    for i in range(1, len(job_res)):
        j = temp
        for j in range(temp, 2+temp):
            print("Company Name and Address : " + com_res[j])
        temp = j
        print("Job : " + job_res[i])
        print("-----------------------------")

# url = "https://api.scrapingrobot.com/?responseType=json&waitUntil=load&noScripts=false&noImages=true&noFonts=true&noCss=true&token=ee529fe3-24ee-4b8f-a5e5-32dcc7b636a5"
# headers = {"Accept": "application/json"}
# response = requests.request("GET", url, headers=headers)
# print(response.text)
# return(<select onChange={that.props.changeHund} className="selectHund" name="hund">{POS}</select>);