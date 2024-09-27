Summary:	Lincity - A City Simulation Game
Name:		lincity-ng
License:	GPLv2+
URL:		https://lincity-ng.berlios.de/
Group:		Games/Strategy
Version:	2.11.2
Release:	1
Source0:	https://github.com/lincity-ng/lincity-ng/releases/download/lincity-ng-%{version}/lincity-ng-%{version}-Source.tar.gz
# Fix build: CPack readme resource file: "README.md" could not be found.
#Patch0:       https://github.com/lincity-ng/lincity-ng/pull/160.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(SDL2_gfx)
BuildRequires:	pkgconfig(physfs)
BuildRequires:	pkgconfig(zlib)
# for compress .wav files
BuildRequires:	vorbis-tools
BuildRequires:       xsltproc

Obsoletes:	lincity
Provides:	lincity

%description
Lincity is a city simulation game. Build your city up from a primitive village
to an advanced civilization.  Build a sustainable economy, or build rockets to
escape from a pollution ridden and resource starved planet. 

LinCity-NG is a polished and improved version of the classic LinCity game with
a new iso-3D graphics engine, with a completely redone and modern GUI.

%prep
%autosetup -p1 -n %{name}-%{version}-Source

sed -i 's|-unknown)|-%{release})|' CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_BINDIR=%{_bindir} \
       -DCMAKE_INSTALL_APPDATADIR=%{_datadir}/%{name} \
       -DCMAKE_INSTALL_MANDIR=%{_mandir}/man6 \
       -DFULL_PROJECT_VERSION=%{version}-%{release} \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON
%make_build

%install
%make_install -C build

# Use font from system, instead bundled by game
ln -fs %{_datadir}/fonts/TTF/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/fonts/sans.ttf

%files
%doc CHANGELOG.md README.md doc/*.xml
%license COPYING*
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man6/lincity-ng.6.*

%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 2.0-5mdv2011.0
+ Revision: 636064
- correct desktop file
- tighten BR

* Fri Dec 03 2010 Tomas Kindl <supp@mandriva.org> 2.0-4mdv2011.0
+ Revision: 606561
- rebuild

  + Thomas Backlund <tmb@mandriva.org>
    - fix missing space in Comment

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 2.0-3mdv2010.0
+ Revision: 449971
- rebuild for new SDL_gfx

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 2.0-2mdv2010.0
+ Revision: 375063
- Change package group to Games/Other (fixes #49516)

* Tue Jan 27 2009 Funda Wang <fwang@mandriva.org> 2.0-1mdv2009.1
+ Revision: 334015
- fix str fmt
- New version 2.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2008.1
+ Revision: 106275
- fix desktop file
- New version 1.1.2

* Mon Aug 20 2007 Funda Wang <fwang@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 67195
- remove old doc files
- move common files into common dir rather games dir
- New version 1.1.1


* Thu Feb 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1mdv2007.0
+ Revision: 124728
- new version

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 1.0.3-5mdv2007.1
+ Revision: 100703
- Import lincity-ng

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 1.0.3-5
- Rebuild

* Wed Sep 13 2006 Emmanuel Andry <eandry@mandriva.org> 1.0.3-4mdv2007.0
- Game category repeated twice in desktop file (bug #25177)
- buildrequires desktop-file-utils

* Mon Aug 14 2006 Emmanuel Andry <eandry@mandriva.org> 1.0.3-3mdv2007.0
- rebuild

* Tue Aug 01 2006 Emmanuel Andry <eandry@mandriva.org> 1.0.3-2mdv2007.0
- xdg menu
- fix buildrequires

* Thu May 04 2006 Emmanuel Andry <eandry@free.fr> 1.0.3-1mdk
- New release 1.0.3

* Mon Jan 16 2006 Michael Scherer <misc@mandriva.org> 1.0.2-1mdk
- New release 1.0.2, thanks to Emmanuel Andry <eandry@free.fr> for testing
  and reporting

* Fri Aug 12 2005 Austin Acton <austin@mandriva.org> 1.0.1-1mdk
- move to lincity-ng, obsolete lincity
- source URL
- new URL
- convert icon on-the-fly

* Tue Aug 09 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.12.1-2mdk
- fix %%{Summary} macro
- build with svga and gzip support
- %%mkrel
- convert icons to png
- move data to %%{_gamesdatadir}
- no .bz2 ending for man page
- clean out suckage!

* Fri Mar 11 2005 Austin Acton <austin@mandrake.org> 1.12.1-1mdk
- configure 2.5
- from Emmanuel Andry <eandry@free.fr> :
  - New release
  - Updated buildrequires
  - Updated menu
  - New source for icons (taken from 1.12-0.pre55)

