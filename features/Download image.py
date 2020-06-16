import requests


def downloadImage(url):
    response = getResponse(url)
    fileName = response.url.split('/')[-1]
    with open(fileName, 'wb') as file:
        file.write(response.content)


def getResponse(url):
    response = requests.get(url, allow_redirects=True)
    return response


url = 'https://loremflickr.com/320/240'
downloadImage(url)
print("Succesful!")
