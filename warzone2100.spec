%define	name	warzone2100
%define	version	2.0.5
%define	release	2
%define	Summary	Postnuclear realtime strategy

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Games/Strategy
# original source with game data stripped
Source0:	http://download.gna.org/warzone/releases/2.0/%{name}-%{version}.tar.bz2
Url:		http://wz2100.net/
Summary:	%{Summary}
License:	GPL
BuildRequires:	SDL-devel SDL_net-devel oggvorbis-devel openal-devel flex
BuildRequires:	mesa-common-devel mad-devel ImageMagick physfs-devel bison
BuildRequires:	jpeg-devel png-devel desktop-file-utils automake1.8
Obsoletes:	warzone2100-opengl warzone2100-software
Provides:	warzone2100-opengl warzone2100-software
Requires:	%{name}-data = %{version}
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
%setup -q

%build

./autogen.sh

perl -pi -e "s#-m32##g" ./makerules/common.mk
perl -pi -e "s#-m32##g" configure
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-make-data

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon="%{name}.png" \
		needs="x11" \
		section="More Applications/Games/Strategy" \
		title="Warzone 2100" \
		longtitle="%{Summary}" \
		xdg="true"
EOF


mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/games/applications/*.desktop %{buildroot}%{_datadir}/applications/


#install -m644 debian/warzone2100.desktop -D %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--remove-key="TryExec" \
			--add-category="X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -resize 16x16 debian/warzone2100.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 debian/warzone2100.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 debian/warzone2100.png %{buildroot}%{_liconsdir}/%{name}.png
rm -rf %{buildroot}%{_datadir}/games/icons/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_menudir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}


