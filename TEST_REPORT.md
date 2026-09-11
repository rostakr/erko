# ERKO RIDER — ověření

Testováno 10.–11. září 2026 v prohlížeči Chrome v testovacím prostředí.

## Ověřené chování

- Start hry a vykreslení perspektivní 3D scény.
- Akcelerace; řízení doleva i doprava.
- Brzdění a zpátečka do −14,4 km/h.
- Nitro: při cíleném testu vzrostla rychlost ze 137,4 na 231,1 km/h; zásoba klesla a stav karoserie zůstal 100 %.
- Bodování vzdálenosti a průběžné přidávání provozu.
- Změna kamery, pauza a pokračování.
- Kolize se svodidly, pokles stavu karoserie až na nulu a obrazovka konce hry.
- Okamžitý restart s vynulovanými body a opraveným autem.
- Zachování nejlepšího skóre v localStorage.
- Mobilní rozměry 844 × 390: současný plyn a řízení, brzda a nitro přes pointer události.
- Checkpoint: při 1 403,6 m byl připsán první checkpoint a zbývající čas vzrostl na 49,18 s.
- Rychlost při boostu dosáhla 327,6 km/h.
- Opětovné využívání pevných poolů silnice, aut a částic; po průjezdu se objevilo 10 aktivních vozidel z maximálně 18.

- Cílené těsné předjetí: 1 near miss, skóre 600,21 a stav karoserie 100 %; při průjezdu boční rozestup středů aut 2,36 m.
- Násobič: po 4,36 sekundách nad 180 km/h vzrostl na ×1,5; maximální rychlost v testu 251,82 km/h, stav karoserie 100 %.
- Samostatný distribuční index.html se načetl, vykreslil menu a po stisku START RIDE přešel do jízdy s přibývajícími body.
- Opravené změny pruhů znovu ověřují vzdálenost a rychlost přibližujícího se hráče před zahájením manévru.

## Rozsah testů a omezení

Prohlížeč v tomto prostředí odmítl vytvoření WebGL kontextu. Vizuální a herní testy proto proběhly přes perspektivní Canvas fallback se stejným světem, modelem a fyzikou. Výkon tohoto rendereru v testovacím prostředí neodpovídá výkonu WebGL na běžném zařízení. WebGL reflexe, skutečný zvukový výstup a 60 FPS na fyzickém iPhonu nebyly nezávisle ověřeny.

První obecný test nitroboostu skončil kolizí s provozem, a proto nemohl prokázat vyšší koncovou rychlost. Samostatný test bez kolize následně prošel. Při automatickém průjezdu checkpointem nebyl získán bonus za těsné předjetí a násobič na konci činil 1; tyto mechaniky byly proto odděleny do cílených testů, které následně prošly.

## Distribuce

Hra nevyžaduje síťové assety ani runtime API. Tato verze je připravena pro vydání v `rostakr/erko`. Výsledek nasazení dokládá příslušný běh GitHub Actions. Přiložený workflow vychází z oficiální dokumentace GitHub Pages:
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
