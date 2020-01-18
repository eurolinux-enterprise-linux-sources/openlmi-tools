Name:           openlmi-tools
Version:        0.9
Release:        22%{?dist}
Summary:        Set of CLI tools for Openlmi providers

License:        GPLv2+
URL:            http://fedorahosted.org/openlmi
Source0:        http://fedorahosted.org/released/openlmi-tools/%{name}-%{version}.tar.gz
Patch0:         openlmi-tools-01-fix-instance-deletion.patch
Patch1:         openlmi-tools-02-fix-passing-instances-to-method-call.patch
Patch2:         openlmi-tools-03-fix-instance-comparision.patch
Patch3:         openlmi-tools-04-fix-passing-method-params.patch
Patch4:         openlmi-tools-05-fix-log-messages-connect.patch
Patch5:         openlmi-tools-06-fix-unify-lmishell-naming.patch
Patch6:         openlmi-tools-07-fix-interactive-connect.patch
Patch7:         openlmi-tools-08-fix-compulsory-call-order-listener.patch
Patch8:         openlmi-tools-09-fix-blocking-when-receiving-indication.patch
Patch9:         openlmi-tools-10-fix-indication-unique-name.patch
Patch10:        openlmi-tools-11-update-documentation.patch
Patch11:        openlmi-tools-12-simplify-indication-subscription.patch
Patch12:        openlmi-tools-13-fix-certificate-subject-validation.patch
Patch13:        openlmi-tools-14-drop-verification-callback.patch
Patch14:        openlmi-tools-15-instances-client-filtering.patch
Patch15:        openlmi-tools-16-fix-local-imports.patch
Patch16:        openlmi-tools-17-fix-inverse-constant-values.patch
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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

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
* Thu Mar  6 2014 Peter Hatina <phatina@redhat.com> - 0.9-22
- fix inverse constant values
- Resolves: #1073423

* Thu Mar  6 2014 Peter Hatina <phatina@redhat.com> - 0.9-21
- CWD is by default appended in search path
- introduced CLI option --cwd-first-in-path which prepends
  CWD in search path
- Related: #1072252

* Tue Mar  4 2014 Peter Hatina <phatina@redhat.com> - 0.9-20
- allow local imports in lmishell
- Resolves: #1072252

* Fri Feb 21 2014 Peter Hatina <phatina@redhat.com> - 0.9-19
- introduce client-side instance filtering
- Resolves: #1067433

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9-18
- Mass rebuild 2013-12-27

* Wed Dec 18 2013 Peter Hatina <phatina@redhat.com> - 0.9-17
- drop certificate verification callback; all the checks are
  done in pywbem
- Related: #1041548

* Fri Dec 13 2013 Peter Hatina <phatina@redhat.com> - 0.9-16
- fix certificate subject validation
- Resolves: #1041548

* Mon Dec  9 2013 Peter Hatina <phatina@redhat.com> - 0.9-15
- simplify indication subscription
- Resolves: #1039573

* Mon Dec  9 2013 Peter Hatina <phatina@redhat.com> - 0.9-14
- fix documentation version
- Related: #1039494

* Mon Dec  9 2013 Peter Hatina <phatina@redhat.com> - 0.9-13
- update documentation
- Resolves: #1039494

* Fri Dec  6 2013 Peter Hatina <phatina@redhat.com> - 0.9-12
- fix indication unique name
- Resolves: #1039032

* Fri Dec  6 2013 Peter Hatina <phatina@redhat.com> - 0.9-11
- fix blocking timeout when receiving indication
- Resolves: #1038996

* Wed Dec  4 2013 Peter Hatina <phatina@redhat.com> - 0.9-10
- fix compulsory call order of LMIIndicationListener methods
- Resolves: #1038032

* Tue Dec  3 2013 Peter Hatina <phatina@redhat.com> - 0.9-9
- fix interactive connect when run with -i
- Resolves: #1036722

* Tue Dec  3 2013 Peter Hatina <phatina@redhat.com> - 0.9-8
- unify LMIShell naming
- Resolves: #1036714

* Mon Dec  2 2013 Peter Hatina <phatina@redhat.com> - 0.9-7
- fix missing log messages in connect()
- Resolves: #1036535

* Mon Nov 18 2013 Peter Hatina <phatina@redhat.com> - 0.9-6
- fix passing parameters to method calls
- Resolves: #1030927

* Wed Nov 13 2013 Peter Hatina <phatina@redhat.com> - 0.9-5
- allow instance comparision to any other type
- Resolves: #1029537

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
