pkgname = "geany"
pkgver = "2.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "glib-devel",
    "gettext",
    "gmake",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
checkdepends = ["bash"]
depends = ["desktop-file-utils"]
pkgdesc = "Gtk+3 IDE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://geany.org"
source = f"https://github.com/geany/geany/releases/download/{pkgver}/geany-{pkgver[:-2]}.tar.gz"
sha256 = "50d28a45ac9b9695e9529c73fe7ed149edb512093c119db109cea6424114847f"


@subpackage("geany-devel")
def _devel(self):
    return self.default_devel()