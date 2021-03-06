Name:           perl-PGPLOT
Version:        2.27
Release:        1%{?dist}
Summary:        Allow subroutines in the PGPLOT graphics library to be called from Perl
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PGPLOT/
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/PGPLOT-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gcc
BuildRequires:	perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::F77)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:	pgplot-devel
Requires:	pgplot
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an inteface to the PGPLOT graphics library. To obtain
the library and its manual, see "OBTAINING PGPLOT".

%prep
%setup -q -n PGPLOT-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES HELP HINTS.irix HINTS.osf INSTALL-MacOSX INSTALL-Win32 LICENSE META.json pgcompatbility.p README test.img
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PGPLOT*
%{_mandir}/man3/*

%changelog
* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 2.27-1
- Specfile autogenerated by cpanspec 1.78.
