-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Format: 3.0 (quilt)
Source: wpa
Binary: hostapd, wpagui, wpasupplicant, wpasupplicant-udeb
Architecture: linux-any kfreebsd-any
Version: 2:2.6-18
Maintainer: Debian wpasupplicant Maintainers <wpa@packages.debian.org>
Uploaders: Andrej Shadura <andrewsh@debian.org>
Homepage: http://w1.fi/wpa_supplicant/
Standards-Version: 3.9.6
Vcs-Browser: https://salsa.debian.org/debian/wpa.git
Vcs-Git: https://salsa.debian.org/debian/wpa.git
Build-Depends: debhelper (>> 10), libdbus-1-dev, libssl-dev, qtbase5-dev, libncurses5-dev, libpcsclite-dev, libnl-3-dev [linux-any], libnl-genl-3-dev [linux-any], libnl-route-3-dev [linux-any], libpcap-dev [kfreebsd-any], libbsd-dev [kfreebsd-any], libreadline-dev, pkg-config, docbook-to-man, docbook-utils
Package-List:
 hostapd deb net optional arch=linux-any,kfreebsd-any
 wpagui deb net optional arch=linux-any,kfreebsd-any
 wpasupplicant deb net optional arch=linux-any,kfreebsd-any
 wpasupplicant-udeb udeb debian-installer standard arch=linux-any
Checksums-Sha1:
 ab85ae8b6a36ae063537c1bd253742b9950c7a37 2009476 wpa_2.6.orig.tar.xz
 99e48b5a221bc5e67675bec12fbd5fa9c52bd6f6 102112 wpa_2.6-18.debian.tar.xz
Checksums-Sha256:
 4492629ea15c9b571ac5e41679dca6703a25b637828272a0e72f3349dd1b4eac 2009476 wpa_2.6.orig.tar.xz
 5c8a1bd40461a17a0fdc6a145990ea6ca63d888e1f49f9245c1edf29e2530256 102112 wpa_2.6-18.debian.tar.xz
Files:
 a4f338bb230895a03182d59222e79a87 2009476 wpa_2.6.orig.tar.xz
 66dcea7d7d2b901fc7a18fd7c7a977cd 102112 wpa_2.6-18.debian.tar.xz
Dgit: 4d39aa61616103a00fbf99d23e7295517d2d1d68 debian archive/debian/2%2.6-18 https://git.dgit.debian.org/wpa

-----BEGIN PGP SIGNATURE-----

iQEzBAEBCAAdFiEEeuS9ZL8A0js0NGiOXkCM2RzYOdIFAltrWCUACgkQXkCM2RzY
OdLAqAgAn/kDRt5dKYszcSsQEt+Uq0Oe984G3wwyXX/frA9uO+CbIlE6j49ZRQuX
wqK0BbaikfaTIw61MRV2OpubbwhamKgkM9fIky9wPqzzyAObr7z5xoUe7vr9qcAn
gbrziNoaA3qRYcFjA6jFzXT4BfJRXqkTUPpwlJiNlZG+F/aX9EkkM3Ros5ANmRHT
c1UWKs5VtINODvS05xrhsdCls6cdhhpvayiggWXqkvH2mAEs06FG1eOoiKxfGMp3
JpjYL0OpzJ806zc2/H2bd73XivlAw5+ZbCCLBxaBAJ9a9/jXChF2BvVMo6WSClvP
fWCy5o/JZc7MiNSYlTZuXRhp5G4MVw==
=saM7
-----END PGP SIGNATURE-----
