
%define		qt_ver		4.6.0

Summary:	Telepathy Qt4
Summary(pl.UTF-8):	Telepathy Qt4
Name:		telepathy-qt4
Version:	0.2.1
Release:	2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://telepathy.freedesktop.org/releases/telepathy-qt4/%{name}-%{version}.tar.gz
# Source0-md5:	9eaaa055eb2503e5a362bd183f344ac7
URL:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	pkgconfig
BuildRequires:	python-dbus
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-pygobject
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	telepathy-farsight-devel
BuildRequires:	telepathy-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy-Qt4 is a high-level binding for Telepathy.

%package devel
Summary:	Header files for telepathy-qt4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-qt4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for telepathy-qt4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-qt4

%package static
Summary:	Static telepathy-qt4 library
Summary(pl.UTF-8):	Statyczna biblioteka telepathy-qt4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static telepathy-qt4 library.

%description static -l pl.UTF-8
Statyczna biblioteka telepathy-qt4.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4.so.?
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farsight.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4-farsight.so.?

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farsight.so
%{_libdir}/libtelepathy-qt4.la
%{_libdir}/libtelepathy-qt4-farsight.la
%{_includedir}/telepathy-1.0
%{_pkgconfigdir}/TelepathyQt4.pc
%{_pkgconfigdir}/TelepathyQt4Farsight.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.a
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farsight.a
