#
%include	/usr/lib/rpm/macros.perl
%define		pnam	amaroK
Summary:	amaroK - Module for controlling amaroK-player
Summary(pl.UTF-8):   amaroK - moduł do sterowania odtwarzaczem amaroK
Name:		perl-amaroK
Version:	0
Release:	0.1
# same as perl ?
License:	GPL v1+ or Artistic
Vendor:		Markus "Linkku" Lindqvist <markus.lindqvist@gmail.com>
Group:		Development/Languages/Perl
Source0:	http://koti.mbnet.fi/linkku-/tuts/perl/amaroK/%{pnam}.pm
# Source0-md5:	3a47978ae362a15cc505ce9188dc7fbe
URL:		http://koti.mbnet.fi/linkku-/tuts/index.php?p=15
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this Perl-module you can easily get information from amaroK and
control amaroK. You can get information with get()-method and execute
commands with command()-method. Before you can use get()-method you
have to set the format for output, you can set it with set().

%description -l pl.UTF-8
Przy pomocy tego modułu Perla można łatwo pobierać informacje z
amaroKa i sterować nim. Można pobierać informacje przy użyciu metody
get() i wykonywać polecenia przy użyciu metody command(). Przed
użyciem metody get() trzeba ustawić format wyjścia, co można zrobić
przy użyciu metody set().

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{perl_vendorlib}/%{pnam}.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pnam}.pm
