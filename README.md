# ERKO RIDER

Hotová malá 3D arkádová hra: černý Mustang inspirovaný moderním fastbackem, noční dálnice, provoz, drift, nitro, těsná předjetí, kolize a časované checkpointy.

## Okamžité spuštění

Rozbalte ZIP a otevřete **index.html** v moderním prohlížeči. Tento soubor obsahuje celou hru včetně 3D enginu, grafiky i syntetizovaného zvuku. Nepotřebuje instalaci, připojení k internetu ani API klíče. Na telefonu je nejpohodlnější hrát přes webový odkaz na šířku.

## Ovládání

| Klávesa | Funkce |
| --- | --- |
| W / ↑ | Plyn |
| S / ↓ | Brzda, při malé rychlosti zpátečka |
| A/D / ← → | Řízení; při vysoké rychlosti kontrolovaný drift |
| Mezerník | Nitro |
| C | Přepnutí kamery |
| Esc | Pauza |
| R | Restart |

Na telefonu držte příslušná velká tlačítka. Plyn, řízení a nitro lze kombinovat. Zvuk se spustí až po stisknutí tlačítka. Rekord se ukládá v prohlížeči; při otevření místního souboru se dostupnost úložiště může lišit podle prohlížeče.

Checkpoint každých 1,4 km prodlouží čas. Jízda nad 180 km/h zvyšuje násobič. Těsné předjetí dává body a doplní nitro. Silné nárazy ubírají stav karoserie; při zničení nebo vypršení času jízda končí.

## Publikace přes GitHub Pages

Repozitář obsahuje hotovou hru i workflow **Publish ERKO RIDER**. Při pushi do `main` workflow sestaví samostatný `index.html`, připraví publikační artefakt a nasadí jej přes GitHub Pages. Workflow při prvním běhu umí Pages pro repozitář automaticky inicializovat.

Pro ruční kontrolu otevřete **Actions → Publish ERKO RIDER**. Výsledný veřejný odkaz je po úspěšném nasazení dostupný také v **Settings → Pages**.

Připravený workflow publikuje pouze sestavenou hru a licenci. Aktuální zdroje a samostatná hra jsou součástí tohoto repozitáře. GitHub Pages pro soukromý repozitář vyžaduje odpovídající plán; tento repozitář je veřejný.

Oficiální postup: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Úpravy zdrojů

- `src/game.js`: fyzika, svět, vozidla, zvuk, UI a herní smyčka.
- `src/software-renderer.js`: perspektivní záložní renderer bez WebGL.
- `src/style.css`: vzhled a mobilní rozložení.
- `src/template.html`: HTML rozhraní.
- `src/vendor/`: lokálně přibalený Three.js.

Po úpravách spusťte `python3 scripts/build.py`. Skript z přibalených modulů vytvoří nový samostatný `index.html`; nemá externí závislosti. Herní zdroje nepoužívají backend ani placené služby.

## Grafika a ověření

Hlavní renderer využívá WebGL / Three.js: reflexní lak, osvětlení, mlhu a světelné efekty. Při nedostupném WebGL se automaticky použije jednodušší perspektivní Canvas renderer. Záložní režim má nižší výkon a omezené vzdálené detaily.

Testování proběhlo v prohlížeči se zablokovaným WebGL, tedy přes záložní renderer. Herní mechaniky i mobilní rozložení byly ověřeny; výkon 60 FPS, WebGL obraz a zvukový výstup na fyzickém iPhonu nebyly změřeny. Podrobnosti jsou v `TEST_REPORT.md`.

Vůz je původní procedurální stylizace inspirovaná Mustangem, nikoli oficiální model od Fordu. Three.js má licenci MIT, uvedenou v `THIRD_PARTY_LICENSES.txt`. Hudba i zvukové efekty vznikají programově.
