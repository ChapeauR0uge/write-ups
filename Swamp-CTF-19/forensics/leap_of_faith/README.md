# Leap of Faith

## Description

![leap_of_faith - SwampCTF'19](pres.png)

## Résolution

D'apres la description, il s'agit d'une citation du film matrix, avec comme particularite de nous parler d'outils de stego, avec une [image de neo](data/leap_of_faith.jpeg).

La premiere chose que je fait, c'est une verification du type de fichier :
```bash
file leap_of_faith.jpg
```
![step1 - SwampCTF'19](step1.png)

Rien d'anormale dans le fichier, il correspond bien a son type.

J'essaye donc d'extraire les donnees exif de l'image.
```bash
exiftool leap_of_faith.jpg
```
![step2 - SwampCTF'19](step2.png)

Je remarque la presence d'un thumbnail, que j'extrais de la maniere suivante:
```bash
exiftool -b -ThumbnailImage leap_of_faith.jpg > thumb1.jpg
```
J'obtiens une image de Morpheus.
![morpheus - SwampCTF'19](src/thumb1.png)

Je repete l'operation precedente
```bash
exiftool thumb1.jpg
```
![step3 - SwampCTF'19](step3.png)

```bash
exiftool -b -ThumbnailImage thumb1.jpg > thumb2.jpg
```
Nous obtenons le flag, sous forme de fichier jpg.
![flag - SwampCTF'19](src/thumb2.png)

## Flag

**flag{FR33_Y0UR_M1ND}**

