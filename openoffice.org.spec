# NOTE:
#	- normal build requires little less than 4GB of disk space
#	- full debug build requires about 9GB of disk space
# TODO:
#	- drop requirement on nas-devel
#	- fix locale names and other locale related things
#	- --with-system-myspell + myspell package as in Debian
#	- --with-system-neon - check compilation (works with 0.23 but not 0.24)
#	- in gtk version menu highlight has almost the same colour as menu text
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- remove oohtml symlink (there is ooweb),
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)
# 	- add lang: rw (?)
#	- add %{_libdir}/%{name}/share/autocorr/acor_(ll)-(LL).dat files to package (marked with %lang)
#       - can't be just i18n-{be,gu,hi,kn,pa,ta} instead of *-{be_BY,*_IN}?

# Conditional build:
%bcond_with	java		# Java support
%bcond_with	vfs		# Enable GNOME VFS and Evolution 2 support

%define		ver		2.0
%define		rel		0
%define		ooobver		1.9.118
%define		snap		SRC680
%define		bver		m118
%define		subver		680

%define		fullver		%{ver}.%{rel}
%define		dfullver	%(echo %{fullver} | tr . _)
%define		ssnap		%(echo %{snap} | tr SRC src)
%define		specflags	-fno-strict-aliasing

Summary:	OpenOffice.org - powerful office suite
Summary(pl):	OpenOffice.org - pot�ny pakiet biurowy
Name:		openoffice.org
Version:	%{fullver}
Release:	0.5%{?with_vfs:vfs}
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://go-ooo.org/packages/%{snap}/ooo-build-%{ooobver}.tar.gz
# Source0-md5:	d0d56a537416473f7deed33947078de8
Source1:	http://go-ooo.org/packages/%{snap}/%{ssnap}-%{bver}-core.tar.bz2
# Source1-md5:	e5dbb456faf8c94e2acab8aae3f64511
Source2:	http://go-ooo.org/packages/%{snap}/%{ssnap}-%{bver}-system.tar.bz2
# Source2-md5:	2aad305908f01086b3dff896b3853e2e
Source3:	http://go-ooo.org/packages/%{snap}/%{ssnap}-%{bver}-binfilter.tar.bz2
# Source3-md5:	fd6abac76015952175f882d63f060506
Source4:	http://go-ooo.org/packages/%{snap}/%{ssnap}-%{bver}-lang.tar.bz2
# Source4-md5:	723806c4287f7ae77ae16eac3711492f
Source10:	http://go-ooo.org/packages/%{snap}/ooo_custom_images-13.tar.bz2
# Source10-md5:	2480af7f890c8175c7f9e183a1b39ed2
Source11:	http://go-ooo.org/packages/%{snap}/ooo_crystal_images-6.tar.bz2
# Source11-md5:	586d0f26b3f79d89bbb5b25b874e3df6
Source12:	http://go-ooo.org/packages/%{snap}/extras-2.tar.bz2
# Source12-md5:	733051ebeffae5232a2eb760162da020
Source13:	http://go-ooo.org/packages/libwpd/libwpd-0.8.0.tar.gz
# Source13-md5:	98e59beecc112339bb78654863304c1c
Source20:	oocalc.desktop
Source21:	oodraw.desktop
Source22:	ooffice.desktop
#Source23:	ooglobal.desktop
Source24:	ooimpress.desktop
Source25:	oomath.desktop
Source26:	ooprinteradmin.desktop
Source27:	oosetup.desktop
Source28:	ooweb.desktop
Source29:	oowriter.desktop

# we keep these in ooo-build repository
# PLD splash screen
#Source20:	%{name}-about.bmp
#Source21:	%{name}-intro.bmp

%define		cftp	http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib

# Help content
Source400:	%{cftp}/helpcontent/helpcontent_01_unix.tgz
# Source400-md5:	7da2aff674c2c84aba8b21ac2ab16bb6
Source401:	%{cftp}/helpcontent/helpcontent_31_unix.tgz
# Source401-md5:	c7e618e2d9b8bd25cae12954ef2548c9
Source402:	%{cftp}/helpcontent/helpcontent_33_unix.tgz
# Source402-md5:	68d58bc30b485a77c0a0fba08af3aee3
Source403:	%{cftp}/helpcontent/helpcontent_34_unix.tgz
# Source403-md5:	8696bbee3dc4d5b6fd60218123016e29
Source404:	%{cftp}/helpcontent/helpcontent_39_unix.tgz
# Source404-md5:	c2ae86d02f462d2b663d621190f5ef34
Source405:	%{cftp}/helpcontent/helpcontent_46_unix.tgz
# Source405-md5:	7b013981edce2fabe4a8751ff64a8d58
Source406:	%{cftp}/helpcontent/helpcontent_49_unix.tgz
# Source406-md5:	a39f44ec40f452c963a4a187f31d1acb
Source407:	%{cftp}/helpcontent/helpcontent_55_unix.tgz
# Source407-md5:	804d3ce61e11335193a410aaf9603f8e
Source408:	%{cftp}/helpcontent/helpcontent_81_unix.tgz
# Source408-md5:	81b705057a0e14ebcbf02fac4762781a
Source409:	%{cftp}/helpcontent/helpcontent_82_unix.tgz
# Source409-md5:	3121fbd251176d7c7b6e33ecec744c65
Source410:	%{cftp}/helpcontent/helpcontent_86_unix.tgz
# Source410-md5:	aee37935139c5ccd4b6d8abdd2037c66
Source411:	%{cftp}/helpcontent/helpcontent_88_unix.tgz
# Source411-md5:	3b00571318e45965dee0545d86306d65
Source412:	%{cftp}/helpcontent/helpcontent_90_unix.tgz
# Source412-md5:	9521a01c5817e87178f356762f8cdab5

