%define upstream_name    XML-Parser-Lite-Tree
%define	upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Lightweight XML tree builder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(SOAP::Lite)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
# duplicated from SOAP::Lite
rm -f %{buildroot}%{perl_vendorlib}/XML/Parser/Lite.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/XML
%{_mandir}/*/*
