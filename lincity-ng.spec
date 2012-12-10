Summary:	Lincity - A City Simulation Game
Name:		lincity-ng
Version:	2.0
Release:	%mkrel 6
Source0:	http://freefr.dl.sourceforge.net/project/lincity-ng.berlios/lincity-ng-%version.tar.bz2
Patch0:		lincity-ng-1.1.2-fix-desktop.patch
Patch1:		lincity-ng-2.0-fix-str-fmt.patch
License:	GPLv2+
URL:		http://lincity-ng.berlios.de/
Group:		Games/Other
BuildRequires:	imagemagick
BuildRequires:	jam
BuildRequires:	mesa-common-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libphysfs-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
Obsoletes:	lincity
Provides:	lincity

%description
Lincity is a city simulation game. Build your city up from a primitive village
to an advanced civilization.  Build a sustainable economy, or build rockets to
escape from a pollution ridden and resource starved planet. 

LinCity-NG is a polished and improved version of the classic LinCity game with
a new iso-3D graphics engine, with a completely redone and modern GUI.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--with-gzip \
		--with-svga \
		--with-x \
		--disable-rpath
jam %_smp_mflags

%install
DESTDIR=%{buildroot} jam install
mkdir -p %{buildroot}%{_miconsdir}
convert -size 48x48 data/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
convert -size 32x32 data/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
convert -size 16x16 data/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %buildroot%_datadir/applications
mv %{buildroot}%{_gamesdatadir}/applications/* %{buildroot}%{_datadir}/applications

mkdir -p %buildroot%_datadir/pixmaps
mv %buildroot%{_gamesdatadir}/pixmaps/* %buildroot%_datadir/pixmaps

rm -fr %buildroot%_gamesdatadir/doc

%files
%doc COPYING* README RELNOTES TODO
%{_gamesbindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


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

