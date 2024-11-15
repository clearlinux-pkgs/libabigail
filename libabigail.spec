#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: f35655a
#
Name     : libabigail
Version  : 2.6
Release  : 36
URL      : https://mirrors.kernel.org/sourceware/libabigail/libabigail-2.6.tar.xz
Source0  : https://mirrors.kernel.org/sourceware/libabigail/libabigail-2.6.tar.xz
Summary  : The ABI Generic Analysis and Instrumentation Library
Group    : Development/Tools
License  : Apache-2.0
Requires: libabigail-bin = %{version}-%{release}
Requires: libabigail-lib = %{version}-%{release}
Requires: libabigail-license = %{version}-%{release}
Requires: libabigail-man = %{version}-%{release}
BuildRequires : bash-completion
BuildRequires : bash-completion-dev
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : file
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxxhash)
BuildRequires : pypi-sphinx
BuildRequires : rpm-extras
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
%setup -q -n libabigail-2.6
cd %{_builddir}/libabigail-2.6
%patch -P 1 -p1
pushd ..
cp -a libabigail-2.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730768163
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-valgrind
make  %{?_smp_mflags}  ; make man

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-valgrind
make  %{?_smp_mflags}  ; make man
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1730768163
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libabigail
cp %{_builddir}/libabigail-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/libabigail/483d1c97dc79ef8741eae507897ca39cfe19da36 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/libabigail/default.abignore

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/abicompat
/V3/usr/bin/abidiff
/V3/usr/bin/abidw
/V3/usr/bin/abilint
/V3/usr/bin/abipkgdiff
/V3/usr/bin/kmidiff
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
/usr/include/libabigail/abg-elf-based-reader.h
/usr/include/libabigail/abg-elf-reader.h
/usr/include/libabigail/abg-fe-iface.h
/usr/include/libabigail/abg-fwd.h
/usr/include/libabigail/abg-hash.h
/usr/include/libabigail/abg-ini.h
/usr/include/libabigail/abg-interned-str.h
/usr/include/libabigail/abg-ir.h
/usr/include/libabigail/abg-libxml-utils.h
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
/V3/usr/lib64/libabigail.so.5.0.0
/usr/lib64/libabigail.so.5
/usr/lib64/libabigail.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libabigail/483d1c97dc79ef8741eae507897ca39cfe19da36

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/abicompat.1
/usr/share/man/man1/abidb.1
/usr/share/man/man1/abidiff.1
/usr/share/man/man1/abidw.1
/usr/share/man/man1/abilint.1
/usr/share/man/man1/abipkgdiff.1
/usr/share/man/man7/libabigail.7
