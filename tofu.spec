Summary:	Tofu provides an easy, very lightweight, and effiscient way to manage your todo list(s)
Summary(hu.UTF-8):	Tofu egy könnyű, nagyon gyors utat biztosít a teendőid listáinak kezeléséhez
Name:		tofu
Version:	2.5
Release:	0.1
License:	MIT/X11
Group:		Development/Tools
Source0:	http://requiescant.tuxfamily.org/tofu/%{name}-%{version}.tar.gz
# Source0-md5:	18dbd1854411f929ea6eb53dceaaab52
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install tofu $RPM_BUILD_ROOT%{_bindir}
cp -a share/tofu.1 $RPM_BUILD_ROOT%{_mandir}/man1
%{__perl} playground.pl -root=$RPM_BUILD_ROOT%{_examplesdir}/%{name} playground

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG PLAY playground.pl
%attr(755,root,root) %{_bindir}/tofu
%{_mandir}/man1/tofu.1*
%{_examplesdir}/%{name}
