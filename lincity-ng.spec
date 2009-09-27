%define name 	lincity-ng
%define version 2.0
%define rel 3
%define	Summary	Lincity - A City Simulation Game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:	http://download.berlios.de/lincity-ng/%{name}-%{version}.tar.bz2
Patch0:		lincity-ng-1.1.2-fix-desktop.patch
Patch1:		lincity-ng-2.0-fix-str-fmt.patch
License:	GPLv2+
URL:		http://lincity-ng.berlios.de/
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	imagemagick
BuildRequires:	jam
BuildRequires:	zlib-devel libxml2-devel
BuildRequires:	X11-devel
BuildRequires:	SDL-devel SDL_mixer-devel SDL_image-devel SDL_ttf-devel libSDL_gfx-devel 
BuildRequires:	libphysfs-devel desktop-file-utils
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
rm -fr %{buildroot}
DESTDIR=%{buildroot} jam install
mkdir -p %{buildroot}%{_miconsdir}
convert -size 48x48 data/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
convert -size 32x32 data/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
convert -size 16x16 data/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

mkdir -p %buildroot%_datadir/applications
desktop-file-install --vendor="" --delete-original \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_gamesdatadir}/applications/*

mkdir -p %buildroot%_datadir/pixmaps
mv %buildroot%{_gamesdatadir}/pixmaps/* %buildroot%_datadir/pixmaps

rm -fr %buildroot%_gamesdatadir/doc

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING* README RELNOTES TODO
%{_gamesbindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
