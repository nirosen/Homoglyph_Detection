# str_to_png
This is a dot-net project which converts a string and a font-file to a corresponding image.

## General Purpuse
given a font and string, render their visual appearance, in order to find **homoglyphs** in different fonts.
### homo-what?
a homoglyph is one of two or more graphemes, characters, or glyphs with shapes that appear identical or very similar (https://en.wikipedia.org/wiki/Homoglyph).
example: 
```
this is NOT a homoglyph. ｔһⅰѕ Ꭵｓ ａ ｈоrnοɡⅼｙрｈ
```
that was created using this cool online tool:
* [homoglyph-generator](https://www.irongeek.com/homoglyph-attack-generator.php)

## How To Run
### usage: 
```
str_to_image.exe string_to_convert path_to_Font_file path_to_output_image

  default font:               GenericSansSerif (already included in System.Drawing)
  default output image path:  output.png
```
example command-line:
```
str_to_image.exe "notepad.exe   this is NOT a homoglyph. ｔһⅰѕ Ꭵｓ ａ ｈоrnοɡⅼｙрｈ." "Lucida Console Regular.TTF" "Lucida Console Regular homoglyph_output.png"
```

## Authors

* **Dr. Liron Allerhand** - *Advisor*
* **Nir Rosen** - *Initial work*
