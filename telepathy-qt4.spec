
%define		orgname	telepathy-qt
%define		qt_ver		4.8.2

Summary:	Telepathy Qt4
Summary(pl.UTF-8):	Telepathy Qt4
Name:		telepathy-qt4
Version:	0.9.3
Release:	2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://telepathy.freedesktop.org/releases/telepathy-qt/%{orgname}-%{version}.tar.gz
# Source0-md5:	94ac93aedf5f6fff49837bc8368e5a37
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
BuildRequires:	telepathy-glib-devel >= 0.19.5
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
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
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
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-qt4.so.?

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libtelepathy-qt4.so
%{_libdir}/cmake/TelepathyQt4
%{_includedir}/telepathy-qt4
%{_pkgconfigdir}/TelepathyQt4.pc
