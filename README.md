# Homoglyphs-Social-Engineering-Project
This is a project which aims to identify Social-Engineering in the domain of digital-forensics & cyber-security.

## General Purpuse
we reffer to the issue of attackers who abuse the graphical-similiarity of strings, in order to harden the detection and the analysis of their attacks. 
for example, an attacker can plant his malicious file in the next path:
C:\windows\systern32\ntd11.dll
this path is actualy very similiar to the legitimate system-file path:
C:\windows\systern32\ntdll.dll
and a security researcher (a hunter) can mistake the forged it for a legitimate file.

the phenomenon of graphical-similiarity is called **homoglyphs**.

### homo-what?
a homoglyph is one of two or more graphemes, characters, or glyphs with shapes that appear identical or very similar (https://en.wikipedia.org/wiki/Homoglyph).
example: 
```
this is NOT a homoglyph. ｔһⅰѕ Ꭵｓ ａ ｈоrnοɡⅼｙрｈ
```
that was created using this cool online tool:
* [homoglyph-generator](https://www.irongeek.com/homoglyph-attack-generator.php)

## How To Run this project?
### usage: 
```
main.py
```

## Authors

* **Dr. Liron Allerhand** - *Advisor*
* **Nir Rosen** - *Initial work*
