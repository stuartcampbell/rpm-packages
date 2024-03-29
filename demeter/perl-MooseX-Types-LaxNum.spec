Name:           perl-MooseX-Types-LaxNum
Version:        0.04
Release:        4%{?dist}
Summary:        LaxNum type which provides the loose behavior of Moose's Num pre-2.10
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MooseX-Types-LaxNum/
Source0:        http://www.cpan.org/authors/id/S/SW/SWEETKID/MooseX-Types-LaxNum-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  make 
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(Scalar::Util)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(MooseX::Types::LaxNum)

%description
LaxNum accepts everything for which "looks_like_number" in Scalar::Util
return true. It can be used to get the old behaviour of
Moose::Util::TypeConstraints::Num, since Num has been changed to be
more strict.

%prep
%setup -q -n MooseX-Types-LaxNum-%{version}

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
%doc dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 16 2022 Stuart Campbell <scampbell@bnl.gov> - 0.04-4
- Add make to build dependencies

* Thu Jun 16 2022 Stuart Campbell <scampbell@bnl.gov> - 0.04-3
- Added perl-generators to build dependencies

* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 0.04-2
- Added Provides info

* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 0.04-1
- Specfile autogenerated by cpanspec 1.78.
