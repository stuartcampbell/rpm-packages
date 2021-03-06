# RHEL doesn't have python 3 and does not know about __python2
%if 0%{?rhel}  
  %global __python2 %{__python}
  %global python2_sitelib %{python_sitelib}
  %global with_python3 0
%else
  %global with_python3 1
%endif

Name:           python-sphinx-theme-bootstrap
Version:        0.4.5
Release:        3%{?dist}
Summary:        A sphinx theme that integrates the Bootstrap framework

License:        MIT
URL:            http://ryan-roemer.github.com/sphinx-bootstrap-theme/
Source0:        https://pypi.python.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:  python2-devel
%if %{with_python3}
BuildRequires:  python3-devel
%endif

Requires:       python-sphinx

%description
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options, 
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of difference Bootswatch CSS themes.

%if %{with_python3}
%package -n python3-sphinx-theme-bootstrap
Summary:        A sphinx theme that integrates the Bootstrap framework
Requires:       python3-sphinx

%description -n python3-sphinx-theme-bootstrap
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options, 
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of difference Bootswatch CSS themes.
%endif

%prep
%setup -q -n sphinx-bootstrap-theme-%{version}

%build
%{__python2} setup.py build

%if %{with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# Remove bundled JQuery
rm -rf %{buildroot}%{python2_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js
rm -rf %{buildroot}%{python2_sitelib}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-3.2.0/js
rm -rf %{buildroot}%{python2_sitelib}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-2.3.2/js

%if %{with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Remove bundled JQuery
rm -rf %{buildroot}%{python3_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js
rm -rf %{buildroot}%{python3_sitelib}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-3.2.0/js
rm -rf %{buildroot}%{python3_sitelib}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-2.3.2/js
%endif

%files
%doc LICENSE.txt README.txt README.rst
%{python2_sitelib}/sphinx_bootstrap_theme/*
%{python2_sitelib}/sphinx_bootstrap_theme-%{version}-py2.7.egg-info/*

%if %{with_python3}
%files -n python3-sphinx-theme-bootstrap
%doc LICENSE.txt README.txt README.rst
%{python3_sitelib}/sphinx_bootstrap_theme/*
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py3.4.egg-info/*
%endif


%changelog
* Fri Mar 11 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-4
- Removed bundled JQuery

* Fri Oct 2 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-3
- Changed to check for all RHELs

* Mon Sep 28 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-2
- Added python3 support 

* Tue Jan 13 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-1
- Initial package
