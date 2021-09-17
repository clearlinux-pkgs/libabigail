#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libabigail
Version  : 1.8.2
Release  : 18
URL      : https://mirrors.kernel.org/sourceware/libabigail/libabigail-1.8.2.tar.gz
Source0  : https://mirrors.kernel.org/sourceware/libabigail/libabigail-1.8.2.tar.gz
Summary  : The ABI Generic Analysis and Instrumentation Library
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: libabigail-bin = %{version}-%{release}
Requires: libabigail-lib = %{version}-%{release}
Requires: libabigail-license = %{version}-%{release}
Requires: libabigail-man = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : bash-completion
BuildRequires : bash-completion-dev
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libzip)
BuildRequires : rpm-extras
BuildRequires : valgrind
Patch1: 0001-Add-a-hidden-option-to-abidw-to-make-it-exit-if-it-s.patch

%description
This is the Application Binary Interface Generic Analysis and
Instrumentation Library.

%package bin
Summary: bin components for the libabigail package.
Group: Binaries
Requires: libabigail-license = %{version}-%{release}

%description bin
bin components for the libabigail package.


%package dev
Summary: dev components for the libabigail package.
Group: Development
Requires: libabigail-lib = %{version}-%{release}
Requires: libabigail-bin = %{version}-%{release}
Provides: libabigail-devel = %{version}-%{release}
Requires: libabigail = %{version}-%{release}

%description dev
dev components for the libabigail package.


%package lib
Summary: lib components for the libabigail package.
Group: Libraries
Requires: libabigail-license = %{version}-%{release}

%description lib
lib components for the libabigail package.


%package license
Summary: license components for the libabigail package.
Group: Default

%description license
license components for the libabigail package.


%package man
Summary: man components for the libabigail package.
Group: Default

%description man
man components for the libabigail package.


%prep
%setup -q -n libabigail-1.8.2
cd %{_builddir}/libabigail-1.8.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631842395
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}  ; make man

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1631842395
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libabigail
cp %{_builddir}/libabigail-1.8.2/COPYING %{buildroot}/usr/share/package-licenses/libabigail/f81facfd488e95a394b99c4b8ac4add46b19999d
cp %{_builddir}/libabigail-1.8.2/COPYING-GPLV3 %{buildroot}/usr/share/package-licenses/libabigail/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/libabigail-1.8.2/COPYING-LGPLV2 %{buildroot}/usr/share/package-licenses/libabigail/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/libabigail-1.8.2/COPYING-LGPLV3 %{buildroot}/usr/share/package-licenses/libabigail/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install
## install_append content
make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/libabigail/default.abignore

%files bin
%defattr(-,root,root,-)
/usr/bin/abicompat
/usr/bin/abidiff
/usr/bin/abidw
/usr/bin/abilint
/usr/bin/abipkgdiff
/usr/bin/kmidiff

%files dev
%defattr(-,root,root,-)
/usr/include/libabigail/abg-comp-filter.h
/usr/include/libabigail/abg-comparison.h
/usr/include/libabigail/abg-config.h
/usr/include/libabigail/abg-corpus.h
/usr/include/libabigail/abg-cxx-compat.h
/usr/include/libabigail/abg-diff-utils.h
/usr/include/libabigail/abg-dwarf-reader.h
/usr/include/libabigail/abg-fwd.h
/usr/include/libabigail/abg-hash.h
/usr/include/libabigail/abg-ini.h
/usr/include/libabigail/abg-interned-str.h
/usr/include/libabigail/abg-ir.h
/usr/include/libabigail/abg-libxml-utils.h
/usr/include/libabigail/abg-libzip-utils.h
/usr/include/libabigail/abg-reader.h
/usr/include/libabigail/abg-regex.h
/usr/include/libabigail/abg-reporter.h
/usr/include/libabigail/abg-sptr-utils.h
/usr/include/libabigail/abg-suppression.h
/usr/include/libabigail/abg-tools-utils.h
/usr/include/libabigail/abg-traverse.h
/usr/include/libabigail/abg-version.h
/usr/include/libabigail/abg-viz-common.h
/usr/include/libabigail/abg-viz-dot.h
/usr/include/libabigail/abg-viz-svg.h
/usr/include/libabigail/abg-workers.h
/usr/include/libabigail/abg-writer.h
/usr/lib64/libabigail.so
/usr/lib64/pkgconfig/libabigail.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libabigail.so.0
/usr/lib64/libabigail.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libabigail/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libabigail/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/libabigail/f45ee1c765646813b442ca58de72e20a64a7ddba
/usr/share/package-licenses/libabigail/f81facfd488e95a394b99c4b8ac4add46b19999d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/abicompat.1
/usr/share/man/man1/abidiff.1
/usr/share/man/man1/abidw.1
/usr/share/man/man1/abilint.1
/usr/share/man/man1/abipkgdiff.1
/usr/share/man/man7/libabigail.7
