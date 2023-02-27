import requests
import base64
import json
import threading
import time
import console
import concurrent.futures

def searcher(dork):
    results = requests.get("http://192.168.1.10:9999/search/google/{}".format(base64.b64encode(dork.encode()).decode('utf-8')))

    results_json = json.loads(results.text)

    print("[+]Reversed {} link from the dork {}".format(len(results_json["link"]), dork))

    with open("results.txt", "a") as results_handler:
        for link in results_json["link"]:
            results_handler.write(link + "\n")

def main():
    dork_file = open(input("[.]Dork list -> "), "r").readlines()

    concurrent.futures.ThreadPoolExecutor(10).map(searcher,dork_file)

if __name__ == "__main__":
    main()
