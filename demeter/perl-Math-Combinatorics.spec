Name:           perl-Math-Combinatorics
Version:        0.09
Release:        3%{?dist}
Summary:        Perform combinations and permutations on lists
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Combinatorics/
Source0:        http://www.cpan.org/authors/id/A/AL/ALLENDAY/Math-Combinatorics-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More::UTF8)
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Math::Combinatorics)

%description
Combinatorics is the branch of mathematics studying the enumeration,
combination, and permutation of sets of elements and the
mathematical relations that characterize their properties. As a
jumping off point, refer to:

%prep
%setup -q -n Math-Combinatorics-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 16 2022 Stuart Campbell (scampbell@bnl.gov) 0.09-3
- Added perl-generators and perl-interpreter

* Sun May 02 2021 Stuart Campbell (scampbell@bnl.gov) 0.09-2
- Added Provides

* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 0.09-1
- Specfile autogenerated by cpanspec 1.78.
