import requests
import json
from bs4 import BeautifulSoup
import html_to_json
import requests
from csv import writer
import requests
import time
from stem import Signal
from stem.control import Controller

# def renew_tor_ip():
#     with Controller.from_port(port = 9051) as controller:
#         controller.authenticate(password="aAjkaI19!!laksjd")
#         controller.signal(Signal.NEWNYM)

def paperScraping(user_Name, user_email):

    url = "https://scholar.google.com/scholar?hl=en&as_sdt=0,5&q=" + user_email +"&btnG="
    authorProfLink= ''
    preAuthorProfLink= ''
    paperCount= 0
    profileStatus= 0

    jsonArr= []

    payload = {'api_key': '257c1db95bff34b0597bd7fd8b6101b4', 'url': url}
    response = requests.get('http://api.scraperapi.com', params=payload)
    print(response.status_code)
    if (response.status_code == 200):
        soup = BeautifulSoup(response.content, "html.parser")
        for items in soup.find_all('div', class_="gs_a"):
            # print(items)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            authorlist= items.find_all('a')
            for author in authorlist:
                authorS= str(author)
                # print(authorS)
                # print(authorS.find("<a"))
                if(authorS.find("<a")!= None):
                    
                    split1= authorS.split('href="')[-1]
                    # print(split1)
                    split2= split1.split('">', 1)[0]
                    split2= split2.replace('&amp;','&')
                    authorProfLink= "https://scholar.google.com" + split2                
                    if(authorProfLink == preAuthorProfLink):
                        break
                    else: 
                        preAuthorProfLink = authorProfLink

                    print(authorProfLink)
                    
                    payload = {'api_key': '257c1db95bff34b0597bd7fd8b6101b4', 'url': authorProfLink}
                    profileResponse = requests.get('http://api.scraperapi.com', params=payload)
                    # profileResponse = requests.get(authorProfLink)
                    # print(profileResponse.status_code)
                    # print("#######################################")
                    if (profileResponse.status_code == 200):
                        foundProfile = BeautifulSoup(profileResponse.content, "html.parser")
                        if(foundProfile.find('div', id ="gsc_prf_in")!= None):
                            name = foundProfile.find('div', id ="gsc_prf_in")
                            nameString = str(name)
                            if(nameString.find('">')!= None):
                    
                                split1= nameString.split('">')[-1]
                                # print(split1)
                                foundProfileName= split1.split('</', 1)[0]
                                # print(foundProfileName)
                                # print("________________________")
                                if (foundProfileName == user_Name):
                                    print("found")
                                    profileStatus= 1
                                    # print(foundProfile.find_all('a', class_ ="gsc_a_at").__len__)
                                    for papers in foundProfile.find_all('a', class_ ="gsc_a_at"):
                                        # print("___________ Test 1 _____________")
                                        splitLink = str(papers)
                                        # splitLink = papers.get('href')
                                        # print(papers)
                                        split1= ''
                                        split2= ''
                                        if(splitLink.find("<a")!= None):
                    
                                            split1= splitLink.split('href="')[-1]  
                                            # print(split1)                                          
                                            split2= split1.split('">', 1)[0]
                                            split2= split2.replace('&amp;','&')
                                            # print(split2)
                                            paperDetailsLink= "https://scholar.google.com" + split2 

                                            print(paperDetailsLink)
                                            
                                            payload = {'api_key': '257c1db95bff34b0597bd7fd8b6101b4', 'url': paperDetailsLink}
                                            paperDetailsResponse = requests.get('http://api.scraperapi.com', params=payload)
                                            # paperDetailsResponse = requests.get(paperDetailsLink)
                                            # print(paperDetailsResponse.status_code)
                                            print("#################    Papaer Details    ######################")
                                            if (paperDetailsResponse.status_code == 200):
                                                paperDetails = BeautifulSoup(paperDetailsResponse.content, "html.parser")

                                                paperCount= paperCount + 1
                                                paperLink =''
                                                paperName= ''
                                                paperType= ''
                                                paperPublishDate= ''
                                                paperDescription= ''
                                                jsonPaperDetails= {}
                                                if(paperDetails.find('a', class_ ="gsc_oci_title_link")!= None):
                                                    paperNameLink= paperDetails.find('a', class_ ="gsc_oci_title_link")

                                                    pLink= []                                                    
                                                    pLink.append(paperNameLink.get('href'))                                            
                                                    paperLink = paperLink.join(pLink)
                                                    # print(paperLink)
                                                    
                                                    paperNameLink = str(paperNameLink)
                                                    split1= ''
                                                    split2= ''
                                                    
                                                    if(paperNameLink.find("<a")!= None):
                                
                                                        split1= splitLink.split('href="')[-1]                                               
                                                        pName = split1.split('">', 1)[-1]
                                                        paperName = pName.split('</a>', 1)[0]
                                                        # print(paperName)
                                                elif(paperDetails.find_all('div', id ="gsc_oci_title")!= None):
                                                    if(paperDetails.find('div', id ="gsc_oci_title_wrapper")!= None):
                                                        paperNameLink= paperDetails.find('div', id ="gsc_oci_title_wrapper")

                                                    else : paperNameLink= paperDetails.find_all('div', id ="gsc_oci_title")[3]

                                                    
                                                    if(paperDetails.find('div', id ="gsc_oci_merged_snippet")!= None): 
                                                    #     pLink= []                                                    
                                                    #     pLink.append(paperNameLink.get('href'))  
                                                    #     print(pLink)                                         
                                                    #     paperLink = paperLink.join(pLink)
                                                    # else: 
                                                        paperNameLink= paperDetails.find('div', id ="gsc_oci_merged_snippet")
                                                        pLink= []                                                    
                                                        pLink.append(paperNameLink.get('href'))
                                                        paperLink = paperLink.join(pLink)
                                                        paperLink = "https://scholar.google.com" + paperLink
                                                    # print(paperLink)
                                                    
                                                    paperNameLink = str(paperNameLink)
                                                    split1= ''
                                                    split2= ''
                                                    
                                                    if(paperNameLink.find("<a")!= None):
                                
                                                        split1= splitLink.split('href="')[-1]                                               
                                                        pName = split1.split('">', 1)[-1]
                                                        paperName = pName.split('</a>', 1)[0]
                                                
                                                pType = paperDetails.find_all('div', class_ ="gsc_oci_field")[2].string
                                                paperType= str(pType)
                                                # print(paperType)
                                                pPublishDate = paperDetails.find_all('div', class_ ="gsc_oci_value")[1].string
                                                paperPublishDate = str(pPublishDate)
                                                # print(paperPublishDate)
                                                
                                                if(paperDetails.find('div', id ="gsc_oci_descr") != None):
                                                    pDescription= paperDetails.find('div', id ="gsc_oci_descr").string
                                                    paperDescription = str(pDescription)
                                                elif(paperDetails.find_all('div', class_ ="gsh_csp") != None):
                                                    gsh_size = paperDetails.find_all('div', class_ ="gsh_csp")
                                                    if(len(gsh_size)>= 2):
                                                        pDescription= paperDetails.find_all('div', class_ ="gsh_csp")[0].string
                                                        paperDescription = str(pDescription)
                                                # print(paperDescription)
                                                
                                                # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \t")
                                                jsonPaperDetails= {
                                                    "id": paperCount,
                                                    "paperLink": paperLink,
                                                    "paperName": paperName,
                                                    "paperType": paperType,
                                                    "paperPublishDate": paperPublishDate,
                                                    "paperDescription": paperDescription,
                                                }
                                                # jsonArr.append([ paperLink, paperName, paperType, paperPublishDate, paperDescription ])
                                                jsonArr.append(jsonPaperDetails)   
                                                        
                                            
                                        
                        if(profileStatus==1):
                            break
    print("total paper = ")
    print(paperCount)
    print("\t\n\n")
    return json.dumps(jsonArr)


# print(paperScraping())
# paperScraping()

        