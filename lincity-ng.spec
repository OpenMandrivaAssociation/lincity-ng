%define name 	lincity-ng
%define version 1.1.0
%define release 1
%define	Summary	Lincity - A City Simulation Game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://download.berlios.de/lincity-ng/%{name}-%{version}.tar.bz2
License:	GPL
URL:		http://lincity-ng.berlios.de/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	jam
BuildRequires:	zlib-devel libxml2-devel
BuildRequires:	XFree86-devel
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

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-gzip \
		--with-svga \
		--with-x \
		--disable-rpath
jam

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

# menu
mkdir -p %{buildroot}%{_menudir}
cat << EOF >> %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" icon="%{name}.png" \
               needs="X11" section="More Applications/Games/Strategy" title="Lincity" \
               longtitle="%{Summary}" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="StrategyGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Strategy" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING* README RELNOTES TODO
%{_gamesbindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


