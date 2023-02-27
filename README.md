# Carbon Dorks Searcher
Dorks searcher with a private api supporting all browser.

## Installation

To download and run the server you would need the server file. Contact the Owners.

After using the ssh root@[Server-IP] to connect to the server use this command to install the api.
```bash
  apt update -y; apt upgrade -y; apt install wget unzip -y;
  wget https://dl.google.com/go/go1.20.1.linux-arm64.tar.gz;
  rm -rf /usr/local/go && tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz;
  export PATH=$PATH:/usr/local/go/bin;
  echo "export PATH=$PATH:/usr/local/go/bin" > /root/.bashrc;
  cd /root; wget "API SERVER PACK URL";
  unzip dork_searcher.zip;
  cd /root/dork_searcher; go run .
```

⚠️ Make sure to change the config inside the main.go file. 
    
## Running

To run this project

```json
  {
      "step_01":"Change api & engine string into searecher.",
      "step_02":"Start the api on the server [cd /root/dork_searcher;go run .]",
      "step_03":"Run the dork shearcher it self[python dork_searcher.py]",
      "step_04":"Enjoy"
  }
```


## Authors

- [@zingstrok](https://t.me/zingstrok)

