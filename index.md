# AdventButWrong
## A text adventure with a twist
### Progress
- [x] Starter rooms
- [x] Interaction system
- [x] Additional things
- [ ] Complete story
- [ ] Further rooms
- [ ] Characters
- [ ] Items
- [ ] Commands
- [ ] Save/load system
- [ ] A normal ending 
### Downloads
- [Lastest (linux DEB)](https://textovortex.github.io/AdventButWrong/lastest.deb)
- [Stable (linux DEB)](https://textovortex.github.io/AdventButWrong/stable.deb)
- [Source code (ZIP)](https://github.com/textovortex/AdventButWrong/archive/refs/heads/main.zip)
- ![Map (JPG)](https://textovortex.github.io/AdventButWrong/AdventButWrong_map.jpg)


## Repository install (Linux Debian, Raspbian, TwisterOS, and Ubuntu ONLY:
1. `curl -s https://packagecloud.io/install/repositories/LEHAtupointow/txtadvent/script.deb.sh | sudo bash`
2. `sudo apt install adventbutwrong`

## Install on Red-Hat Based distributions (Fedora, Red Hat Enterpise Linux, etc.):
1. Install Alien from [Here](http://ftp.de.debian.org/debian/pool/main/a/alien/)
2. `tar xf alien-VERSION.tar.gz`
3. `cd alien`
4. `perl Makefile.PL; make; sudo make install`
5. Download adventbutwrong
6. `alien -r adventbutwrongVERSION.deb`
7. `sudo yum localinstall adventbutwrongVERSION.rpm`
8. Play it!

## Termux install (Download Termux from Google Play)
1. `pkg update && pkg install root-repo && pkg update && pkg install python`
2. `wget https://textovortex.github.io/AdventButWrong/termux_stable.deb`
3. `pkg install ./termux_stable.deb
4. `adventbutwrong # to run`
5. Play it!
