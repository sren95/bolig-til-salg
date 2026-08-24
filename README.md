# Bolig til salg - Sundgade 1, 4.th

Statisk salgsside for privat salg af ejerlejligheden på Sundgade 1, 4.th,
6400 Sønderborg.

## Se siden

Offentlig GitHub Pages-side:

<https://sren95.github.io/bolig-til-salg/>

Direkte links:

- Forside: <https://sren95.github.io/bolig-til-salg/>
- Galleri: <https://sren95.github.io/bolig-til-salg/gallery.html>
- Salgsopstilling: <https://sren95.github.io/bolig-til-salg/salgsopstilling-sundgade-1.pdf>

## Lokal preview

Fra projektmappen kan siden ses lokalt med:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Åbn derefter:

- Forside: <http://127.0.0.1:8080/>
- Galleri: <http://127.0.0.1:8080/gallery.html>
- Salgsopstilling: <http://127.0.0.1:8080/salgsopstilling-sundgade-1.pdf>

Stop serveren igen med `Ctrl+C`.

## GitHub Pages

GitHub Pages bør være sat op sådan:

- Source: Deploy from a branch
- Branch: `main`
- Folder: `/root`

Når ændringer er pushet til `main`, ligger siden på den offentlige URL ovenfor.

## Vedligehold

Når billeder til det fulde galleri tilføjes eller slettes i `assets/gallery/`,
opdateres billedlisten med:

```sh
node scripts/update-gallery-manifest.mjs
```

Hvis QR-koden skal gendannes til den offentlige URL:

```sh
python3 -m pip install -r scripts/requirements-qr.txt
python3 scripts/generate-qr-code.py
```
