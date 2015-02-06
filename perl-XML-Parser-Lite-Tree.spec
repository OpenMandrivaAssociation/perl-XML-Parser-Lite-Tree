%define upstream_name    XML-Parser-Lite-Tree
%define	upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Lightweight XML tree builder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(SOAP::Lite)
BuildArch:	noarch

%description
This is a singleton class for parsing XML into a tree structure. How does this
differ from other XML tree generators? By using XML::Parser::Lite, which is a
pure perl XML parser. Using this module you can tree-ify simple XML without
having to compile any C.

Each node contains a "type" key, one of "root", "tag" and "data". "root" is the
document root, and only contains an array ref "children". "tag" represents a
normal tag, and contains an array ref "children", a hash ref "attributes" and a
string "name". "data" nodes contain only a "content" string.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
# duplicated from SOAP::Lite
rm -f %{buildroot}%{perl_vendorlib}/XML/Parser/Lite.pm

%files
%{perl_vendorlib}/XML
%{_mandir}/*/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 684844
- update to new version 0.14

* Sun Nov 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 597483
- rebuild

* Wed Sep 16 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 443472
- update to 0.12

* Mon Aug 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 420263
- update to 0.11

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 418381
- update to 0.10

* Thu Aug 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 410566
- update to 0.09

* Wed Aug 05 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 410068
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 292360
- update to new version 0.08

* Wed Sep 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdv2009.0
+ Revision: 279960
- drop file duplicated with perl-SOAP-Lite

* Mon Sep 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 278241
- update to new version 0.06

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.0
+ Revision: 272258
- new version

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.03-7mdv2009.0
+ Revision: 258877
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-6mdv2009.0
+ Revision: 246775
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2008.1
+ Revision: 166689
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-4mdv2008.0
+ Revision: 23509
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-3mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Sat Sep 10 2005 Pascal Terjan <pterjan@mandriva.org> 0.03-2mdk
- BuildRequires perl-SOAP-Lite (for make test)
- mkrel

* Sat Aug 20 2005 Pascal Terjan <pterjan@mandriva.org> 0.03-1mdk
- First version of the package

