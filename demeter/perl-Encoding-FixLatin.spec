Name:           perl-Encoding-FixLatin
Version:        1.04
Release:        4%{?dist}
Summary:        Takes mixed encoding input and produces UTF-8 output
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Encoding-FixLatin/
Source0:        http://www.cpan.org/authors/id/G/GR/GRANTM/Encoding-FixLatin-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.90
#Requires:       perl(Encoding::FixLatin::XS) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Encoding::FixLatin)

%description
Most encoding conversion tools take input in one encoding and produce
output in another encoding. This module takes input which may contain
characters in more than one encoding and makes a best effort to convert
them all to UTF-8 output.

%prep
%setup -q -n Encoding-FixLatin-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes dist.ini LICENSE META.json README
%{_bindir}/fix_latin
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Jun 16 2022 Stuart Campbell (scampbell@bnl.gov) 1.04-4
- Added perl-generators to build dependencies

* Tue Jun  7 2022 Stuart Campbell (scampbell@bnl.gov) 1.04-3
- Added make to Build Dependencies

* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 1.04-2
- Added Provides info

* Sun Apr 11 2021 Stuart Campbell (scampbell@bnl.gov) 1.04-1
- Specfile autogenerated by cpanspec 1.78.
