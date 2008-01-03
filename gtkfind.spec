%define name gtkfind
%define release %mkrel 8
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


mkdir -p %buildroot%_menudir
cat > %buildroot%_menudir/%{name} <<EOF
?package(%{name}):\
command="%_bindir/%name"\
title="Gtkfind"\
longtitle="Graphical file finding program"\
needs="x11"\
icon="file_tools_section.png"\
section="System/File Tools"
EOF
 
%post
%{update_menus}
 
%postun
%{clean_menus}  

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL
%_bindir/%name
%{_mandir}/man1/*
%{_menudir}/*

