
%define		qt_ver		4.8.2

Summary:	Telepathy Qt4
Summary(pl.UTF-8):	Telepathy Qt4
Name:		telepathy-qt4
Version:	0.8.0
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://telepathy.freedesktop.org/releases/telepathy-qt4/%{name}-%{version}.tar.gz
# Source0-md5:	b93f03f063d784855d83e1b3c79a1cc5
Patch0:		%{name}-build.patch
URL:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	cmake
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

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
        ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
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
%{_includedir}/telepathy-1.0
%{_pkgconfigdir}/TelepathyQt4.pc
%{_pkgconfigdir}/TelepathyQt4Farsight.pc
