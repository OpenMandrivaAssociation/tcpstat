%define name tcpstat
%define version 1.5
%define release 13

Summary: A network statistics reporter
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Monitoring
Url: http://www.frenchfries.net/paul/tcpstat/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-12mdv2010.0
+ Revision: 445383
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-11mdv2009.1
+ Revision: 298410
- rebuilt against libpcap-1.0.0

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-10mdv2009.0
+ Revision: 261435
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-9mdv2009.0
+ Revision: 254263
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-7mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5-7mdv2008.0
+ Revision: 68892
- rebuild

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5-5mdv2008.0
+ Revision: 68702
- rebuild


* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 19:40:33 (42219)
- rebuild

* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 19:28:59 (42218)
Import tcpstat

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.5-2mdk
- Enlarge your changelog, natural rebuild method, make all bots happy for free

* Tue Aug 12 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.5-1mdk 
- First mdk contrib

