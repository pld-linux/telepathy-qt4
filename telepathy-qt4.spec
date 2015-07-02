#
# Conditional build:
%bcond_without	qt4	# Qt4 interface
%bcond_without	qt5	# Qt5 interface

# "telepathy_qt" name is occupied by earlier work under the same name from different project;
# thus spec and repo stick to original "telepathy-qt4" name of this project (used before 0.9.0 release)
%define		orgname	telepathy-qt
%define		qt4_ver		4.8.2
%define		qt5_ver		5.0.0

Summary:	Library for Qt4-based Telepathy clients
Summary(pl.UTF-8):	Biblioteka dla klientów Telepathy opartych na Qt4
Name:		telepathy-qt4
Version:	0.9.6.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-qt/%{orgname}-%{version}.tar.gz
# Source0-md5:	bebebfbe29d194a9ba00b4f422a44f74
Patch0:		telepathy-qt-warnings.patch
URL:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	farstream-devel >= 0.2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-pygobject
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	telepathy-farstream-devel >= 0.6.0
BuildRequires:	telepathy-glib-devel >= 0.18.0
%if %{with qt4}
BuildRequires:	QtCore-devel >= %{qt4_ver}
BuildRequires:	QtDBus-devel >= %{qt4_ver}
BuildRequires:	QtGui-devel >= %{qt4_ver}
BuildRequires:	QtHelp >= %{qt4_ver}
BuildRequires:	QtNetwork-devel >= %{qt4_ver}
BuildRequires:	QtTest-devel >= %{qt4_ver}
BuildRequires:	QtXml-devel >= %{qt4_ver}
BuildRequires:	qt4-build >= %{qt4_ver}
BuildRequires:	qt4-qmake >= %{qt4_ver}
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5DBus-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
BuildRequires:	Qt5Network-devel >= %{qt5_ver}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	Qt5Xml-devel >= %{qt5_ver}
BuildRequires:	qt5-assistant >= %{qt5_ver}
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-qmake >= %{qt5_ver}
%endif
Requires:	QtCore >= %{qt4_ver}
Requires:	QtDBus >= %{qt4_ver}
Requires:	QtNetwork >= %{qt4_ver}
Requires:	QtXml >= %{qt4_ver}
Requires:	telepathy-farstream >= 0.6.0
Requires:	telepathy-glib >= 0.18.0
Obsoletes:	telepathy-qt4-yell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Qt4-based Telepathy clients.

%description -l pl.UTF-8
Biblioteka dla klientów Telepathy opartych na Qt4.

%package devel
Summary:	Header files for telepathy-qt4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-qt4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qt4_ver}
Requires:	QtDBus-devel >= %{qt4_ver}
Requires:	QtNetwork-devel >= %{qt4_ver}
Requires:	QtXml-devel >= %{qt4_ver}
Obsoletes:	telepathy-qt4-yell-devel

%description devel
Header files for telepathy-qt4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-qt4.

%package apidocs
Summary:	API documentation for telepathy-qt4 and telepathy-qt5 libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek telepathy-qt5 i telepathy-qt5
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for telepathy-qt4 and telepathy-qt5 libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek telepathy-qt5 i telepathy-qt5.

%package -n telepathy-qt5
Summary:	Library for Qt5-based Telepathy clients
Summary(pl.UTF-8):	Biblioteka dla klientów Telepathy opartych na Qt5
Group:		Libraries
Requires:	Qt5Core >= %{qt5_ver}
Requires:	Qt5DBus >= %{qt5_ver}
Requires:	Qt5Network >= %{qt5_ver}
Requires:	Qt5Xml >= %{qt5_ver}
Requires:	telepathy-farstream >= 0.6.0
Requires:	telepathy-glib >= 0.18.0

%description -n telepathy-qt5
Library for Qt5-based Telepathy clients.

%description -n telepathy-qt5 -l pl.UTF-8
Biblioteka dla klientów Telepathy opartych na Qt5.

%package -n telepathy-qt5-devel
Summary:	Header files for telepathy-qt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki telepathy-qt5
Group:		Development/Libraries
Requires:	Qt5Core-devel >= %{qt5_ver}
Requires:	Qt5DBus-devel >= %{qt5_ver}
Requires:	telepathy-qt5 = %{version}-%{release}

%description -n telepathy-qt5-devel
Header files for telepathy-qt5 library.

%description -n telepathy-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-qt5.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake .. \
	-DENABLE_FARSTREAM:BOOL=ON \
	-DDESIRED_QT_VERSION=4 \
	-DQT_QMAKE_EXECUTABLE_FINDQT=%{_libdir}/qt4/bin/qmake

%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DENABLE_FARSTREAM:BOOL=ON \
	-DDESIRED_QT_VERSION=5 \
	-DQT_QMAKE_EXECUTABLE_FINDQT=%{_libdir}/qt5/bin/qmake

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
        DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
        DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n telepathy-qt5 -p /sbin/ldconfig
%postun	-n telepathy-qt5 -p /sbin/ldconfig

%if %{with qt4}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4.so.2
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4-farstream.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farstream.so
%{_libdir}/libtelepathy-qt4-service.a
%{_libdir}/cmake/TelepathyQt4
%{_libdir}/cmake/TelepathyQt4Farstream
%{_libdir}/cmake/TelepathyQt4Service
%{_includedir}/telepathy-qt4
%{_pkgconfigdir}/TelepathyQt4.pc
%{_pkgconfigdir}/TelepathyQt4Farstream.pc
%{_pkgconfigdir}/TelepathyQt4Service.pc
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*

%if %{with qt5}
%files -n telepathy-qt5
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt5.so.0
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt5-farstream.so.0

%files -n telepathy-qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-qt5.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt5-farstream.so
%{_libdir}/libtelepathy-qt5-service.a
%{_libdir}/cmake/TelepathyQt5
%{_libdir}/cmake/TelepathyQt5Farstream
%{_libdir}/cmake/TelepathyQt5Service
%{_includedir}/telepathy-qt5
%{_pkgconfigdir}/TelepathyQt5.pc
%{_pkgconfigdir}/TelepathyQt5Farstream.pc
%{_pkgconfigdir}/TelepathyQt5Service.pc
%endif