Patch0:		%{name}-pld.patch

URL:		http://www.openoffice.org/
BuildRequires:	ImageMagick
BuildRequires:	STLport-devel >= 4.5.3-6
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-4
BuildRequires:	boost-devel
BuildRequires:	boost-spirit-devel
BuildRequires:	boost-mem_fn-devel
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
BuildRequires:	db-cxx-devel
BuildRequires:	db-devel
BuildRequires:	/usr/bin/getopt
%if %{with vfs}
BuildRequires:	gnome-vfs2-devel
%endif
%if %{with java}
BuildRequires:	db-java >= 4.2.52-4
BuildRequires:	jar
BuildRequires:	jdk
%else
BuildRequires:	libxslt-progs
%endif
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	gtk+2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	nss-devel >= 1:3.10
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.3
BuildRequires:	mozilla-devel >= 5:1.7.6-2
BuildRequires:	nas-devel
BuildRequires:	neon-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	perl-Archive-Zip
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	python >= 2.2
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	sablotron-devel
BuildRequires:	sane-backends-devel
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tcsh
BuildRequires:	unixODBC-devel
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildConflicts:	java-sun = 1.4.2
Requires(post,postun):	fontpostinst
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	cups-lib
Requires:	db
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	sed
#Suggested:	chkfontpath
ExclusiveArch:	%{ix86} ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice.org is an open-source project sponsored by Sun Microsystems
and hosted by CollabNet. In October of 2000, Sun released the source
code of its popular StarOfficeTM productivity suite under open-source
licenses. The aim of the OpenOffice.org project is to create, using
open-source methods, the next generation of open-network productivity
services, including the establishment of open, XML-based standards for
office productivity file formats and language-independent bindings to
component APIs.

Features of OpenOffice.org include:
 - Downloadable source code,
 - CVS control, and
 - Infrastructure for community involvement, including guidelines and
   discussion groups.

%description -l pl
OpenOffice.org jest projektem open-source sponsorowanym przez Sun
Microsystems i przechowywanym przez CollabNet. W pa�dzierniku 2000
roku Sun udost�pni� kod �r�d�owy popularnego pakietu biurowego
StarOfficeTM na zasadach licencji open-source. G��wnym celem
OpenOffice.org jest stworzenie sieciowego pakietu biurowego nast�pnej
generacji, wykorzystuj�c open-source'owe metody pracy.

Do zalet OpenOffice.org mo�na zaliczy�:
 - dost�pny ca�y czas kod �r�d�owy,
 - kontrola CVS,
 - infrastruktura s�u��ca do komunikowania si� w ramach projektu.

%package libs
Summary:	OpenOffice.org shared libraries
Summary(pl):	Biblioteki dzielone OpenOffice.org
Group:		X11/Libraries
Obsoletes:	openoffice-libs

%description libs
OpenOffice.org productivity suite - shared libraries.

%description libs -l pl
Pakiet biurowy OpenOffice.org - biblioteki.

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-libs-kde

%description libs-kde
OpenOffice.org productivity suite - KDE Interface.

%description libs-kde -l pl
Pakiet biurowy OpenOffice.org - Interfejs KDE.

%package libs-gtk
Summary:	OpenOffice.org GTK+ Interface
Summary(pl):	Interfejs GTK+ dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-libs-gtk

%description libs-gtk
OpenOffice.org productivity suite - GTK+ Interface.

%description libs-gtk -l pl
Pakiet biurowy OpenOffice.org - Interfejs GTK+.

%package i18n-af
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl):	OpenOffice.org - interfejs w j�zyku afrykanerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
afrykanerskim.

%files i18n-af -f af.lang

%package i18n-ar
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w j�zyku arabskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde

%description i18n-ar
This package provides resources containing menus and dialogs in
Arabic language.

%description i18n-ar -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
arabskim.

%files i18n-ar -f ar.lang

%package i18n-be_BY
Summary:	OpenOffice.org - interface in Belarusian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku bia�oruskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-be_BY
This package provides resources containing menus and dialogs in
Belarusian language.

%description i18n-be_BY -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
bia�oruskim.

%files i18n-be_BY -f be-BY.lang

%package i18n-bg
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku bu�garskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
bu�garskim.

%files i18n-bg -f bg.lang

%package i18n-bn
Summary:	OpenOffice.org - interface in Bangla language
Summary(pl):	OpenOffice.org - interfejs w j�zyku bengalskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bn
This package provides resources containing menus and dialogs in
Bangla language.

%description i18n-bn -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
bengalskim.

%files i18n-bn -f bn.lang

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w j�zyku katalo�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
katalo�skim.

%files i18n-ca -f ca.lang

%package i18n-cs
Summary:	OpenOffice.org - interface in Czech language
Summary(pl):	OpenOffice.org - interfejs w j�zyku czeskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde

%description i18n-cs
This package provides resources containing menus and dialogs in
Czech language.

%description i18n-cs -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
czeskim.

%files i18n-cs -f cs.lang

%package i18n-cy
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl):	OpenOffice.org - interfejs w j�zyku walijskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
walijskim.

%files i18n-cy -f cy.lang

%package i18n-da
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku du�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde

%description i18n-da
This package provides resources containing menus and dialogs in
Danish language.

%description i18n-da -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
du�skim.

%files i18n-da -f da.lang

%package i18n-de
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w j�zyku niemieckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde

%description i18n-de
This package provides resources containing menus and dialogs in
German language.

%description i18n-de -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
niemieckim.

%files i18n-de -f de.lang

%package i18n-el
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w j�zyku greckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde

%description i18n-el
This package provides resources containing menus and dialogs in
Greek language.

%description i18n-el -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
greckim.

%files i18n-el -f el.lang

