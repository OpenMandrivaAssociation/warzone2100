%define	Werror_cflags	%nil
%define	name	warzone2100
%define	version	2.1.1
%define	release	1
%define	Summary	Postnuclear realtime strategy

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Games/Strategy
# original source with game data stripped
Source0:	http://download.gna.org/warzone/releases/2.1/%{name}-%{version}.tar.bz2
Patch0:		warzone2100-scriptfuncs.patch
URL:		http://wz2100.net/
Summary:	%{Summary}
License:	GPLv2+
BuildRequires:	SDL-devel SDL_net-devel oggvorbis-devel openal-devel flex
BuildRequires:	mesa-common-devel mad-devel imagemagick physfs-devel bison
BuildRequires:	jpeg-devel png-devel desktop-file-utils zip
BuildRequires:	quesoglc-devel popt-devel gettext-devel
Requires:	%{name}-data
Requires:	fonts-ttf-dejavu
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep
%setup -q -n %{name}-%{version}
%patch0 
%build
#perl -pi -e "s#-m32##g" ./makerules/common.mk
#perl -pi -e "s#-m32##g" configure
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-data \
		--with-distributor="Mandriva"
                  
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/games/applications/*.desktop %{buildroot}%{_datadir}/applications/

#remove unwanted extension
sed -i s/"warzone2100.png"/"warzone2100"/"" %{buildroot}%{_datadir}/applications/warzone2100.desktop

desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--remove-key="TryExec" \
			--add-category="Game;StrategyGame" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -resize 16x16 icons/warzone2100.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 icons/warzone2100.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 icons/warzone2100.png %{buildroot}%{_liconsdir}/%{name}.png
rm -rf %{buildroot}%{_datadir}/games/icons/%{name}.png

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/*.wz
%{_gamesdatadir}/%{name}/mods/global/*.wz
%{_gamesdatadir}/%{name}/mods/global/autoload/music/music/menu.ogg
%{_gamesdatadir}/%{name}/mods/global/autoload/music/music/music.wpl
%{_gamesdatadir}/%{name}/mods/global/autoload/music/music/track1.ogg
%{_gamesdatadir}/%{name}/mods/global/autoload/music/music/track2.ogg
%{_gamesdatadir}/%{name}/mods/multiplay/ntw.wz


