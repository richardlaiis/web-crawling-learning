import requests
url = input("Enter url of the image: ")
path = input("Enter the path the - saved in: ")
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print('Download complete.')
else:
    print('Oops! The HTTP request failed.')