%package i18n-en_GB
Summary:	OpenOffice.org - interface in English language for United Kingdom
Summary(pl):	OpenOffice.org - interfejs w j�zyku anglieskim dla Wielkiej Brytanii
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-en_GB
This package provides resources containing menus and dialogs in
English language for United Kingdom.

%description i18n-en_GB -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
anglieskim dla Wielkiej Brytanii.

%files i18n-en_GB -f en-GB.lang

%package i18n-eo
Summary:	OpenOffice.org - interface in Esperanto language
Summary(pl):	OpenOffice.org - interfejs w j�zyku esperanto
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-eo
This package provides resources containing menus and dialogs in
Esperanto language.

%description i18n-eo -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
esperanto.

%files i18n-eo -f eo.lang

%package i18n-es
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku hiszpa�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
hiszpa�skim.

%files i18n-es -f es.lang

%package i18n-et
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku esto�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
esto�skim.

%files i18n-et -f et.lang

%package i18n-eu
Summary:	OpenOffice.org - interface in Basque (Euskara) language
Summary(pl):	OpenOffice.org - interfejs w j�zyku baskijskim (euskera)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde

%description i18n-eu
This package provides resources containing menus and dialogs in
Basque (Euskara) language.

%description i18n-eu -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
baskijskim (euskera).

%files i18n-eu -f eu.lang

%package i18n-fi
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku fi�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
fi�skim.

%files i18n-fi -f fi.lang

%package i18n-fo
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl):	OpenOffice.org - interfejs w j�zyku farerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde

%description i18n-fo
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
farerskim.

#%files i18n-fo -f fo.lang

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w j�zyku francuskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde

%description i18n-fr
This package provides resources containing menus and dialogs in
French language.

%description i18n-fr -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
francuskim.

%files i18n-fr -f fr.lang

%package i18n-ga
Summary:	OpenOffice.org - interface in Irish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku irlandzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde

%description i18n-ga
This package provides resources containing menus and dialogs in
Irish language.

%description i18n-ga -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
irlandzkim.

#%files i18n-ga-f ga.lang

%package i18n-gl
Summary:	OpenOffice.org - interface in Galician language
Summary(pl):	OpenOffice.org - interfejs w j�zyku galicyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
galicyjskim.

%files i18n-gl -f gl.lang

%package i18n-gu_IN
Summary:	OpenOffice.org - interface in Gujarati language
Summary(pl):	OpenOffice.org - interfejs w j�zyku gud�arati
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-gu_IN
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu_IN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
gud�arati.

%files i18n-gu_IN -f gu-IN.lang

%package i18n-he
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl):	OpenOffice.org - interfejs w j�zyku hebrajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde

%description i18n-he
This package provides resources containing menus and dialogs in
Hebrew language.

%description i18n-he -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
hebrajskim.

%files i18n-he -f he.lang

%package i18n-hi_IN
Summary:	OpenOffice.org - interface in Hindi language
Summary(pl):	OpenOffice.org - interfejs w j�zyku hindi
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-kde

%description i18n-hi_IN
This package provides resources containing menus and dialogs in
Hindi language.

%description i18n-hi_IN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
hindi.

%files i18n-hi_IN -f hi-IN.lang

%package i18n-hr
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku chorwackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
chorwackim.

%files i18n-hr -f hr.lang

%package i18n-hu
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku w�gierskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
w�gierskim.

%files i18n-hu -f hu.lang

%package i18n-ia
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl):	OpenOffice.org - interfejs w j�zyku interlingua
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde

%description i18n-ia
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
interlingua.

#%files i18n-ia -f ia.lang

%package i18n-id
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku indonezyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
indonezyjskim.

#%files i18n-id -f id.lang

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku w�oskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-it
ObsoleteS:	openoffice-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
w�oskim.

%files i18n-it -f it.lang

%package i18n-ja
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w j�zyku japo�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde

%description i18n-ja
This package provides resources containing menus and dialogs in
Japan language.

%description i18n-ja -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
japo�skim.

%files i18n-ja -f ja.lang

%package i18n-km
Summary:	OpenOffice.org - interface in Khmer language
Summary(pl):	OpenOffice.org - interfejs w j�zyku khmerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-km
This package provides resources containing menus and dialogs in
Khmer language.

%description i18n-km -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
khmerskim.

%files i18n-km -f km.lang

%package i18n-kn_IN
Summary:	OpenOffice.org - interface in Kannada language
Summary(pl):	OpenOffice.org - interfejs w j�zyku kannara
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde

%description i18n-kn_IN
This package provides resources containing menus and dialogs in
Kannada language.

%description i18n-kn_IN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
kannara.

%files i18n-kn_IN -f kn-IN.lang

%package i18n-ko
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w j�zyku korea�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde

%description i18n-ko
This package provides resources containing menus and dialogs in
Korean language.

%description i18n-ko -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
korea�skim.

%files i18n-ko -f ko.lang

%package i18n-la
Summary:	OpenOffice.org - interface in Latin language
Summary(pl):	OpenOffice.org - interfejs w j�zyku �aci�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde

%description i18n-la
This package provides resources containing menus and dialogs in
Latin language.

%description i18n-la -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
�aci�skim.

#%files i18n-la -f la.lang

%package i18n-lt
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku litewskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
litewskim.

%files i18n-lt -f lt.lang

%package i18n-med
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl):	OpenOffice.org - interfejs w j�zyku melpa
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde

%description i18n-med
This package provides resources containing menus and dialogs in
Melpa language.

%description i18n-med -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
melpa.

#%files i18n-med -f med.lang

%package i18n-mi
Summary:	OpenOffice.org - interface in Maori language
Summary(pl):	OpenOffice.org - interfejs w j�zyku maoryjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde

