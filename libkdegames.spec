#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkdegames
Version  : 19.12.1
Release  : 15
URL      : https://download.kde.org/stable/release-service/19.12.1/src/libkdegames-19.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.1/src/libkdegames-19.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.1/src/libkdegames-19.12.1.tar.xz.sig
Summary  : Common code and data for many KDE games
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1 MIT
Requires: libkdegames-data = %{version}-%{release}
Requires: libkdegames-lib = %{version}-%{release}
Requires: libkdegames-license = %{version}-%{release}
Requires: libkdegames-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kdnssd-dev
BuildRequires : kglobalaccel-dev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-extras
BuildRequires : openal-soft-dev
BuildRequires : qtbase-dev mesa-dev

%description
some thoughts and comments about the lib - usually for KGame hackers
- setMin/MaxPlayers() etc. use KGameProperty::changeValue() which is slightly
unclean but as these functions can only called by the ADMIN it doesn't matter.
- AB: KGamePropertyList && KGamePropertyArray:
for PolicyClean||PolicyDirty the values are streamed into a QDataStream as usual
for PolicyDirty||PolicyLocal the values are streamed as well but
additionally command() is called immediately. The values are read from
the stream there. This is some kind of performance loss as it would be
faster *not* to stream it but imediately call e.g. insert(). But it will
probably save a *lot* of bugs!

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
%setup -q -n libkdegames-19.12.1
cd %{_builddir}/libkdegames-19.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578683820
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1578683820
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdegames
cp %{_builddir}/libkdegames-19.12.1/COPYING %{buildroot}/usr/share/package-licenses/libkdegames/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libkdegames-19.12.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/libkdegames/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/libkdegames-19.12.1/carddecks/svg-konqi-modern/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9
cp %{_builddir}/libkdegames-19.12.1/carddecks/svg-standard/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4
cp %{_builddir}/libkdegames-19.12.1/carddecks/svg-tigullio-international/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886
cp %{_builddir}/libkdegames-19.12.1/carddecks/svg-xskat-french/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af
cp %{_builddir}/libkdegames-19.12.1/carddecks/svg-xskat-german/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0
cp %{_builddir}/libkdegames-19.12.1/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkdegames/ff3ed70db4739b3c6747c7f624fe2bad70802987
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
/usr/include/KF5/KF5KDEGames/KDE/KExtHighscore
/usr/include/KF5/KF5KDEGames/KDE/KGameClock
/usr/include/KF5/KF5KDEGames/KDE/KGamePopupItem
/usr/include/KF5/KF5KDEGames/KDE/KGameRenderedItem
/usr/include/KF5/KF5KDEGames/KDE/KGameRenderedObjectItem
/usr/include/KF5/KF5KDEGames/KDE/KGameRenderer
/usr/include/KF5/KF5KDEGames/KDE/KGameRendererClient
/usr/include/KF5/KF5KDEGames/KDE/KHighscore
/usr/include/KF5/KF5KDEGames/KDE/KScoreDialog
/usr/include/KF5/KF5KDEGames/KDE/KStandardGameAction
/usr/include/KF5/KF5KDEGames/KDE/KgAudioScene
/usr/include/KF5/KF5KDEGames/KDE/KgDeclarativeView
/usr/include/KF5/KF5KDEGames/KDE/KgDifficulty
/usr/include/KF5/KF5KDEGames/KDE/KgSound
/usr/include/KF5/KF5KDEGames/KDE/KgTheme
/usr/include/KF5/KF5KDEGames/KDE/KgThemeProvider
/usr/include/KF5/KF5KDEGames/KDE/KgThemeSelector
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
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesLibraryDepends-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KDEGames/KF5KDEGamesLibraryDepends.cmake
/usr/lib64/libKF5KDEGames.so
/usr/lib64/libKF5KDEGamesPrivate.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KDEGames.so.7
/usr/lib64/libKF5KDEGames.so.7.2.0
/usr/lib64/libKF5KDEGamesPrivate.so.1
/usr/lib64/libKF5KDEGamesPrivate.so.1.0.0
/usr/lib64/qt5/qml/org/kde/games/core/KgItem.qml
/usr/lib64/qt5/qml/org/kde/games/core/libcorebindingsplugin.so
/usr/lib64/qt5/qml/org/kde/games/core/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886
/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af
/usr/share/package-licenses/libkdegames/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9
/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4
/usr/share/package-licenses/libkdegames/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0
/usr/share/package-licenses/libkdegames/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f libkdegames5.lang
%defattr(-,root,root,-)

