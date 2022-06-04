# AUTHOR: Xeonrx | SOURCE: https://github.com/Xeonrx/Schlrint | LICENSE: MIT LICENSE
import argparse, requests
from googlesearch import search
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Command line for Schlrint.')
parser.add_argument('-d', '--district', type=str, help='School district to analyze.')
parser.add_argument('-l', '--location', type=str, help='Location for a more percise search.')
parser.add_argument('-t', '--targets', type=str, nargs="+", help='Checks for specified names only.')
parser.add_argument('-o', '--output', type=str, help='Outputs results into file.')
parser.add_argument('--full', action="store_true", help='Targets the full names of people.')
parser.add_argument('--deeper', action="store_true", help='Index more search results.')
parser.add_argument('--unique', action="store_true", help='Ingnore repeated names.')
args = parser.parse_args()

names = [] # Scraped names are stored here
pages = [] # Saved pages from google results
queries = [] # Queries to search for are stored here
deep = 2 if not args.deeper else 5
location = "" if not args.location else args.location

print("[SCHLRINT | https://github.com/Xeonrx/Schlrint]\n")
if not args.district:
    exit("[X] A school district needs to be specified (-d).")
if args.targets and args.full:
    exit("[X] Can't use both --full and -t in the same command!")

targets = args.targets if args.targets else open("FIRST.txt","r").read().splitlines() # Creates list of names to search
if args.full:
    lastnames = open("LAST.txt","r").read().splitlines() # Opens list of last names if args.full

def ending(names): # Ending prompt of Schlrint. Returns amount of names found, along with unique number
    exit(f"\n[SCHLRINT RESULTS]:\nfound: {len(names)}\nunique: {len(set(names))}")

with open("QUERY.txt","r") as f: # Uses queries to search on google, and scrapes results off internet
    try:
        for i in f.read().splitlines():
            for s in search(f"{args.district} {location} {i}", tld="co.in", num=deep, stop=deep, pause=2):
                page = requests.get(s);soup = BeautifulSoup( page.content , 'html.parser');pages.append(page.text)
    except KeyboardInterrupt:
        ending(names)

def pagescan(page,target): # Takes 1 target at a time. If target is in page, added into list and printed on terminal
    try:
        if target in page:
            if args.unique:
                if target in names:
                    return
            names.append(target)
            if args.output: # outputs findings into a file if args.output
                with open(args.output,"a") as f:
                    f.write(target + "\n")
            print(target)
    except:
        return


try: # Goes through all given names of all scraped pages. Runs each through the pagescan() function
    for a in pages:
        for b in targets:
            if args.full:
                for i in lastnames:
                    pagescan(a,f'{b} {i}')
                continue
            pagescan(a,b)
except KeyboardInterrupt:
    ending(names)

ending(names) # Script ends here