%description i18n-mi
This package provides resources containing menus and dialogs in
Maori language.

%description i18n-mi -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
maoryjskim.

#%files i18n-mi -f mi.lang

%package i18n-ms
Summary:	OpenOffice.org - interface in Malay language
Summary(pl):	OpenOffice.org - interfejs w j�zyku malajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ms
Obsoletes:	openoffice-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-kde

%description i18n-ms
This package provides resources containing menus and dialogs in
Malay language.

%description i18n-ms -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
malajskim.

%files i18n-ms -f ms.lang

%package i18n-nb
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl):	OpenOffice.org - interfejs w j�zyku norweskim (odmiana Bokmaal)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
norweskim w odmianie Bokmaal.

%files i18n-nb -f nb.lang

%package i18n-nl
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w j�zyku holenderskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde

%description i18n-nl
This package provides resources containing menus and dialogs in
Dutch language.

%description i18n-nl -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
holenderskim.

%files i18n-nl -f nl.lang

%package i18n-nn
Summary:	OpenOffice.org - interface in Norwegian Nynorsk language
Summary(pl):	OpenOffice.org - interfejs w j�zyku norweskim (odmiana Nynorsk)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde

%description i18n-nn
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
norweskim w odmianie Nynorsk.

%files i18n-nn -f nn.lang

%package i18n-nso
Summary:	OpenOffice.org - interface in Northern Sotho language
Summary(pl):	OpenOffice.org - interfejs w j�zyku ludu Soto
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde

%description i18n-nso
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
ludu Soto.

%files i18n-nso -f ns.lang

%package i18n-pa_IN
Summary:	OpenOffice.org - interface in Punjabi language
Summary(pl):	OpenOffice.org - interfejs w j�zyku pend�abskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-pa_IN
This package provides resources containing menus and dialogs in
Punjabi language.

%description i18n-pa_IN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
pend�abskim.

%files i18n-pa_IN -f pa-IN.lang

%package i18n-pl
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku polskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde

%description i18n-pl
This package provides resources containing menus and dialogs in
Polish language.

%description i18n-pl -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
polskim.

%files i18n-pl -f pl.lang

%package i18n-pt
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w j�zyku portugalskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
portugalskim.

%files i18n-pt -f pt.lang

%package i18n-pt_BR
Summary:	OpenOffice.org - interface in Brazilian Portuguese language
Summary(pl):	OpenOffice.org - interfejs w j�zyku portugalskim dla Brazylii
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
portugalskim dla Brazylii.

%files i18n-pt_BR -f pt-BR.lang

%package i18n-ro
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku rumu�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
rumu�skim.

#%files i18n-ro -f ro.lang

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku rosyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
rosyjskim.

%files i18n-ru -f ru.lang

%package i18n-rw
Summary:	OpenOffice.org - interface in Kinarwanda language
Summary(pl):	OpenOffice.org - interfejs w j�zyku kinya-ruanda
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-rw
This package provides resources containing menus and dialogs in
Kinarwanda language.

%description i18n-rw -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
kinya-ruanda.

%files i18n-ro -f rw.lang

%package i18n-sk
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl):	OpenOffice.org - interfejs w j�zyku s�owackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde

%description i18n-sk
This package provides resources containing menus and dialogs in
Slovak language.

%description i18n-sk -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
s�owackim.

%files i18n-sk -f sk.lang

%package i18n-sl
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku s�owe�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
s�owe�skim.

%files i18n-sl -f sl.lang

%package i18n-sv
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku szwedzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
szwedzkim.

%files i18n-sv -f sv.lang

%package i18n-ta_IN
Summary:	OpenOffice.org - interface in Tamil language
Summary(pl):	OpenOffice.org - interfejs w j�zyku tamiskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ta_IN
This package provides resources containing menus and dialogs in
Tamil language.

%description i18n-ta_IN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
tamilskim.

%files i18n-ta_IN -f ta-IN.lang

%package i18n-th
Summary:	OpenOffice.org - interface in Thai language
Summary(pl):	OpenOffice.org - interfejs w j�zyku tajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde

%description i18n-th
This package provides resources containing menus and dialogs in
Thai language.

%description i18n-th -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
tajskim.

%files i18n-th -f th.lang

%package i18n-tn
Summary:	OpenOffice.org - interface in Tswana language
Summary(pl):	OpenOffice.org - interfejs w j�zyku tswana
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde

%description i18n-tn
This package provides resources containing menus and dialogs in
Tswana language.

%description i18n-tn -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
tswana.

%files i18n-tn -f tn.lang

%package i18n-tr
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w j�zyku tureckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}-:%{version}-%{release}
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
tureckim.

%files i18n-tr -f tr.lang

%package i18n-uk
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl):	OpenOffice.org - interfejs w j�zyku ukrai�skim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
ukrai�skim.

#%files i18n-uk -f uk.lang

%package i18n-vi
Summary:	OpenOffice.org - interface in Vietnamese language
Summary(pl):	OpenOffice.org - interfejs w j�zyku wietnamskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-vi
This package provides resources containing menus and dialogs in
Vietnamese language.

%description i18n-vi -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
wietnamskim.

%files i18n-vi -f vi.lang

%package i18n-xh
Summary:	OpenOffice.org - interface in Xhosa language
Summary(pl):	OpenOffice.org - interfejs w j�zyku khosa
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-xh
This package provides resources containing menus and dialogs in
Xhosa language.

%description i18n-xh -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
khosa.

%files i18n-xh -f xh.lang

%package i18n-zh_CN
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w j�zyku chi�skim dla Chin
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
chi�skim dla Chin.

%files i18n-zh_CN -f zh-CN.lang

