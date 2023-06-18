#!/usr/bin/env python3

from os import walk
from os.path import join
from sys import exit


path = 'docs/'


for a, b, c in walk(path):
    for fichier in c:
        fp = join(a, fichier)
        if fp.lower().endswith('.md'):
            print(fp)
            r = list()
            with open(fp, 'r') as f:
                indetails = False
                hint = False
            
                lignes = f.readlines()
            
                for ligne in lignes:
                    if ligne.startswith('<details>'):
                        indetails = True
                    if ligne.startswith('</details>'):
                        indetails = False

                    if '{% hint style="' in ligne:
                        hint = True
                    if '{% endhint %}' in ligne:
                        hint = False
                    
            
                    if not indetails and not ligne.startswith('</details>') and not '{% endhint %}' in ligne:

                        if hint and '{% hint style="info" %}' in ligne:
                            ligne = '> [!NOTE]\n'
                        elif hint and '{% hint style="success" %}' in ligne:
                            ligne = '> [!TIP]\n'
                        elif hint and '{% hint style="warning" %}' in ligne:
                            ligne = '> [!WARNING]\n'
                        elif hint and '{% hint style="danger" %}' in ligne:
                            ligne = '> [!ATTENTION]\n'

                        elif hint and '[!NOTE]' not in ligne and '[!TIP]' not in ligne and '[!WARNING]' not in ligne and '[!ATTENTION]' not in ligne:
                            ligne = '> ' + ligne

                        banned = list()
                        banned.append('![](<../.gitbook/assets/image (9) (1) (2).png>)')
                        banned.append('to easily build and **automate workflows** powered by the world')
                        banned.append('Get Access Today:')
                        banned.append('url="https://trickest.com/?utm_campaign=hacktrics')

                        isBanned = False
                        for i in banned:
                            if i in ligne:
                                isBanned = True

                        if not isBanned:
                            r.append(ligne)


            with open(fp, 'w') as f:
                for ligne in r:
                    f.write(ligne)
