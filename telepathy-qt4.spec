
%define		orgname	telepathy-qt
%define		qt_ver		4.8.2

Summary:	Library for Qt4-based Telepathy clients
Summary(pl.UTF-8):	Biblioteka dla klientów Telepathy opartych na Qt4
Name:		telepathy-qt4
Version:	0.9.3
Release:	4
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://telepathy.freedesktop.org/releases/telepathy-qt/%{orgname}-%{version}.tar.gz
# Source0-md5:	94ac93aedf5f6fff49837bc8368e5a37
Patch0:		%{name}-build.patch
URL:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	farstream-devel >= 0.1.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-pygobject
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	telepathy-farstream-devel >= 0.2.2
BuildRequires:	telepathy-glib-devel >= 0.19.5
Requires:	QtCore >= %{qt_ver}
Requires:	QtDBus >= %{qt_ver}
Requires:	QtNetwork >= %{qt_ver}
Requires:	QtXml >= %{qt_ver}
Requires:	telepathy-farstream >= 0.2.2
Requires:	telepathy-glib >= 0.19.5
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
Requires:	QtCore-devel >= %{qt_ver}
Requires:	QtDBus-devel >= %{qt_ver}
Obsoletes:	telepathy-qt4-yell-devel

%description devel
Header files for telepathy-qt4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki telepathy-qt4

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DENABLE_FARSTREAM:BOOL=ON \
	-DENABLE_FARSIGHT:BOOL=OFF \
	-DQT_QMAKE_EXECUTABLE_FINDQT=%{_libdir}/qt4/bin/qmake \
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
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4.so.2
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4-farstream.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so
%attr(755,root,root) %{_libdir}/libtelepathy-qt4-farstream.so
%{_libdir}/cmake/TelepathyQt4
%{_libdir}/cmake/TelepathyQt4Farstream
%{_includedir}/telepathy-qt4
%{_pkgconfigdir}/TelepathyQt4.pc
%{_pkgconfigdir}/TelepathyQt4Farstream.pc
