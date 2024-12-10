# Modello Ptolemaico pro Planetis in Python

Haec projectum visualisationem systematis Ptolemaici in Python implet, ubi planetarum motus circum Terram computantur secundum rationem epicycli et deferentis. Codex includit animae planetarum, circulos deferentes, epicyclus, et projectionem apparentem positionum planetarum in globum caelestem.

## Caracteristicae

- Terra in medio figurationis
- Planetae circum Terram moveantur secundum systema Ptolemaicum (cum epicyclis et deferentibus)
- Circulus zodiacus cum signis zodiacalibus in figuris
- Unitas temporis inanimatione et annotatione data
- Animae animatae cum tracibus planetarum et circulis deferentibus et epicyclis
- Planetarum positio pro datum tempore calculata, prout initium in data astronomica notorum
- Facile configurabilis pro positionibus planetarum secundum datam epocham

## Notae

- Planetae sunt initii secundum data astronomica notiora ad 2024-01-01
- Data orbitalia includunt: radius deferentis, radius epicycli, periodus deferentis, periodus epicycli, et angulus initialis
- Nova data facile inseri possunt pro aliis planetis vel temporibus
- Codex in Python implementatus cum libris `numpy`, `matplotlib`, et `datetime`
  
## Facultates

- Generatio animationis cum planetarum motu
- Traciatio de positione planetarum et epicyclorum
- Divisio circuli zodiacalis per signa zodiacalibus
- Configurabile tempus et data initium

## Instrucitio ad Usum

1. Clonare hunc repositorium:
git clone https://github.com/oldbridge/ptolomeo.git

2. Installare necessarias bibliothecas:
pip install numpy matplotlib

3. Exsecutione codice:
python ptolemaicum.py

## Licentia

Haec projectum licentiatur sub [Licentia MIT](LICENSE).
