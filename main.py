import requests
from bs4 import BeautifulSoup




image=['jpeg','jpg','png','ico', 'avif']
    




def getLinks(INPUT_TYPE):
    r = requests.get(INPUT_URL)
    soup = BeautifulSoup(r.content , 'html5lib')
    links = soup.findAll('a')
    for i in range(len(image)):
        if (INPUT_TYPE == image[i] ):
            links = soup.findAll('img')
            file_links = [INPUT_URL + link['src'] for link in links if link['src'].endswith(INPUT_TYPE)]
            break
        else :
            file_links = [INPUT_URL + link['href'] for link in links if link['href'].endswith(INPUT_TYPE)]


    return file_links

def download(file_links):
    for link in file_links:
        file_name=link.split('/')[-1]
        print("Downlaoding %s"%file_name)
        r= requests.get(link, stream =True)
        if  (r.status_code == 200):
            with open(file_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=2048*2048):
                  if chunk:
                      f.write(chunk)
            print("%s Downloaded" %file_name)
        else :
            print("Cant find source of file!")
            next
        
    return



if __name__ == "__main__":
    print('enter website you want  to download its filse:')
    INPUT_URL=input()
    r=requests.get(INPUT_URL)
    if (r.status_code != 200):
        raise {"Website's not responding!"}
       
    print('What kind of files you want to download:')
    INPUT_TYPE = input()
    
    file_links = getLinks(INPUT_TYPE)
    download(file_links) 
    print("Done!")

