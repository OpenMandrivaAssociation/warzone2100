%define	Werror_cflags	%nil
%define	name	warzone2100
%define	version	2.3.9
#version of the videos in warzone2100-videos-low. May not match current game version (e.g. videos 2.2 for game 2.3.5).
%define videoversion 2.2
%define	release	1
%define	Summary	Postnuclear realtime strategy

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Games/Strategy
# original source with game data stripped
Source0:	http://downloads.sourceforge.net/project/warzone2100/releases/%{version}/warzone2100-%{version}.tar.gz
URL:		http://wz2100.net/
Summary:	%{Summary}
License:	GPLv2+
BuildRequires:	SDL-devel SDL_net-devel oggvorbis-devel openal-devel flex
BuildRequires:	mesa-common-devel mad-devel imagemagick physfs-devel bison
BuildRequires:	jpeg-devel png-devel desktop-file-utils zip
BuildRequires:	quesoglc-devel popt-devel gettext-devel
BuildRequires:	libtheora-devel
Requires:	%{name}-data = %{version}
Requires:	fonts-ttf-dejavu
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	%{name}-videos = %{videoversion}

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
mv %{buildroot}%{_gamesdatadir}/applications/*.desktop %{buildroot}%{_datadir}/applications/

desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--remove-key="TryExec" \
			--add-category="Game;StrategyGame" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -resize 16x16 icons/warzone2100.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 icons/warzone2100.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 icons/warzone2100.png %{buildroot}%{_liconsdir}/%{name}.png
rm -rf %{buildroot}%{_gamesdatadir}/icons/%{name}.png

#remove data that already are in the data package => lighter package
rm -rf %{buildroot}%{_gamesdatadir}

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


%changelog
* Mon Oct 24 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.9-1mdv2011.0
+ Revision: 705903
- Upgrade to 2.3.9

* Tue May 17 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.8-1
+ Revision: 675901
- Upgrade to 2.3.8

* Wed Jan 26 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.7-1
+ Revision: 632780
- Upgrade to 2.3.7

* Sat Dec 04 2010 Zombie Ryushu <ryushu@mandriva.org> 2.3.6-1mdv2011.0
+ Revision: 609497
- Upgrade to 2.3.6
- Upgrade to 2.3.6

* Sun Sep 26 2010 Samuel Verschelde <stormi@mandriva.org> 2.3.5-1mdv2011.0
+ Revision: 581120
- update to 2.3.5
- fix video package version number (was 2.3 should be 2.2)

* Fri Aug 20 2010 Zombie Ryushu <ryushu@mandriva.org> 2.3.4-1mdv2011.0
+ Revision: 571484
- Upgrade to 2.3.4
- Upgrade to 2.3.4

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 2.3.3-1mdv2011.0
+ Revision: 565905
- new version 2.3.3

  + Zombie Ryushu <ryushu@mandriva.org>
    - Upgrade to 2.3.1a
    - Upgrade to 2.3.1a

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2010.1
+ Revision: 538568
- New version 2.3.0

* Sat Nov 07 2009 Samuel Verschelde <stormi@mandriva.org> 2.2.4-1mdv2010.1
+ Revision: 462495
- Suggests warzone-videos
- buildrequires libtheora-devel
- new version 2.2.4
- removed unneeded data from the resulting RPM (they are already in the warzone2100-data package).
- removed an apparently no more needed patch
- require warzone2100-data in same version (previous require didn't specify the version)
- removed no more needed sed on desktop file

* Sun Oct 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.2-3mdv2010.0
+ Revision: 453719
- rebuild for new libopenal

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 2.1.2-1mdv2009.1
+ Revision: 352992
- New version 2.1.2

* Wed Feb 11 2009 Zombie Ryushu <ryushu@mandriva.org> 2.1.1-1mdv2009.1
+ Revision: 339315
- Upgrade to 2.1.1 and include the music
- Stable release 2.1.0
- Preliminary 2.1.0 Stable Build

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 2.1-0.beta4.3mdv2009.0
+ Revision: 275777
- fix file list
- split data again to save bandwith
- fix source URL

* Sun Aug 24 2008 Emmanuel Andry <eandry@mandriva.org> 2.1-0.beta4.2mdv2009.0
+ Revision: 275518
- fix requires

* Sun Aug 24 2008 Emmanuel Andry <eandry@mandriva.org> 2.1-0.beta4.1mdv2009.0
+ Revision: 275495
- New version
- fix license
- Also package warzone2100 data, not useful to have it in a different package

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.0.10-1mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Feb 03 2008 Emmanuel Andry <eandry@mandriva.org> 2.0.10-1mdv2008.1
+ Revision: 161733
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.9-1mdv2008.1
+ Revision: 120385
- New version
- fix desktop file validation

* Sun Jul 08 2007 Funda Wang <fwang@mandriva.org> 2.0.7-1mdv2008.0
+ Revision: 49732
- Remove duplicated files
- fix spec file on icon dir
- New version

* Sun May 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.6-1mdv2008.0
+ Revision: 28841
- update to latest version
- buildrequires on zip
- correct configure options
- drop old menu style
- own missing files


* Mon Jan 15 2007 Olivier Blin <oblin@mandriva.com> 2.0.5-2mdv2007.0
+ Revision: 109210
- update url

* Sun Jan 14 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.5-1mdv2007.1
+ Revision: 108425
- New version 2.0.5

* Sat Dec 02 2006 Olivier Blin <oblin@mandriva.com> 2.0.4-5mdv2007.1
+ Revision: 90018
- buildrequire desktop-file-utils
- buildrequires png-devel
- buildrequires jpeg-devel
- remove TryExec from XDG menu (so that it appears in KDE)
- Import warzone2100

* Wed Sep 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.4-4mdv2007.0
- fix buildrequires

* Wed Sep 13 2006 Emmanuel Andry <eandry@mandriva.org> 2.0.4-3mdv2007.0
- add Game;StrategyGame in xdg category

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.4-2mdv2007.0
- add missing buildrequires

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.4-1mdv2007.0
- 2.0.4
- fix buildrequires
- merge packages
- update url

* Sat Aug 26 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-6mdv2007.0
- xdg menu

* Thu Sep 15 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-5mdk
- rebuild to fix path to menudir on x86_64

* Fri Sep 09 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-4mdk
- enable 64 bit build (not considered safe)
- make %%build --short-circuitable

* Sat Sep 03 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-3mdk
- split out data in own package to be able to provide smaller releases
- build software accelerated binary too

* Fri Sep 02 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-2mdk
- fix summary

* Thu Sep 01 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-1mdk
- initial release

