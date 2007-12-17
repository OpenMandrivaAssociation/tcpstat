%define name tcpstat
%define version 1.5
%define release %mkrel 7

Summary: A network statistics reporter
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Monitoring
Url: http://www.frenchfries.net/paul/tcpstat/index.html
BuildRequires: libpcap-devel

%description
Tcpstat reports certain network interface statistics much like 
vmstat does for system statistics. tcpstat gets its information by 
either monitoring a specific interface, or by reading previously 
saved tcpdump data from a file. 

Some of the statistics tcpstat calculates: 
- bandwidth 
- number of packets 
- packets per second 
- average packet size 
- standard deviation of packet size 
- interface load 
- more...

tcpstat is written with performance and efficiency in mind and is capable 
of handling large amounts of packets per second. Its compact command line 
interface is geared for the network researcher, system administrator and 
desktop shell user. tcpstat has been a valuable tool in university research 
papers and commercial networks alike.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL LICENSE NEWS README doc/Tips_and_Tricks.txt
%_bindir/tcp*
%_mandir/man1/tcp*
