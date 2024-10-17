%define real_name Term-Query

Summary:	Term::Query - table-driven query routine
Name:		perl-%{real_name}
Version:	2.0
Release: 9
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Array::PrintCols)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Term::Query is a Perl 5 module, which performs generalized queries on
various kinds of values. Validation and normalization of input, based
on the type, is automated, as is error reporting and re-solicitation
of input.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work
# make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Term/*
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-7mdv2010.0
+ Revision: 430572
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-6mdv2009.0
+ Revision: 241962
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0-4mdv2008.0
+ Revision: 25457
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 2.0-3mdv2008.0
+ Revision: 23831
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0-1mdk
- initial Mandriva package

