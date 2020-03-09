### RPM external form 4.1.033e
Source: https://gosam.hepforge.org/gosam-installer/form-%{realversion}.tar.gz
BuildRequires: gmake
Requires: zlib

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%prep
%setup -q -n form-4.1

%build

CXX="$(which %{cms_cxx}) -fPIC"
CC="$(which gcc) -fPIC"

./configure --prefix=%i \
            --bindir=%i/bin \
            --without-gmp \
            --with-zlib=${ZLIB_ROOT} \
            CXX="$CXX" CC="$CC" CXXFLAGS=-fpermissive

make %makeprocesses

%install
make install
