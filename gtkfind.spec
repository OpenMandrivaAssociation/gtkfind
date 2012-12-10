%define name gtkfind
%define release %mkrel 12
%define version 1.1

Summary  : A graphical file finding program
Name     : %{name}
Version  : %{version}
Release  : %{release}
License: GPL
Group    : File tools
Source0  : %{name}-%{version}.tar.bz2
URL      : http://www.oz.net/~mattg/download.html
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildrequires: xterm libgtk+-devel man

%description
gtkfind is a graphical file finding program, written by Matt Grossman
<mattg@oz.net> and distributed under the terms of the GNU GPL.  It
requires X and the freely distributable (GPL) gtk toolkit to run.  gtk
is available from www.gtk.org and other places.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure

%make

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
install -s -m 755 gtkfind %buildroot%_bindir
install -m 444 gtkfind.1 %buildroot%_mandir/man1


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%_bindir/%name
Name=Gtkfind
Comment=Graphical file finding program
Icon=file_tools_section
Categories=X-MandrivaLinux-System-FileTools;System;
EOF
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}  
%endif

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL
%_bindir/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-*.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-12mdv2011.0
+ Revision: 619287
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-11mdv2010.0
+ Revision: 429336
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1-10mdv2009.0
+ Revision: 246686
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2008.1
+ Revision: 141938
- auto-convert XDG menu entry
- BR man
- kill re-definition of %%buildroot on Pixel's request
- import gtkfind

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Apr 08 2005 Olivier Thauvin <nanardon@mandrake.org> 1.1-8mdk
- fix menu path

* Wed Apr 26 2004 Lenny Cartier <lenny@mandrakesoft.com 1.1-7mdk
- rebuild

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com 1.1-6mdk
- buildrequires

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com 1.1-5mdk
- rebuild

* Fri Jun 14 2002 Lenny Cartier <lenny@mandrakesoft.com 1.1-4mdk
- buildrequires

* Wed Jan 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1-3mdk
- icon

* Wed Jul 25 2001  Lenny Cartier <lenny@mandrakesoft.com> 1.1-2mdk
- rebuild

* Mon Sep 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1-1mdk
- BM
- macros 
- menu

* Thu Apr 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9-2mdk
- fix group
- fix files section

* Wed Dec 22 1999 Lenny Cartier <lenny@mandrakesoft.com>
- fix location of files
- bz2 archive

