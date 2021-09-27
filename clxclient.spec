Summary:	Kokkini Zita clxclient library
Summary(pl.UTF-8):	Biblioteka Kokkini Zita clxclient
Name:		clxclient
Version:	3.9.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	39af7de7888fb4d37362edbc94566314
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	clthreads-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clxclient library, used by Kokkini Zita Linux Audio projects.

%description -l pl.UTF-8
Biblioteka clxclient, używana w projektach Kokkini Zita Linux Audio.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXft-devel >= 2
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q
%patch0 -p1

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libclxclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclxclient.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclxclient.so
%{_includedir}/clxclient.h
