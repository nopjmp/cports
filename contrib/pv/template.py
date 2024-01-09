pkgname = "pv"
pkgver = "1.8.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel"]
pkgdesc = "Tool for monitoring the progress of data through a pipeline"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://www.ivarch.com/programs/pv.shtml"
source = f"https://www.ivarch.com/programs/sources/{pkgname}-{pkgver}.tar.gz"
sha256 = "d22948d06be06a5be37336318de540a2215be10ab0163f8cd23a20149647b780"