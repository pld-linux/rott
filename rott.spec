#
# Choose build for game data type by defining:
# product SHAREWARE	- shareware version (default)
# product REGISTERED	- registered version
# product ROTTSUPER	- ROTT Super-CD
# product SITELICENSE	- ROTT Site License
#
%{!?product:%define	product	SHAREWARE}
Summary:	Rise of the Triad game
Summary(pl.UTF-8):   Gra Rise of the Triad
Name:		rott
Version:	1.0
Release:	1
License:	GPL (program only)
Group:		Applications/Games
Source0:	http://icculus.org/rott/releases/%{name}-%{version}.tar.gz
# Source0-md5:	c1c6cbecf00f2229cf2e0053334dcfc1
Patch0:		%{name}-version.patch
URL:		http://icculus.org/rott/
BuildRequires:	SDL_mixer-devel
Provides:	rott(%{product})
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rise of the Triad game.

%description -l pl.UTF-8
Gra Rise of the Triad.

%prep
%setup -q
%patch0 -p1

%build
cd rott
%{__make} \
	EXTRACFLAGS="%{rpmcflags} -DUSE_EXECINFO=1 -D%{product}=1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rott/rott $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README readme.txt rott/13todo.txt
%attr(755,root,root) %{_bindir}/*
