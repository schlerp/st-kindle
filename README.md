# schlerp's st

### about
This is my fork of ST, it was started form the 0.7 version of the AUR package. Currenly uses make and manual installation. ~~Will be writing PKGBUILD build soon for easy use on arch, probably wont add it to aur unless someone asks for it!)~~

### features

  * Transparency with an x compositor (eg. xcompmgr or compton)
  * Base16 Hopscotch theme
  * Scroll support added (why the fuck would I use such a light terminal and then wait for tmux to load every time I want to use it?)
  * Default font ("monofur for Powerline" currently) configured to be legible on a HiDPI screen (I have a 13.3 inch with 3000x1800)
  * Will add more as I see fit, after all isnt that the beauty of st!?!

### updateconf.sh
This is a script that i use to remove ("rm ./config.h") and replace (cp ./config.def.h ./config.h) the config.h file. Semi deprecated as the chtheme.py script can be used instead (see below).

### chtheme.py
This script is used to perform surgery on the config.h file. Themes are sections of the config.h file that define default colours and bg/fg colours. 

You will notice some tags in my config.def.h file that signify the themes starting and end point ("// THEME_START" and "// THEME_END" respectively). The chthemes.py script will use the config.def.h file as a template and insert the text from the .theme file inbetween the tags (any data that was between the tags in config.def.h will be removed).

Themes are stored in the "themes/" directory with an extension of .theme (not compulsory, anything in the theme name after the first "." will be ignored, eg. "derp.theme" is referred to as "derp"), you can check them out to see how simple they are. 

These themes were created from Base16 Xdefault colour schemes from github. By importing them as Xresources into [Terminal.sexy](http://terminal.sexy) and then exporting them as "Simple Terminal" header excerpts, you can quickly and effectively create themes from Base16 colour schemes. :D

### todo

  * ~~Configure font size a bit more~~ Done!
  * ~~Work out if a broke anything allowing scroll without holding shift key~~ Done! (seems all good :D)
  * ~~Remove commented code blocks when sure its all good~~ Done!
  * ~~Adjust color theme to Base16 Hopscotch, (write a tool to do this for me?)~~ - #archlinux rnabinger got me onto http://terminal.sexy, god mode enabled!
  * ~~Create PKGBUILD for makepkg on arch.~~ - created one, placed in folder "arch/", .gitignore ignores all files in "arch/" except PKGBUILD so you can makepkg to your hearts content. (PKGBUILD modified from st-git in AUR)