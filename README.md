# bolig-til-salg

En enkel statisk salgsside for en lejlighed.

Åbn `index.html` direkte i en browser for at se siden. Udskift pladsholderne
med de rigtige boligdata, og læg eventuelle billeder i projektet, når de er klar.

Når billeder til det fulde galleri tilføjes eller slettes i `assets/gallery/`,
opdateres billedlisten med:

```sh
node scripts/update-gallery-manifest.mjs
```
