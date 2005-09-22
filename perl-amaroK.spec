#
%include	/usr/lib/rpm/macros.perl
%define		pnam	amaroK
Summary:	amaroK - Module for controlling amaroK-player
Summary(pl):	amaroK - modu³ do sterowania odtwarzaczem amaroK
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

%description -l pl
Przy pomocy tego modu³u Perla mo¿na ³atwo pobieraæ informacje z
amaroKa i sterowaæ nim. Mo¿na pobieraæ informacje przy u¿yciu metody
get() i wykonywaæ polecenia przy u¿yciu metody command(). Przed
u¿yciem metody get() trzeba ustawiæ format wyj¶cia, co mo¿na zrobiæ
przy u¿yciu metody set().

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{perl_vendorlib}/%{pnam}.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pnam}.pm