%package i18n-zh_TW
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w j�zyku chi�skim dla Tajwanu
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
chi�skim dla Tajwanu.

%files i18n-zh_TW -f zh-TW.lang

%package i18n-zu
Summary:	OpenOffice.org - interface in Zulu language
Summary(pl):	OpenOffice.org - interfejs w j�zyku zuluskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde

%description i18n-zu
This package provides resources containing menus and dialogs in
Zulu language.

%description i18n-zu -l pl
Ten pakiet dostarcza zasoby zawieraj�ce menu i okna dialogowe w j�zyku
zuluskim.

%files i18n-zu -f zu.lang

%prep
%setup -q -n ooo-build-%{ooobver}
#%patch0 -p1

install -d src
# sources, icons, KDE_icons
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} src
# help files
ln -sf %{SOURCE400} %{SOURCE401} %{SOURCE402} %{SOURCE403} %{SOURCE404} \
	%{SOURCE405} %{SOURCE406} %{SOURCE407} %{SOURCE408} %{SOURCE409} \
	%{SOURCE410} %{SOURCE411} %{SOURCE412} src

# we keep these in ooo-build repository
#ln -s %{SOURCE20} src/openabout_pld.bmp
#ln -s %{SOURCE21} src/openintro_pld.bmp

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -r /proc/cpuinfo ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

%ifarch %{x8664} sparc64 ppc64 alpha
DISTRO="PLD64"
%else
DISTRO="PLD"
%endif

CC="%{__cc}"
CXX="%{__cxx}"
ENVCFLAGS="%{rpmcflags}"
ENVCFLAGSCXX="%{rpmcflags}"
DESTDIR=$RPM_BUILD_ROOT
IGNORE_MANIFEST_CHANGES=1
QTINC="%{_includedir}/qt"
QTLIB="%{_libdir}"
export CC CXX ENVCFLAGS ENVCFLAGSCXX DESTDIR IGNORE_MANIFEST_CHANGES DISTRO QTINC QTLIB

%if %{with java}
GCJ=gcj
JAVA_HOME=%{_libdir}/java
DB_JAR="%{_javadir}/db.jar"
export JAVA_HOME DB_JAR GCJ
%endif

DEFAULT_TO_ENGLISH_FOR_PACKING=1; export DEFAULT_TO_ENGLISH_FOR_PACKING

RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g' | xargs)"
[ "$RPM_BUILD_NR_THREADS" = "%{__make}" ] && RPM_BUILD_NR_THREADS=1

CONFOPTS=" \
%ifarch %{ix86} \
	--with-arch=x86 \
%endif
%ifarch ppc
	--with-arch=ppc \
%endif
%ifarch sparc sparcv9
	--with-arch=sparc \
%endif
	--with-ccache-allowed \
	--with-system-gcc \
	--with-system-zlib \
	--with-system-jpeg \
	--with-system-libxml \
	--with-system-python \
	--with-system-sane-headers \
	--with-system-x11-extensions-headers \
	--with-system-odbc-headers \
	--with-system-db \
	--with-system-curl \
	--with-system-freetype \
	--with-system-nas \
	--with-system-xrender \
	--with-system-expat \
	--with-system-sablot \
	--with-system-boost \
	--with-system-neon \
	--with-system-mozilla \
	--with-dynamic-xinerama \
	--with-vendor="${DISTRO}" \
	--with-distro="${DISTRO}" \
	--enable-gtk \
	--enable-kde \
	--without-binsuffix \
	--with-installed-ooo-dirname=%{name} \
	--with-lang=ALL \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
%else
	--without-java \
%endif
%if %{with vfs}
	--enable-gnome-vfs \
%else
	--disable-gnome-vfs \
%endif
	--with-docdir=%{_docdir}/%{name}-%{version} \
	--with-python=%{_bindir}/python \
	--with-stlport4=/usr \
	--with-x \
	--without-fonts \
	--without-gpc \
	--disable-epm \
	--disable-fontooo \
	--enable-openldap \
	--enable-cups \
	--enable-fontconfig \
	--enable-libsn \
	--enable-libart \
	--disable-rpath \
%if 0%{?debug:1}
	--enable-debug \
	--enable-crashdump=yes \
	--enable-symbols=FULL \
%else
	--enable-crashdump=no \
	--disable-symbols \
%endif
	--with-num-jobs=$RPM_BUILD_NR_THREADS
"

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# build-ooo script will pickup these
CONFIGURE_OPTIONS="$CONFOPTS"; export CONFIGURE_OPTIONS

:> distro-configs/Common.conf
:> distro-configs/Common.conf.in
echo "$CONFOPTS" > distro-configs/${DISTRO}.conf

# main build
%configure \
	$CONFOPTS

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
%{__make} -j1

# hack for parallel build
if [ "$RPM_BUILD_NCPUS" -gt 1 ]; then
	doit=1
	while [ "$doit" -eq 1 ]; do
		echo "Waiting one more time..."
		FCH=$(nice -n 20 find . -type f ! -mmin +3 -print 2> /dev/null | wc -l)
		[ "$FCH" -eq 0 ] && doit=0 || sleep 30
	done
fi

%install
rm -rf $RPM_BUILD_ROOT

# limit to single process installation, it's safe at least
sed -i -e 's#^BUILD_NCPUS=.*#BUILD_NCPUS=1#g' bin/setup

DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
TMP="%{tmpdir}"; export TMP
TEMP="%{tmpdir}"; export TEMP
DEFAULT_TO_ENGLISH_FOR_PACKING=1; export DEFAULT_TO_ENGLISH_FOR_PACKING

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE20} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE21} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE22} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE23} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE24} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE25} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE26} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE27} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE28} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE29} $RPM_BUILD_ROOT%{_desktopdir}

