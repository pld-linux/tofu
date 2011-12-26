%include        /usr/lib/rpm/macros.perl
Summary:	Tofu provides an easy, very lightweight, and effiscient way to manage your todo list(s)
Summary(hu.UTF-8):	Tofu egy könnyű, nagyon gyors utat biztosít a teendőid listáinak kezeléséhez
Name:		tofu
Version:	3.5
Release:	0.1
License:	MIT/X11
Group:		Development/Tools
Source0:	http://requiescant.tuxfamily.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	a09d9b2d9527d5baf76d69415210b45f
URL:		http://requiescant.tuxfamily.org/tofu/index.html
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tofu provides an easy, very lightweight, and effiscient way to manage
your todo list(s).

%description -l hu.UTF-8
Tofu egy könnyű, nagyon gyors utat biztosít a teendőid listáinak
kezeléséhez.

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' tofu tofuup

%build
./configure \
	--perl=%{__perl} \
	--prefix=%{_prefix} \
	--docdir=%{_docdir}/%{name}-%{version} \
	--mandir=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/tofu
%attr(755,root,root) %{_bindir}/tofuup
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
