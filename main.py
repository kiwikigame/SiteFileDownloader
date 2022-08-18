import requests, random, re, time, os

url = "aaa"

while(url[0:4] != "http"):
    url = input("URL : ")
    if(url[0:4] != "http"):
        print("L'url doit commencer par http...")
    else:
        url = f"{url}/"
        psg = input("Nombre de scan (0=inf) -Défaut=0 : ")
        if not psg:
            psg = 0
        psg = int(psg)
        delay = input("Delay entre chaque fichier (en sec) -Défaut=0 : ")
        if not delay:
            delay = 0
        delay = int(delay)
        iter = 1

        if psg == 0:
            print(f"Telechargement de tout les fichier depuis {url} avec une infinité d'itérations et un delay de {delay} secondes")
        else:
            print(f"Telechargement de tout les fichier depuis {url} avec {psg} itérations et un delay de {delay} secondes")

        if not os.path.exists('Out'):
            os.makedirs('Out')
        globalname = re.search('\:\/\/(.*?)\.',str(url)).group(1)
        if not os.path.exists(f"Out/{globalname}"):
            os.makedirs(f"Out/{globalname}")
        
        while iter <= psg or psg == 0:
            time.sleep(delay)
            iter += 1
            headers = {"User-Agent": f"Mozilla/5.0 (X11; Windows x86_64; rv:60.0) Gecko/{random.randint(12548,1354795)} Firefox/60.0",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                       "Accept-Language": "fr-FR,fr;q=0.9"
                      }
            start = time.time()
            response = requests.get(url=url, headers=headers)
            name = re.search('filename="(.*?)"',str(response.headers)).group(1)
            open(f"Out/{globalname}/{name[:-4]}.{name[-3:]}", "wb").write(response.content)
            print(f"{name}   {time.time()-start:.3}ms   {response.content.__sizeof__()/1000}ko")
