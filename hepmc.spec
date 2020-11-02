### RPM external hepmc 2.06.10
Source: http://hepmc.web.cern.ch/hepmc/releases/hepmc%realversion.tgz

Requires: autotools

%define keep_archives true
%define drop_files %i/share

%prep
%setup -q -n HepMC-%{realversion}

F77="$(which gfortran) -fPIC"
CXX="$(which g++) -fPIC"
PLATF_CONFIG_OPTS="--enable-static --disable-shared"

perl -p -i -e 's|glibtoolize|libtoolize|g' ./bootstrap

export HEPMC_NODOC=1

./bootstrap
./configure $PLATF_CONFIG_OPTS --prefix=%{i} --with-momentum=GEV --with-length=MM F77="$F77" CXX="$CXX"

%build
make %makeprocesses

%install
make install
rm -rf %i/lib/*.la
