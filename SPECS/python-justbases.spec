%global srcname justbases

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:       python-%{srcname}
Version:    0.14
Release:    4%{?dist}
Summary:    A small library for precise conversion between arbitrary bases

License:    LGPLv2+
URL:        http://pypi.python.org/pypi/justbases
Source0:    https://pypi.io/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

%description
A small library for precise conversion between arbitrary bases and native
Python numbers.

%if %{with python2}
%package -n python2-%{srcname}
Summary:    A small library for precise conversion between arbitrary bases
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires: python2-six

%description -n python2-%{srcname}
A small library for precise conversion between arbitrary bases and native
Python numbers.
%endif # with python2


%package -n python3-%{srcname}
Summary:    A small library for precise conversion between arbitrary bases
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires: python3-six

%description -n python3-%{srcname}
A small library for precise conversion between arbitrary bases and native
Python numbers.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf justbases.egg-info

%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/justbases/
%{python2_sitelib}/justbases-%{version}-*.egg-info
%endif # with python2

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/justbases/
%{python3_sitelib}/justbases-%{version}-*.egg-info

%changelog
* Tue May 26 2020  Dennis Keefe <dkeefe@redhat.com> - 0.14-4
- Update to 0.14
- Resolves: rhbz#1824230 

* Sun Jun 10 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.9-6
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-2
- Rebuild for Python 3.6

* Tue Aug 2 2016 mulhern <amulhern@redhat.com> - 0.9
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 16 2016 mulhern <amulhern@redhat.com> - 0.6
- Initial release
