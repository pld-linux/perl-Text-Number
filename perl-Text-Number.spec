%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Number
Summary:	Text::Number perl module
Summary(pl):	Modu� perla Text::Number
Name:		perl-Text-Number
Version:	0.80
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Number perl module.

%description -l pl
Modu� perla Text::Number.

%prep
%setup -q -n %{pnam}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Number.pm
%{_mandir}/man3/*
