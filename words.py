import urllib.request

word_url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
#even though the url was valid, it didn't like it, so we had to request using headers
req = urllib.request.Request(word_url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    response = urllib.request.urlopen(req)
    long_txt = response.read().decode()
    word_list = long_txt.splitlines()  # Print first 10 words as an example
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")



'''Resulted in a 404 error - 
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()'''
