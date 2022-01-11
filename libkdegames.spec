#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkdegames
Version  : 21.12.1
Release  : 36
URL      : https://download.kde.org/stable/release-service/21.12.1/src/libkdegames-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/libkdegames-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/libkdegames-21.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GFDL-1.2 GPL-2.0 ISC LGPL-2.0 LGPL-2.1 MIT
Requires: libkdegames-data = %{version}-%{release}
Requires: libkdegames-lib = %{version}-%{release}
Requires: libkdegames-license = %{version}-%{release}
Requires: libkdegames-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdnssd-dev
BuildRequires : libsndfile-dev
BuildRequires : openal-soft-dev

%description
This directory contains the library for the kdegames package.
It is a collection of functions used by some games or which
are useful for other games.

%package data
Summary: data components for the libkdegames package.
Group: Data

%description data
data components for the libkdegames package.


%package dev
Summary: dev components for the libkdegames package.
Group: Development
Requires: libkdegames-lib = %{version}-%{release}
Requires: libkdegames-data = %{version}-%{release}
Provides: libkdegames-devel = %{version}-%{release}
Requires: libkdegames = %{version}-%{release}

%description dev
dev components for the libkdegames package.


%package lib
Summary: lib components for the libkdegames package.
Group: Libraries
Requires: libkdegames-data = %{version}-%{release}
Requires: libkdegames-license = %{version}-%{release}

%description lib
lib components for the libkdegames package.


%package license
Summary: license components for the libkdegames package.
Group: Default

%description license
license components for the libkdegames package.


%package locales
Summary: locales components for the libkdegames package.
Group: Default

%description locales
locales components for the libkdegames package.


