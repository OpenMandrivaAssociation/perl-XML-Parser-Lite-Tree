%define pkgname XML-Parser-Lite-Tree
%define name	perl-%{pkgname}
%define	version	0.03
%define	release	%mkrel 6

Name:		%{name}
Summary:	Lightweight XML tree builder
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{pkgname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{pkgname}/
BuildRequires:	perl-devel 
BuildRequires:  perl(SOAP::Lite)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl

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
%setup -q -n %{pkgname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/XML/Parser/Lite/Tree.pm
%{_mandir}/*/*

