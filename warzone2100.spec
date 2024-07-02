#global debug_package %{nil}
%define _empty_manifest_terminate_build 0
%define _disable_ld_no_undefined 1
%define _disable_lto 1

%global build_ldflags %{build_ldflags} -lz -pthread -lpthread
%define	Werror_cflags	%nil

Summary:	Postnuclear realtime strategy
Name:		warzone2100
Version:	4.5.0
Release:	1
Group:		Games/Strategy
License:	GPLv2+
URL:		http://wz2100.net/
# original source with game data stripped
Source0:	https://downloads.sourceforge.net/project/warzone2100/releases/%{version}/%{name}_src.tar.xz
Source1:	https://sourceforge.net/projects/warzone2100/files/warzone2100/Videos/standard-quality-en/sequences.wz

BuildRequires:	cmake
# Used to build man
BuildRequires:	asciidoc
BuildRequires:  asciidoctor
BuildRequires:	a2x
# Other BR
BuildRequires:  automake
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:  glslc
BuildRequires:	imagemagick
BuildRequires:	zip
BuildRequires:	%{_lib}intl
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	physfs-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
Requires:	%{name}-data = %{version}
Requires:	fonts-ttf-dejavu
Requires:	%{name}-videos

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
%doc %{_datadir}/doc/%{name}/*
%{_bindir}/warzone2100
%{_datadir}/icons/net.wz2100.warzone2100.png
%{_datadir}/applications/net.wz2100.warzone2100.desktop
%{_datadir}/metainfo/net.wz2100.warzone2100.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/warzone2100.mo
%{_mandir}/man6/%{name}.6*


#---------------------------------------------------------------------------

%package data
Summary:	Data files for Warzone 2100
Group:		Games/Strategy
Requires:	%{name} = %{version}
BuildArch:	noarch

%description data
Data files needed to play Warzone 2100.

%files data
%doc %{_datadir}/warzone2100/fonts/Noto.LICENSE.txt
%{_datadir}/warzone2100/base.wz
%{_datadir}/warzone2100/fonts/DejaVu*
%{_datadir}/warzone2100/fonts/NotoSansCJK-VF.otf.ttc
%{_datadir}/warzone2100/music/*
%{_datadir}/warzone2100/terrain_overrides/classic.wz
%{_datadir}/warzone2100/terrain_overrides/high.wz

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
%{_datadir}/warzone2100/mp.wz

#---------------------------------------------------------------------------

%prep
%setup -qn %{name}
%autopatch -p1

%build
%cmake \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release \
    	-DWZ_DISTRIBUTOR="OpenMandriva" \
        -DWZ_ENABLE_WARNINGS_AS_ERRORS=OFF

#	-DIntl_LIBRARY=""
       
%make_build

%install
cd build
%make_install

#find_lang %{name}

# remove not needed devel stuff
rm -rf  %{buildroot}%{_includedir}/fmt  %{buildroot}%{_libdir}/libfmt.a %{buildroot}%{_libdir}/cmake/fmt %{buildroot}/%{_libdir}/pkgconfig/fmt.pc
rmdir -v %{buildroot}%{_libdir}/cmake %{buildroot}/%{_libdir}/pkgconfig
