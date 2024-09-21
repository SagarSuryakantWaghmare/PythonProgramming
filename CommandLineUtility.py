import argparse
import requests

def download_file(url,local_filename):
    #note the stream =True parameters below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename,'wb')as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename            
parser=argparse.ArgumentParser()
#Add command line Arguments
parser.add_argument("url",help="Url of the file to download")
parser.add_argument("Output",help="name to download the file")
#parse the arguments
args=parser.parse_args()
#use the arguments in your code
print(args.url) 
print(args.output)
download_file(args.url,args.output)
