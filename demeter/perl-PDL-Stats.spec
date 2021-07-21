Name:           perl-PDL-Stats
Version:        0.76
Release:        2%{?dist}
Summary:        Collection of statistics modules in Perl Data Language, with a quick-start guide for non-PDL people
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PDL-Stats/
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/PDL-Stats-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PDL::Core)
BuildRequires:  perl(PDL::Slatec)
BuildRequires:  perl(Test::More)
Requires:       perl(PDL::Core)
Requires:       perl(PDL::Slatec)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(PDL::Stats)
Provides:       perl(PDL::Stats::Basic)
Provides:       perl(PDL::Stats::GLM)
Provides:       perl(PDL::Stats::Kmeans)
Provides:       perl(PDL::Stats::TS)


%description
Loads modules named below, making the functions available in the current
namespace.

%prep
%setup -q -n PDL-Stats-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README.md
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 0.76-2
- Added Provides for sub modules 

* Sun Apr 11 2021 Stuart Campbell (scampbell@bnl.gov) 0.76-1
- Specfile autogenerated by cpanspec 1.78.