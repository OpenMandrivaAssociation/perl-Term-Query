%define real_name Term-Query

Summary:	Term::Query - table-driven query routine
Name:		perl-%{real_name}
Version:	2.0
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
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

