Summary:	A graphical file finding program
Name:		gtkfind
Version:	1.1
Release:	14
License:	GPLv2+
Group:		File tools
Source0:	%{name}-%{version}.tar.bz2
Url:		https://www.oz.net/~mattg/download.html
BuildRequires:	man
BuildRequires:	xterm
BuildRequires:	pkgconfig(gtk+)

%description
gtkfind is a graphical file finding program, written by Matt Grossman
<mattg@oz.net> and distributed under the terms of the GNU GPL. It
requires X and the freely distributable (GPL) gtk toolkit to run.

%files
%doc README COPYING INSTALL
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 gtkfind %{buildroot}%{_bindir}
install -m 444 gtkfind.1 %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Name=Gtkfind
Comment=Graphical file finding program
Icon=file_tools_section
Categories=X-MandrivaLinux-System-FileTools;System;
EOF

