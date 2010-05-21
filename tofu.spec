Summary:	Tofu provides an easy, very lightweight, and effiscient way to manage your todo list(s)
Summary(hu.UTF-8):	Tofu egy könnyű, nagyon gyors utat biztosít a teendőid listáinak kezeléséhez
Name:		tofu
Version:	3.0
Release:	0.1
License:	MIT/X11
Group:		Development/Tools
Source0:	http://requiescant.tuxfamily.org/tofu/%{name}-%{version}.tar.gz
# Source0-md5:	8c6f71c31a269cf75c6fc8f483ff79c0
URL:		http://requiescant.tuxfamily.org/tofu/index.html
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Tofu provides an easy, very lightweight, and effiscient way to manage
your todo list(s).

%description -l hu.UTF-8
Tofu egy könnyű, nagyon gyors utat biztosít a teendőid listáinak
kezeléséhez.

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' tofu

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tofu*
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
