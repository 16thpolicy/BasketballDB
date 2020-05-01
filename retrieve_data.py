import wget
from os import mkdir
from shutil import rmtree
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
    
with open('code/datasets.txt') as datasets_file:
    urls = datasets_file.readlines()

    if len(urls) > 5:
        raise Exception("Too many datasets were specified")

    rmtree('code/datasets', ignore_errors=True)
    mkdir('code/datasets')

    for u in urls:
        #f = urllib.request.urlretrieve(u.rstrip())
        f = wget.download(u.rstrip(),'code/datasets/')
        print(f)
