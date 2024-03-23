#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkdegames
Version  : 24.02.1
Release  : 66
URL      : https://download.kde.org/stable/release-service/24.02.1/src/libkdegames-24.02.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.1/src/libkdegames-24.02.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.1/src/libkdegames-24.02.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 ISC LGPL-2.0 LGPL-2.1 MIT
Requires: libkdegames-data = %{version}-%{release}
Requires: libkdegames-lib = %{version}-%{release}
Requires: libkdegames-license = %{version}-%{release}
Requires: libkdegames-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kdnssd-dev
BuildRequires : ki18n-dev
BuildRequires : libsndfile-dev
BuildRequires : openal-soft-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n libkdegames-24.02.1
cd %{_builddir}/libkdegames-24.02.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711152414
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711152414
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdegames
cp %{_builddir}/libkdegames-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkdegames/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/libkdegames/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkdegames/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkdegames/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/ICS.txt %{buildroot}/usr/share/package-licenses/libkdegames/221e6be04f1b020e012e7bd9e9e39b86fda17ba2 || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/libkdegames-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/libkdegames-%{version}/src/carddecks/svg-konqi-modern/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9 || :
cp %{_builddir}/libkdegames-%{version}/src/carddecks/svg-standard/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4 || :
cp %{_builddir}/libkdegames-%{version}/src/carddecks/svg-tigullio-international/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886 || :
cp %{_builddir}/libkdegames-%{version}/src/carddecks/svg-xskat-french/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af || :
cp %{_builddir}/libkdegames-%{version}/src/carddecks/svg-xskat-german/COPYRIGHT %{buildroot}/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkdegames6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/qlogging-categories6/libkdegames.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KDEGames6/KGameAudioScene
/usr/include/KDEGames6/KGameClock
/usr/include/KDEGames6/KGameDifficulty
/usr/include/KDEGames6/KGameDifficultyLevel
/usr/include/KDEGames6/KGameGraphicsViewRenderer
/usr/include/KDEGames6/KGameHighScoreDialog
/usr/include/KDEGames6/KGameHighscore
/usr/include/KDEGames6/KGamePopupItem
/usr/include/KDEGames6/KGameRenderedGraphicsObject
/usr/include/KDEGames6/KGameRenderedItem
/usr/include/KDEGames6/KGameRenderer
/usr/include/KDEGames6/KGameRendererClient
/usr/include/KDEGames6/KGameSound
/usr/include/KDEGames6/KGameStandardAction
/usr/include/KDEGames6/KGameTheme
/usr/include/KDEGames6/KGameThemeProvider
/usr/include/KDEGames6/KGameThemeSelector
/usr/include/KDEGames6/kdegames_export.h
/usr/include/KDEGames6/kdegames_version.h
/usr/include/KDEGames6/kgameaudioscene.h
/usr/include/KDEGames6/kgameclock.h
/usr/include/KDEGames6/kgamedifficulty.h
/usr/include/KDEGames6/kgamegraphicsviewrenderer.h
/usr/include/KDEGames6/kgamehighscore.h
/usr/include/KDEGames6/kgamehighscoredialog.h
/usr/include/KDEGames6/kgamepopupitem.h
/usr/include/KDEGames6/kgamerenderedgraphicsobject.h
/usr/include/KDEGames6/kgamerendereditem.h
/usr/include/KDEGames6/kgamerenderer.h
/usr/include/KDEGames6/kgamerendererclient.h
/usr/include/KDEGames6/kgamesound.h
/usr/include/KDEGames6/kgamestandardaction.h
/usr/include/KDEGames6/kgametheme.h
/usr/include/KDEGames6/kgamethemeprovider.h
/usr/include/KDEGames6/kgamethemeselector.h
/usr/include/KDEGames6/libkdegames_capabilities.h
/usr/include/KDEGames6/libkdegamesprivate/kchatbase.h
/usr/include/KDEGames6/libkdegamesprivate/kchatbaseitemdelegate.h
/usr/include/KDEGames6/libkdegamesprivate/kchatbasemodel.h
/usr/include/KDEGames6/libkdegamesprivate/kdegamesprivate_export.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgame.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgamechat.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgameerror.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgameio.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgamemessage.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgamenetwork.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgameproperty.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgamepropertyhandler.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgamesequence.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kgameversion.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kmessageclient.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kmessageio.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kmessageserver.h
/usr/include/KDEGames6/libkdegamesprivate/kgame/kplayer.h
/usr/include/KDEGames6/libkdegamesprivate/kgamesvgdocument.h
/usr/lib64/cmake/KDEGames6/KDEGames6Config.cmake
/usr/lib64/cmake/KDEGames6/KDEGames6ConfigVersion.cmake
/usr/lib64/cmake/KDEGames6/KDEGames6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KDEGames6/KDEGames6Targets.cmake
/usr/lib64/libKDEGames6.so
/usr/lib64/libKDEGames6Private.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKDEGames6.so.6.0.240201
/V3/usr/lib64/libKDEGames6Private.so.6.0.240201
/V3/usr/lib64/qt6/qml/org/kde/games/core/libcorebindingsplugin.so
/usr/lib64/libKDEGames6.so.6
/usr/lib64/libKDEGames6.so.6.0.240201
/usr/lib64/libKDEGames6Private.so.6
/usr/lib64/libKDEGames6Private.so.6.0.240201
/usr/lib64/qt6/qml/org/kde/games/core/KGameItem.qml
/usr/lib64/qt6/qml/org/kde/games/core/corebindingsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/games/core/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/games/core/libcorebindingsplugin.so
/usr/lib64/qt6/qml/org/kde/games/core/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdegames/0525f48093a421a78d3524e598e8fee0cb5d4886
/usr/share/package-licenses/libkdegames/221e6be04f1b020e012e7bd9e9e39b86fda17ba2
/usr/share/package-licenses/libkdegames/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libkdegames/33f6ef5ae6fc21b42ca7d9d1aeb7390aca7366af
/usr/share/package-licenses/libkdegames/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkdegames/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/libkdegames/5573560dd763dfa71382a7b14fc7016fe877f9b9
/usr/share/package-licenses/libkdegames/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/libkdegames/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkdegames/8d92c816e421da0e573f208ff54beab223dc2de4
/usr/share/package-licenses/libkdegames/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkdegames/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/libkdegames/f2324384bebcce4eaf3d153583f0eb2caf6960a0

%files locales -f libkdegames6.lang
%defattr(-,root,root,-)

