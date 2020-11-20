%global debug_package %{nil}
%define _disable_ld_no_undefined 1
%define _disable_lto 1

%global build_ldflags %{build_ldflags} -lz -pthread -lpthread
%define	Werror_cflags	%nil

Summary:	Postnuclear realtime strategy
Name:		warzone2100
Version:	3.4.1
Release:	1
Group:		Games/Strategy
License:	GPLv2+
URL:		http://wz2100.net/
# original source with game data stripped
Source0:	http://downloads.sourceforge.net/project/warzone2100/releases/%{version}/%{name}_src.tar.xz
Source1:	http://sourceforge.net/projects/warzone2100/files/warzone2100/Videos/standard-quality-en/sequences.wz

BuildRequires:	cmake
# Used to build man
BuildRequires:	asciidoc
BuildRequires:	a2x
# Other BR
BuildRequires:  automake
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	zip
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	physfs-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	qmake5
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew) >= 2.1.0
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(quesoglc)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(zlib)
Requires:	%{name}-data = %{version}
Requires:	fonts-ttf-dejavu
Suggests:	%{name}-videos

%description
Upon entering the game you land from your transport and establish your base.
Here you conduct research, design and manufacture vehicles, build new
structures and prepare your plans of global conquest. If the game goes badly
you'll end up fighting last ditch battles here to defend your base from
enemy attacks.

Combat is frenetic, with extensive graphical effects and damage to the
terrain and buildings giving rise to flying shrapnel and boulders. Within
the game are many different structures and vehicles. From an initial Command
Centre, you then go on to build Resource Extractors to provide fuel for Power
Generators, which in turn supply energy to Factories, Research Facilities and
weapons emplacements to protect your base.

Features:
 * 400+ Technologies to research 
 * 2,000+ different units to design 
 * 3 Large campaign maps to conquer 
 * 24 Fast play mission maps for extra action 
 * Intelligence Display sets objectives dynamically 
 * Interactive message system 
 * Fast Play Interface graphically Based 
 * Quick Screen Navigation 
 * Fast Find System for units & structures 
 * Set Factories to constant production 
 * Automatically send each factory's units to where you want them 

The Warzone 2100 ReDev Project aims to continue the vision of Pumpkin studios
started in 1999 with the game Warzone 2100, Which was closed source until
Dec 6, 2004 when it was let out the doors for the first time under a
GPL license.

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}/*
%{_datadir}/applications/%{name}.desktop
#{_datadir}/games/metainfo/warzone2100.appdata.xml
%{_mandir}/man6/%{name}.6*
#{_miconsdir}/%{name}.png
#{_iconsdir}/%{name}.png
#{_liconsdir}/%{name}.png
#attr(755,root,root) #{_gamesbindir}/%{name}

#---------------------------------------------------------------------------

%package data
Summary:	Data files for Warzone 2100
Group:		Games/Strategy
Requires:	%{name} = %{version}
BuildArch:	noarch

%description data
Data files needed to play Warzone 2100.

%files data
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}
%exclude %{_gamesdatadir}/%{name}/sequences.wz

#---------------------------------------------------------------------------

%package videos
Summary:	Optional video files for Warzone 2100
Group:		Games/Strategy
Requires:	%{name} = %{version}
BuildArch:	noarch

%description videos
Optional video files for Warzone 2100.

%files videos
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/sequences.wz

#---------------------------------------------------------------------------

%prep
%setup -qn %{name}
%autopatch -p1

%build
#export CC=gcc
#export CXX=g++
%cmake \
    	-DWZ_DISTRIBUTOR="OpenMandriva"
%make_build

%install
cd build
%make_install

#mkdir -p %{buildroot}%{_datadir}/applications
#mv %{buildroot}%{_gamesdatadir}/applications/*.desktop %{buildroot}%{_datadir}/applications/

#desktop-file-install	--vendor="" \
#			--remove-category="Application" \
#			--remove-key="TryExec" \
#			--add-category="Game;StrategyGame;" \
#			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
#convert -resize 16x16 icons/warzone2100.png %{buildroot}%{_miconsdir}/%{name}.png
#convert -resize 32x32 icons/warzone2100.png %{buildroot}%{_iconsdir}/%{name}.png
#convert -resize 48x48 icons/warzone2100.png %{buildroot}%{_liconsdir}/%{name}.png
#
#install -m 0644 %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{name}/
#
#rm -f %{buildroot}%{_gamesdatadir}/icons/warzone2100.png

#find_lang %{name}

