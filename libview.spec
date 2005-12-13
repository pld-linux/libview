Summary:	A collection of widgets for VMware (but not only)
Summary(pl):	Zestaw widgetów dla VMware (ale nie tylko)
Name:		libview
Version:	0.5.5
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/view/%{name}-%{version}.tar.bz2
# Source0-md5:	3125e73865e7a76ffe1024cafe6d6573
Patch0:		%{name}-constructor.patch
URL:		http://view.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libview is a collection of widgets that were developed for use VMware
relased at MIT license so that open source community can use it.

%description -l pl
libview to zestaw widgetów stworzonych do u¿ytku z VMware ale
udostêpnionych na otwartej licencji (MIT), aby spo³eczno¶æ opensource
mog³a z nich skorzystaæ.

%package devel
Summary:	Header files for libview library
Summary(pl):	Pliki nag³ówkowe biblioteki libview
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.4.0

%description devel
Header files for libview library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libview.

%package static
Summary:	Static libview library
Summary(pl):	Statyczna biblioteka libview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libview library.

%description static -l pl
Statyczna biblioteka libview.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libview
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