%prep
%setup -q -n libkdegames-21.12.1
cd %{_builddir}/libkdegames-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641930618
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641930618
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdegames
cp %{_builddir}/libkdegames-21.12.1/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/libkdegames/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
cp %{_builddir}/libkdegames-21.12.1/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkdegames/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/libkdegames-21.12.1/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/libkdegames-21.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/libkdegames-21.12.1/LICENSES/ICS.txt %{buildroot}/usr/share/package-licenses/libkdegames/221e6be04f1b020e012e7bd9e9e39b86fda17ba2
cp %{_builddir}/libkdegames-21.12.1/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/libkdegames-21.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/libkdegames-21.12.1/src/carddecks/svg-konqi-modern/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9
cp %{_builddir}/libkdegames-21.12.1/src/carddecks/svg-standard/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4
cp %{_builddir}/libkdegames-21.12.1/src/carddecks/svg-tigullio-international/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886
cp %{_builddir}/libkdegames-21.12.1/src/carddecks/svg-xskat-french/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af
cp %{_builddir}/libkdegames-21.12.1/src/carddecks/svg-xskat-german/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0
pushd clr-build
%make_install
popd
%find_lang libkdegames5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/carddecks/svg-ancient-egyptians/11.png
/usr/share/carddecks/svg-ancient-egyptians/Ancient_Egyptians.svgz
/usr/share/carddecks/svg-ancient-egyptians/index.desktop
/usr/share/carddecks/svg-dondorf/11.png
/usr/share/carddecks/svg-dondorf/dondorf.svgz
/usr/share/carddecks/svg-dondorf/index.desktop
/usr/share/carddecks/svg-future/11.png
/usr/share/carddecks/svg-future/future.svgz
/usr/share/carddecks/svg-future/index.desktop
/usr/share/carddecks/svg-gm-paris/11.png
/usr/share/carddecks/svg-gm-paris/index.desktop
/usr/share/carddecks/svg-gm-paris/paris.svgz
/usr/share/carddecks/svg-jolly-royal/11.png
/usr/share/carddecks/svg-jolly-royal/index.desktop
/usr/share/carddecks/svg-jolly-royal/jolly-royal.svgz
/usr/share/carddecks/svg-konqi-modern/11.png
/usr/share/carddecks/svg-konqi-modern/index.desktop
/usr/share/carddecks/svg-konqi-modern/konqi.svgz
/usr/share/carddecks/svg-nicu-ornamental/11.png
/usr/share/carddecks/svg-nicu-ornamental/AUTHORS
/usr/share/carddecks/svg-nicu-ornamental/COPYING
/usr/share/carddecks/svg-nicu-ornamental/index.desktop
/usr/share/carddecks/svg-nicu-ornamental/ornamental.svgz
/usr/share/carddecks/svg-nicu-white/11.png
/usr/share/carddecks/svg-nicu-white/AUTHORS
/usr/share/carddecks/svg-nicu-white/COPYING
/usr/share/carddecks/svg-nicu-white/index.desktop
/usr/share/carddecks/svg-nicu-white/white.svgz
/usr/share/carddecks/svg-oxygen-air/11.png
/usr/share/carddecks/svg-oxygen-air/index.desktop
/usr/share/carddecks/svg-oxygen-air/oxygen-air.svgz
/usr/share/carddecks/svg-oxygen-white/11.png
/usr/share/carddecks/svg-oxygen-white/index.desktop
/usr/share/carddecks/svg-oxygen-white/oxygen-white.svgz
/usr/share/carddecks/svg-oxygen/11.png
/usr/share/carddecks/svg-oxygen/index.desktop
/usr/share/carddecks/svg-oxygen/oxygen.svgz
/usr/share/carddecks/svg-penguins/11.png
/usr/share/carddecks/svg-penguins/COPYRIGHT
/usr/share/carddecks/svg-penguins/index.desktop
/usr/share/carddecks/svg-penguins/penguins.svgz
/usr/share/carddecks/svg-standard/11.png
/usr/share/carddecks/svg-standard/index.desktop
/usr/share/carddecks/svg-standard/standard.svgz
/usr/share/carddecks/svg-tigullio-international/index.desktop
/usr/share/carddecks/svg-tigullio-international/queen-of-hearts.png
/usr/share/carddecks/svg-tigullio-international/tigullio-international.svgz
/usr/share/carddecks/svg-xskat-french/11.png
/usr/share/carddecks/svg-xskat-french/COPYRIGHT
/usr/share/carddecks/svg-xskat-french/french.svgz
/usr/share/carddecks/svg-xskat-french/index.desktop
/usr/share/carddecks/svg-xskat-german/11.png
/usr/share/carddecks/svg-xskat-german/COPYRIGHT
/usr/share/carddecks/svg-xskat-german/german.svgz
/usr/share/carddecks/svg-xskat-german/index.desktop
/usr/share/kconf_update/kgthemeprovider-migration.upd
/usr/share/qlogging-categories5/libkdegames.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KF5KDEGames/KGameClock
/usr/include/KF5/KF5KDEGames/KGamePopupItem
/usr/include/KF5/KF5KDEGames/KGameRenderedItem
/usr/include/KF5/KF5KDEGames/KGameRenderedObjectItem
/usr/include/KF5/KF5KDEGames/KGameRenderer
/usr/include/KF5/KF5KDEGames/KGameRendererClient
/usr/include/KF5/KF5KDEGames/KHighscore
/usr/include/KF5/KF5KDEGames/KScoreDialog
/usr/include/KF5/KF5KDEGames/KStandardGameAction
/usr/include/KF5/KF5KDEGames/KgAudioScene
/usr/include/KF5/KF5KDEGames/KgDeclarativeView
/usr/include/KF5/KF5KDEGames/KgDifficulty
/usr/include/KF5/KF5KDEGames/KgSound
/usr/include/KF5/KF5KDEGames/KgTheme
/usr/include/KF5/KF5KDEGames/KgThemeProvider
/usr/include/KF5/KF5KDEGames/KgThemeSelector
/usr/include/KF5/KF5KDEGames/highscore/khighscore.h
/usr/include/KF5/KF5KDEGames/highscore/kscoredialog.h
/usr/include/KF5/KF5KDEGames/kdegames_version.h
/usr/include/KF5/KF5KDEGames/kgameclock.h
/usr/include/KF5/KF5KDEGames/kgamepopupitem.h
/usr/include/KF5/KF5KDEGames/kgamerendereditem.h
/usr/include/KF5/KF5KDEGames/kgamerenderedobjectitem.h
/usr/include/KF5/KF5KDEGames/kgamerenderer.h
/usr/include/KF5/KF5KDEGames/kgamerendererclient.h
/usr/include/KF5/KF5KDEGames/kgaudioscene.h
/usr/include/KF5/KF5KDEGames/kgdeclarativeview.h
/usr/include/KF5/KF5KDEGames/kgdifficulty.h
/usr/include/KF5/KF5KDEGames/kgsound.h
/usr/include/KF5/KF5KDEGames/kgtheme.h
/usr/include/KF5/KF5KDEGames/kgthemeprovider.h
/usr/include/KF5/KF5KDEGames/kgthemeselector.h
/usr/include/KF5/KF5KDEGames/kstandardgameaction.h
/usr/include/KF5/KF5KDEGames/libkdegames_capabilities.h
/usr/include/KF5/KF5KDEGames/libkdegames_export.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kchatbase.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kchatbaseitemdelegate.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kchatbasemodel.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgame.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgamechat.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgameerror.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgameio.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgamemessage.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgamenetwork.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgameproperty.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgamepropertyhandler.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgamesequence.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kgameversion.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kmessageclient.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kmessageio.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kmessageserver.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgame/kplayer.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgamecanvas.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgamedifficulty.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgamesvgdocument.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgametheme.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/kgamethemeselector.h
/usr/include/KF5/KF5KDEGames/libkdegamesprivate/libkdegamesprivate_export.h
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesConfig.cmake
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesConfigVersion.cmake
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesTargets.cmake
/usr/lib64/libKF5KDEGames.so
/usr/lib64/libKF5KDEGamesPrivate.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KDEGames.so.7
/usr/lib64/libKF5KDEGames.so.7.3.0
/usr/lib64/libKF5KDEGamesPrivate.so.7
/usr/lib64/libKF5KDEGamesPrivate.so.7.3.0
/usr/lib64/qt5/qml/org/kde/games/core/KgItem.qml
/usr/lib64/qt5/qml/org/kde/games/core/libcorebindingsplugin.so
/usr/lib64/qt5/qml/org/kde/games/core/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886
/usr/share/package-licenses/libkdegames/221e6be04f1b020e012e7bd9e9e39b86fda17ba2
/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af
/usr/share/package-licenses/libkdegames/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkdegames/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9
/usr/share/package-licenses/libkdegames/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4
/usr/share/package-licenses/libkdegames/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0

%files locales -f libkdegames5.lang
%defattr(-,root,root,-)

