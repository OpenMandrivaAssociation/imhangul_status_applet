%define version 0.3
%define release %mkrel 2

Summary:	GTK+ 2.x hangul input module status applet
Name:		imhangul_status_applet
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Internationalization
URL:		http://kldp.net/projects/imhangul/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		%{name}-%{version}.tar.bz2

BuildRequires:	gnome-panel-devel >= 2.0.0
Prereq:		GConf2 >= 2.3.3
Requires:	imhangul >= 0.9.4

%description
This applet shows status of imhangul, a GTK+ 2.x hangul input
module, under GNOME environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
for SCHEMA in imhangul_status; do
    gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$SCHEMA.schemas > /dev/null
done

%preun
if [ "$1" = "0" ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    for SCHEMA in imhangul_status; do
        gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/$SCHEMA.schemas > /dev/null
    done
fi

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/imhangul
%{_datadir}/pixmaps/*
%{_libexecdir}/imhangul-status-applet
%{_libdir}/bonobo/servers/*.server


