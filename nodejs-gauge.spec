%{?scl:%scl_package nodejs-gauge}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-gauge

%global npm_name gauge
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-gauge
Version:    2.6.0
Release:    1%{?dist}
Summary:	A terminal based horizontal guage
Url:		https://github.com/iarna/gauge
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
A terminal based horizontal guage

%prep
%setup -q -n package

%nodejs_fixdep has-unicode

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
#%%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/gauge

%doc README.md LICENSE

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.6.0-1
- Updated with script

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.7-1
- Updated with script
- removed requires

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.2-6
- Removed wrong dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.2-5
- Use %%nodejs_fixdep macro

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.2-4
- rebuilt

* Wed Dec 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.2-3
- Initial build
