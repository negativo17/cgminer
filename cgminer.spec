Name:           cgminer
Version:        4.10.0
Release:        1%{?dist}
Summary:        Mmulti-threaded multi-pool FPGA and ASIC miner for Bitcoin

License:        GPLv3
URL:            http://ck.kolivas.org/apps/%{name}/
Source0:        http://ck.kolivas.org/apps/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libcurl) >= 7.25.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(jansson) >= 2.6
BuildRequires:  zlib-devel
#Requires:       

%description
Cgminer should automatically find all of your Avalon ASIC, BFL ASIC, BitForce
FPGAs, Icarus bitstream FPGAs, Klondike ASIC, ASICMINER usb block erupters, KnC
ASICs, BaB ASICs, Hashfast ASICs, ModMiner FPGAs, BPMC/BGMC BF1 USB ASICs,
Bi*fury USB ASICs, Onestring miner USB ASICs, Hexfury USB ASICs, Nanofury USB
ASICs, Antminer U1/U2/U2+ U3 USB ASICs, Cointerra devices, BFx2 USB ASICs,
Rockminer R-Box/RK-Box/T1 USB ASICs, Avalon2/3/4 USB ASICs and Hashratio USB
ASICs.

%prep
%autosetup
# Do not look in bin for modminer data files
sed -i -e 's|$(bindir)/bitstreams|$(sysconfdir)/%{name}|g' Makefile.*
sed -i -e 's|path, "bitstreams"|path, "%{_sysconfdir}/%{name}"|g' fpgautils.c

%build
export CPPFLAGS="%{optflags}"
%configure \
    --disable-ants1 \
    --disable-ants2 \
    --disable-ants3 \
    --enable-avalon \
    --enable-avalon2 \
    --enable-avalon4 \
    --enable-avalon7 \
    --enable-avalon-miner \
    --enable-bab \
    --enable-bflsc \
    --enable-bitforce \
    --enable-bitfury \
    --enable-blockerupter \
    --enable-cointerra \
    --enable-drillbit \
    --enable-forcecombo \
    --enable-hashfast \
    --enable-hashratio \
    --enable-icarus \
    --enable-klondike \
    --enable-knc \
    --enable-minion \
    --enable-modminer \
    --enable-sp10 \
    --enable-sp30 \
    --enable-libsystemd \
    --with-system-jansson

%make_build


%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}


%files
%license COPYING
%doc API-README ASIC-README FPGA-README NEWS README
%{_bindir}/%{name}
%{_sysconfdir}/%{name}

%changelog
* Tue May 30 2017 Simone Caronni <negativo17@gmail.com> - 4.10.0-1
- First build.
