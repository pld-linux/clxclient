Summary:	Kokkini Zita clxclient library
Name:		clxclient
Version:	3.9.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	bd6df73f688c9be1b3afef58283d7ef5
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/
BuildRequires:	clthreads-devel
BuildRequires:	freetype-devel
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clxclient library, used by Kokkini Zita Linux Audio projects.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
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
%{__make} \
	LIBDIR="%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LIBDIR="%{_lib}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
