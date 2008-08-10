Summary:	Source code browser for the Vim editor
Summary(pl.UTF-8):	Przeglądarka kodu źródłowego dla edytora Vim
Name:		vim-plugin-taglist
Version:	4.5
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	http://dl.sourceforge.net/vim-taglist/taglist_45.zip
# Source0-md5:	99b5366a64eea6092bb140df7d4c1a95
URL:		http://vim-taglist.sourceforge.net/
BuildRequires:	unzip
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
Requires:	ctags
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
The "Tag List" plugin is a source code browser for the Vim editor. It
provides an overview of the structure of source code files and allows
you to efficiently browse through source code files in different
programming languages. It is the top-rated and most-downloaded plugin
for the Vim editor.

%description -l pl.UTF-8
Wtyczka "Tag List" to przeglądarka kodu źródłowego dla edytora Vim.
Udostępnia widok struktury plików kodu źródłowego i umożliwia
efektywne przeglądanie plików z kodem w różnych językach
programowania. Jest to jedna z najczęściej ściąganych wtyczek dla
Vima.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
if [ "$1" = 0 ]; then
	umask 022
	echo ':helptags %{_vimdatadir}/doc' | vim -e -s
fi

%files
%defattr(644,root,root,755)
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