# Add in the regcomp tool since some people need it for 3rd party add-ons
cp -f build/src%{subver}-%{bver}/solver/%{subver}/unxlng*.pro/bin/regcomp $RPM_BUILD_ROOT%{_libdir}/%{name}/program

# fix python
sed -i -e 's|#!/bin/python|#!%{_bindir}/python|g' $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.py

# Really needed?
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/kde
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/cde
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/gnome
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/icons
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome

# Remove dictionaries (in separate pkg)
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/*
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/dictionary.lst

# OOo should not install the Vera fonts, they are Required: now
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/fonts/truetype/*

# Copy fixed OpenSymbol to correct location
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
install fonts/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

# We don't need spadmin (gtk) or the setup application
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/setup
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/crash_report.bin
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-setup.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-printeradmin.desktop

#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/gnomeint

# some libs creep in somehow
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstl*.so*
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libsndfile*

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/sopatchlevel.sh
perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup

# Remove setup log
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup.log

# Remove copied system libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libgcc_s.so* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstdc++*so*

# Find out locales
rm -f *.lang*
langlist="`ls build/lang_*_list.txt|sed -e 's=build/lang_\(.*\)_list.txt=\1=g'`"

for lang in $langlist; do
	echo "%%defattr(644,root,root,755)" > ${lang}.lang

	# help files
	if [ -f build/help_${lang}_list.txt ]; then
		cat build/help_${lang}_list.txt >> ${lang}.lang
	fi

	lfile="build/lang_${lang}_list.txt"
	if [ -f ${lfile} ]; then
		lprefix="`bin/openoffice-xlate-lang -p ${lang} 2>/dev/null || echo ""`"
		longlang="`bin/openoffice-xlate-lang -l ${lang} 2>/dev/null || echo ""`"
		# share/*/${longlang}
		if [ "x${longlang}" != "x" ] ; then 
			grep "^%%dir.*/${longlang}/\$" ${lfile} > tmp.lang || :
		fi
		# share/registry/res/${lang} (but en-US for en)
		grep "^%%dir.*/res/${lang}[^/]*/\$" ${lfile} >> tmp.lang || :
		# ... translate %dir into whole tree, handle special wordbook/english case
		sed -e 's,^%%dir ,,;s,\(wordbook/english/\)$,\1soffice.dic,;s,/$,,' tmp.lang >> ${lang}.lang || :
		# share/autocorr/acor${somecodes}.dat (if exist)
		grep '/autocorr/acor.*dat$' ${lfile} >> ${lang}.lang || :
		# user/config/* (if exist, without parent directory)
		grep '/user/config/..*' ${lfile} >> ${lang}.lang || :
		grep "/licenses/LICENSE_${lang}" ${lfile} >> ${lang}.lang || :
		grep "/readmes/README_${lang}" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/presers/config/*.so[cdegh]
		grep "/presets/config/.*_${lang}\.so[cdegh]$" ${lfile} >> ${lang}.lang || :
		if [ "x${lprefix}" != "x" ] ; then
			grep "/presets/config/${lprefix}.*\.so[cdegh]$" ${lfile} >> ${lang}.lang || :
		fi
		# lib/openoffice.org/program/resource/*.res
		grep "/program/resource/.*${lang}.res$" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/autocorr/*.dat
		grep "/share/autocorr/.*${lang}.dat$" ${lfile} >> ${lang}.lang || :
		grep -i "/share/autocorr/.*${lang}-${lang}.dat$" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/autotext/$lang
		grep "/share/autotext/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/autotext/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/registry/res/$lang
		grep "/share/registry/res/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/registry/res/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}$" build/common_list.txt >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}/" build/common_list.txt >> ${lang}.lang || :
		# lib/openoffice.org/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${lang}.lang || :
	fi
done

echo "%{_libdir}/%{name}/presets/config/*_hun.*" >> hu.lang
echo "%{_libdir}/%{name}/presets/config/*_pol.*" >> pl.lang
echo "%{_libdir}/%{name}/presets/config/*_rus.*" >> ru.lang
echo "%{_libdir}/%{name}/presets/config/*_hun.*" >> hu.lang

find $RPM_BUILD_ROOT -type f -name '*.so' -exec chmod 755 "{}" ";"
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg
rm -rf $RPM_BUILD_ROOT/opt/gnome

%if %{without java}
# Java-releated bits
rm -f $RPM_BUILD_ROOT%{_sbin}/oojvmsetup
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/javascript
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/beanshell
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xslt
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:

%post libs
fontpostinst TTF

%postun libs
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%dir %{_sysconfdir}/openoffice.org

%attr(755,root,root) %{_libdir}/%{name}/install-dict

%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
#%{_libdir}/%{name}/program/user_registry.xsl
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
#%{_libdir}/%{name}/program/instdb.ins
%dir %{_libdir}/%{name}/program/resource
%dir %{_libdir}/%{name}/licenses
%dir %{_libdir}/%{name}/readmes

#%dir %{_libdir}/%{name}/help
#%{_libdir}/%{name}/help/en
#%{_libdir}/%{name}/help/main_transform.xsl

%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/autocorr
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/basic
#%dir %{_libdir}/%{name}/share/bookmark
%dir %{_libdir}/%{name}/share/config
%{_libdir}/%{name}/share/config/symbol
%{_libdir}/%{name}/share/config/webcast
%{_libdir}/%{name}/share/config/*.xpm
%{_libdir}/%{name}/share/config/images.zip
%{_libdir}/%{name}/share/config/images_crystal.zip
%{_libdir}/%{name}/share/config/images_industrial.zip
%{_libdir}/%{name}/share/config/images_hicontrast.zip
%{_libdir}/%{name}/share/config/soffice.cfg
%{_libdir}/%{name}/share/config/wizard
#%dir %{_libdir}/%{name}/share/database
%dir %{_libdir}/%{name}/share/dict
%dir %{_libdir}/%{name}/share/dict/ooo
%{_libdir}/%{name}/share/dtd
%{_libdir}/%{name}/share/fonts
%{_libdir}/%{name}/share/gallery
%{_libdir}/%{name}/share/psprint
%dir %{_libdir}/%{name}/share/samples
%dir %{_libdir}/%{name}/share/template
%dir %{_libdir}/%{name}/share/wordbook
#%dir %{_libdir}/%{name}/share/wordbook/english
#%{_libdir}/%{name}/share/wordbook/english/sun.dic
%{_libdir}/%{name}/share/readme

%dir %{_libdir}/%{name}/share/registry
%dir %{_libdir}/%{name}/share/registry/res
%{_libdir}/%{name}/share/registry/data
%{_libdir}/%{name}/share/registry/schema
%{_libdir}/%{name}/share/registry/ldap
# split ?
%{_libdir}/%{name}/share/registry/modules

#%{_libdir}/%{name}/share/autotext/english
# XXX: in ooo-build only template/english/wizard/bitmaps is in main?
#%{_libdir}/%{name}/share/template/english
%ghost %{_libdir}/%{name}/share/dict/ooo/dictionary.lst

%dir %{_libdir}/%{name}/presets
%dir %{_libdir}/%{name}/presets/autotext
%{_libdir}/%{name}/presets/autotext/mytexts.bau
%{_libdir}/%{name}/presets/basic
%dir %{_libdir}/%{name}/presets/config
%{_libdir}/%{name}/presets/config/autotbl.fmt
%{_libdir}/%{name}/presets/config/arrowhd.soe
%{_libdir}/%{name}/presets/config/classic.sog
%{_libdir}/%{name}/presets/config/cmyk.soc
%{_libdir}/%{name}/presets/config/gallery.soc
%{_libdir}/%{name}/presets/config/hatching.soh
%{_libdir}/%{name}/presets/config/html.soc
%{_libdir}/%{name}/presets/config/modern.sog
%{_libdir}/%{name}/presets/config/palette.soc
%{_libdir}/%{name}/presets/config/standard.so?
%{_libdir}/%{name}/presets/config/styles.sod
%{_libdir}/%{name}/presets/config/sun-color.soc
%{_libdir}/%{name}/presets/config/web.soc
%{_libdir}/%{name}/presets/config/Classico.sog
%{_libdir}/%{name}/presets/config/Linhas.sod
%{_libdir}/%{name}/presets/config/Palheta.soc
%{_libdir}/%{name}/presets/config/PreenchimentoDePadrao.soh
%{_libdir}/%{name}/presets/config/Ptseta.soe
%{_libdir}/%{name}/presets/config/Vigente.sog
%{_libdir}/%{name}/presets/config/actual.sog
%{_libdir}/%{name}/presets/config/aktuell.sog
%{_libdir}/%{name}/presets/config/arcer.soh
%{_libdir}/%{name}/presets/config/arrowhead.soe
%{_libdir}/%{name}/presets/config/cary.sod
%{_libdir}/%{name}/presets/config/chic.sod
%{_libdir}/%{name}/presets/config/clasico.sog
%{_libdir}/%{name}/presets/config/classico.sog
%{_libdir}/%{name}/presets/config/classique.sog
%{_libdir}/%{name}/presets/config/color.soc
%{_libdir}/%{name}/presets/config/colore.soc
%{_libdir}/%{name}/presets/config/colours.soc
%{_libdir}/%{name}/presets/config/contemporary.sog
%{_libdir}/%{name}/presets/config/cor.soc
%{_libdir}/%{name}/presets/config/couleur.soc
%{_libdir}/%{name}/presets/config/drawstyles.sod
%{_libdir}/%{name}/presets/config/einden.soe
%{_libdir}/%{name}/presets/config/elegant.sog
%{_libdir}/%{name}/presets/config/enden.soe
%{_libdir}/%{name}/presets/config/estilos.sod
%{_libdir}/%{name}/presets/config/estrem.soe
%{_libdir}/%{name}/presets/config/extrem.soe
%{_libdir}/%{name}/presets/config/faerg.soc
%{_libdir}/%{name}/presets/config/farben.soc
%{_libdir}/%{name}/presets/config/fimlinha.soe
%{_libdir}/%{name}/presets/config/finlinea.soe
%{_libdir}/%{name}/presets/config/formellt.sog
%{_libdir}/%{name}/presets/config/hachures.soh
%{_libdir}/%{name}/presets/config/hatch.soh
%{_libdir}/%{name}/presets/config/klasicky.sog
%{_libdir}/%{name}/presets/config/klasik.sog
%{_libdir}/%{name}/presets/config/klasika.sog
%{_libdir}/%{name}/presets/config/klassiek.sog
%{_libdir}/%{name}/presets/config/klassik.sog
%{_libdir}/%{name}/presets/config/klassisk.sog
%{_libdir}/%{name}/presets/config/linien.sod
%{_libdir}/%{name}/presets/config/moderne.sog
%{_libdir}/%{name}/presets/config/moderni.sog
%{_libdir}/%{name}/presets/config/moderno.sog
%{_libdir}/%{name}/presets/config/moderny.sog
%{_libdir}/%{name}/presets/config/modieus.sog
%{_libdir}/%{name}/presets/config/moenster.soh
%{_libdir}/%{name}/presets/config/nuevo.sog
%{_libdir}/%{name}/presets/config/palet.soc
%{_libdir}/%{name}/presets/config/paleta.soc
%{_libdir}/%{name}/presets/config/palete.soc
%{_libdir}/%{name}/presets/config/pilespds.soe
%{_libdir}/%{name}/presets/config/puscice.soe
%{_libdir}/%{name}/presets/config/schraffu.soh
%{_libdir}/%{name}/presets/config/singelo.sog
%{_libdir}/%{name}/presets/config/sipky.soe
%{_libdir}/%{name}/presets/config/skraver.soh
%{_libdir}/%{name}/presets/config/slogi.sod
%{_libdir}/%{name}/presets/config/slut.soe
%{_libdir}/%{name}/presets/config/sombread.soh
%{_libdir}/%{name}/presets/config/srafovani.soh
%{_libdir}/%{name}/presets/config/srafovanie.soh
%{_libdir}/%{name}/presets/config/srafure.soh
%{_libdir}/%{name}/presets/config/stijlen.sod
%{_libdir}/%{name}/presets/config/stil.sod
%{_libdir}/%{name}/presets/config/stili.sod
%{_libdir}/%{name}/presets/config/stilos.sod
%{_libdir}/%{name}/presets/config/streger.sod
%{_libdir}/%{name}/presets/config/styly.sod
%{_libdir}/%{name}/presets/config/tramas.soh
%{_libdir}/%{name}/presets/config/tratto.soh

%{_libdir}/%{name}/presets/database
%{_libdir}/%{name}/presets/gallery
%{_libdir}/%{name}/presets/psprint

#%{_libdir}/%{name}/presets/autotext/english

/etc/bash_completion.d/*

# Programs
%attr(755,root,root) %{_bindir}/oo*
%attr(755,root,root) %{_sbindir}/oopadmin
#%attr(755,root,root) %{_libdir}/%{name}/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/*.bin
#%attr(755,root,root) %{_libdir}/%{name}/program/fromtemplate
#%attr(755,root,root) %{_libdir}/%{name}/program/mozwrapper
#%attr(755,root,root) %{_libdir}/%{name}/program/nswrapper
#%attr(755,root,root) %{_libdir}/%{name}/program/ooovirg
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
#%attr(755,root,root) %{_libdir}/%{name}/program/python.sh
%attr(755,root,root) %{_libdir}/%{name}/program/pythonloader.unorc
#%attr(755,root,root) %{_libdir}/%{name}/program/pyunorc
%attr(755,root,root) %{_libdir}/%{name}/program/regcomp
#%attr(755,root,root) %{_libdir}/%{name}/program/sagenda
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
#%attr(755,root,root) %{_libdir}/%{name}/program/setup
%{_libdir}/%{name}/program/setuprc
#%attr(755,root,root) %{_libdir}/%{name}/program/sfax
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
#%attr(755,root,root) %{_libdir}/%{name}/program/slabel
#%attr(755,root,root) %{_libdir}/%{name}/program/sletter
#%attr(755,root,root) %{_libdir}/%{name}/program/smaster
%attr(755,root,root) %{_libdir}/%{name}/program/smath
#%attr(755,root,root) %{_libdir}/%{name}/program/smemo
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
#%attr(755,root,root) %{_libdir}/%{name}/program/svcard
#%attr(755,root,root) %{_libdir}/%{name}/program/sweb
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%attr(755,root,root) %{_libdir}/%{name}/program/open-url
%attr(755,root,root) %{_libdir}/%{name}/program/nsplugin
%attr(755,root,root) %{_libdir}/%{name}/program/gengal
%attr(755,root,root) %{_libdir}/%{name}/program/configimport
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%attr(755,root,root) %{_libdir}/%{name}/program/senddoc
%attr(755,root,root) %{_libdir}/%{name}/program/setofficelang
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/uri-encode
%attr(755,root,root) %{_libdir}/%{name}/program/viewdoc
%attr(755,root,root) %{_libdir}/%{name}/program/*.py

%if %{with java}
%attr(755,root,root) %{_sbindir}/oojvmsetup
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/jvmsetup
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%attr(755,root,root) %{_libdir}/%{name}/program/jvmfwk3rc
%{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/share/Scripts/beanshell
%{_libdir}/%{name}/share/Scripts/javascript
%{_libdir}/%{name}/share/xslt
%endif

%dir %{_libdir}/%{name}/share/Scripts
%{_libdir}/%{name}/share/Scripts/python

%{_datadir}/mime/packages/openoffice.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/o*.1*

# en-US
%{_libdir}/%{name}/share/autotext/en-US
%{_libdir}/%{name}/share/registry/res/en-US
%{_libdir}/%{name}/share/template/en-US
%{_libdir}/%{name}/share/wordbook/en-US
%{_libdir}/%{name}/program/resource/*en-US.res
%{_libdir}/%{name}/licenses/LICENSE_en-US
%{_libdir}/%{name}/licenses/LICENSE_en-US.html
%{_libdir}/%{name}/readmes/README_en-US
%{_libdir}/%{name}/readmes/README_en-US.html

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
#%dir %{_libdir}/%{name}/program/filter

%attr(755,root,root) %{_libdir}/%{name}/program/*.so
%exclude %{_libdir}/%{name}/program/libvclplug_gtk*.so
%exclude %{_libdir}/%{name}/program/libvclplug_kde*.so
%exclude %{_libdir}/%{name}/program/libfps_kde.so
#%exclude %{_libdir}/%{name}/program/libfps_gnome.so
%attr(755,root,root) %{_libdir}/%{name}/program/*.so.*
#%attr(755,root,root) %{_libdir}/%{name}/program/filter/*.so

%{_fontsdir}/TTF/*.ttf

%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfps_kde.so
%attr(755,root,root) %{_libdir}/%{name}/program/kde-open-url
#%dir %{_libdir}/%{name}/program/resource.kde

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url
#%attr(755,root,root) %{_libdir}/%{name}/program/libfps_gnome.so
#%dir %{_libdir}/%{name}/program/resource.gnome
