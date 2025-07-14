Summary:	A collection of widgets for VMware (but not only)
Summary(pl.UTF-8):	Zestaw widgetów dla VMware (ale nie tylko)
Name:		libview
Version:	0.6.6
Release:	4
License:	MIT
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/view/%{name}-%{version}.tar.bz2
# Source0-md5:	12b0a1e03013ae315d5f9088261d4f2b
Patch0:		%{name}-constructor.patch
Patch1:		%{name}-pc.patch
URL:		http://view.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.4.0
Requires:	gtkmm >= 2.4.0
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
Requires:	gtk+2-devel >= 2:2.4.0
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
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export CFLAGS="%{rpmcflags} -std=c++11"
export CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

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
%{_includedir}/libview
%{_pkgconfigdir}/libview.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libview.a
