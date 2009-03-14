Summary:	A collection of widgets for VMware (but not only)
Summary(pl.UTF-8):	Zestaw widgetów dla VMware (ale nie tylko)
Name:		libview
Version:	0.6.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/view/%{name}-%{version}.tar.gz
# Source0-md5:	e917f9c33e83e55e20d52fe251278c84
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

%description -l pl.UTF-8
libview to zestaw widgetów stworzonych do użytku z VMware ale
udostępnionych na otwartej licencji (MIT), aby społeczność opensource
mogła z nich skorzystać.

%package devel
Summary:	Header files for libview library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.4.0

%description devel
Header files for libview library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libview.

%package static
Summary:	Static libview library
Summary(pl.UTF-8):	Statyczna biblioteka libview
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libview library.

%description static -l pl.UTF-8
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
%attr(755,root,root) %{_libdir}/libview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libview.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libview.so
%{_libdir}/libview.la
%{_includedir}/libview
%{_pkgconfigdir}/libview.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libview.a
