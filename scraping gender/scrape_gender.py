from sys import argv
import csv 
import requests

def main(csv_names , csv_proxies):
    url = "https://api.genderize.io?name="
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

    try:
        f_names  = open(csv_names,'r') 
        f_proxies = open(csv_proxies,'r')
        #f_output = open('./output.csv'.'w')
    except FileNotFoundError: 
        print("Could not open files")
    w_names = csv.reader(f_names)
    w_proxies = csv.reader(f_proxies)
    names = list()
    genders = list()
    for proxy in proxies: 
        for i in range(1000):


if __name__ == "__main__":
    main(argv[1],argv[2])
