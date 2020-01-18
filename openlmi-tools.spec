Name:           openlmi-tools
Version:        0.9
Release:        4%{?dist}
Summary:        Set of CLI tools for Openlmi providers

License:        GPLv2+
URL:            http://fedorahosted.org/openlmi
Source0:        http://fedorahosted.org/released/openlmi-tools/%{name}-%{version}.tar.gz
Patch0:         openlmi-tools-01-fix-instance-deletion.patch
Patch1:         openlmi-tools-02-fix-passing-instances-to-method-call.patch
Patch2:         openlmi-tools-03-fix-instance-comparision.patch
BuildArch:      noarch

BuildRequires:  automake
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pywbem
BuildRequires:  pyOpenSSL
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx-theme-openlmi
Requires:       pywbem
Requires:       openlmi-python-base
Requires:       pyOpenSSL

Provides:       cura-tools = %{version}-%{release}
Obsoletes:      cura-tools < 0.1-4

%description
%{name} is a set of command line tools for Openlmi providers.

%package doc
Summary:        Documentation for %{name}

%description doc
%{summary}

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
pushd cli
%{__python} setup.py build
popd # cli

pushd doc
make html man
popd # doc

%install
pushd cli
%{__python} setup.py install --skip-build -O1 --root %{buildroot}
popd # cli
install -m 755 -d %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 README %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 COPYING %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 755 -d %{buildroot}/%{_mandir}/man1
install -m 755 -d %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 doc/build/man/lmishell.1 %{buildroot}/%{_mandir}/man1/lmishell.1
cp -r doc/build/html %{buildroot}/%{_docdir}/%{name}-%{version}

# completion for bash
bash_comp_dir=%{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 755 -d $bash_comp_dir
install -m 644 cli/completion/lmishell.bash $bash_comp_dir

# completion for zsh
zsh_comp_dir=%{buildroot}/%{_datadir}/zsh/site-functions
install -m 755 -d $zsh_comp_dir
install -m 644 cli/completion/_lmishell $zsh_comp_dir

%files
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/COPYING
%dir %{_docdir}/%{name}-%{version}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%dir %{_sysconfdir}/bash_completion.d/
%attr(755,root,root) %{_bindir}/lmishell
%{_mandir}/man1/lmishell.1.gz
%{_datadir}/zsh/site-functions/_lmishell
%{_sysconfdir}/bash_completion.d/lmishell.bash
%{python_sitelib}/lmi/shell/
%{python_sitelib}/openlmi_tools-*

%files doc
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/html

%changelog
* Thu Nov  7 2013 Peter Hatina <phatina@redhat.com> - 0.9-4
- fix instance comparision
- Resolves: #1027641

* Wed Nov  6 2013 Peter Hatina <phatina@redhat.com> - 0.9-3
- fix passing instance references to method call
- Resolves: #1027243

* Wed Nov  6 2013 Peter Hatina <phatina@redhat.com> - 0.9-2
- fix instance deletion
- Resolves: #1027223

* Mon Nov  4 2013 Peter Hatina <phatina@redhat.com> - 0.9-1
- upgrade to v0.9
- Related: #1021521

* Wed Oct 23 2013 Peter Hatina <phatina@redhat.com> - 0.8-1
- upgrade to v0.8
- Resolves: #1021521

* Mon Sep 16 2013 Peter Hatina <phatina@redhat.com> - 0.7-3
- fix passing method calls' arguments by dictionary
- Resolves: #1006220

* Tue Sep  3 2013 Peter Hatina <phatina@redhat.com> - 0.7-2
- fix cql query wrapping

* Fri Aug  9 2013 Peter Hatina <phatina@redhat.com> - 0.7-1
- upgrade to v0.7

* Wed Jul 31 2013 Peter Hatina <phatina@redhat.com> - 0.6-1
- upgrade to v0.6

* Mon Apr 29 2013 Peter Hatina <phatina@redhat.com> - 0.5-3
- remove sample scripts from the package

* Wed Feb 20 2013 Peter Hatina <phatina@redhat.com> - 0.5-2
- fix namespace handling

* Tue Feb 19 2013 Peter Hatina <phatina@redhat.com> - 0.5-1
- upgrade to v0.5

* Fri Feb 15 2013 Peter Hatina <phatina@redhat.com> - 0.4-1
- upgrade to v0.4

* Wed Feb 06 2013 Peter Hatina <phatina@redhat.com> - 0.3-1
- upgrade to v0.3

* Mon Nov 19 2012 Peter Hatina <phatina@redhat.com> - 0.2-1
- upgrade to v0.2

* Thu Oct 25 2012 Peter Hatina <phatina@redhat.com> - 0.1-5
- added python2-devel into BuildRequires

* Thu Oct 25 2012 Peter Hatina <phatina@redhat.com> - 0.1-4
- package renamed to openlmi-tools

* Sun Oct 07 2012 Peter Hatina <phatina@redhat.com> - 0.1-3
- added pywbem into Requires

* Sun Oct 07 2012 Peter Hatina <phatina@redhat.com> - 0.1-2
- removed python2 dependency
- fixed python_sitelib/fmci ownership
- fixed BuildRequires

* Sun Oct 07 2012 Peter Hatina <phatina@redhat.com> - 0.1-1
- initial import
