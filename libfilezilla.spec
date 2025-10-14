# FIXME
# libfilezilla need now c++17, so force clang to use it but for some reason this workaround wont work...
# so disable it for now, until we find a better solution
#global optflags %{optflags} -std=gnu++17

%define major		46
%define libname		%mklibname filezilla
%define develname	%mklibname filezilla -d

Name:		libfilezilla
Version:	0.51.1
Release:	1
Summary:	Small and modern C++ library
License:	GPLv2+
Group:		System/Libraries
URL:		https://lib.filezilla-project.org/
Source0:	https://download.filezilla-project.org/libfilezilla/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:	doxygen
BuildRequires:  gettext
BuildRequires:	graphviz
BuildRequires:  pkgconfig(nettle)
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(gnutls)

# needed for testsuite
BuildRequires:	locales-en
BuildRequires:	pkgconfig(cppunit)

%description
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their accuracy,
  which simplifies dealing with timestamps originating from different sources.
* Simple process handling for spawning child processes with redirected I/O.

#------------------------------------------------

%package -n	%{libname}
Summary:	Small and modern C++ library
Group:		System/Libraries
Obsoletes: %{libname} < %{EVRD}
Obsoletes: %{libname}32
Obsoletes: %{libname}35

%description -n	%{libname}
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their accuracy,
  which simplifies dealing with timestamps originating from different sources.
* Simple process handling for spawning child processes with redirected I/O.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------
%prep
%setup -q

%build

%configure
%make_build

pushd doc
make html
popd

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.%{major}*
%{_datadir}/locale/*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%doc doc/doxygen-doc/*
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

