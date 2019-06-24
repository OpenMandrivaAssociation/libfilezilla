%define major		0
%define libname		%mklibname filezilla %{major}
%define develname	%mklibname filezilla -d

Name:		libfilezilla
Version:	0.17.1
Release:	1
Summary:	Small and modern C++ library
License:	GPLv2+
Group:		System/Libraries
URL:		https://lib.filezilla-project.org/
Source0:	http://download.filezilla-project.org/libfilezilla/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:  pkgconfig(nettle)
BuildRequires:  gmp-devel

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
%ifarch %ix86
export CC=gcc
export CXX=g++
%endif

%configure
%make_build

pushd doc
make html
popd

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%check
LC_ALL=en_US.UTF-8 \
make check

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%doc doc/doxygen-doc/*
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

