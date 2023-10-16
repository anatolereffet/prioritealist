## Pour lancer l'environnement
---
Dans le folder source du projet
```bash
pip install poetry
```

Pour créer son environnement poetry
```bash
poetry shell
```
Récupérer la commande dans l'output du style 
```bash
emulate bash -c '. /Users/aze/Library/Caches/pypoetry/virtualenvs/priori-tea-list-FeC8235P_-py3.8/bin/activate'
```
Ça permet de relancer son environnement poetry dès que nécessaire

Pour désactiver l'environnement 
```bash
deactivate
```

Pour run les différents tests/type hint checker utiliser le makefile tel 
```bash
make lint
```
Les différentes commandes dispo sont visible dans le Makefile