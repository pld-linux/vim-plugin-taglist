Summary:	Source code browser for the Vim editor
Summary(pl):	Przegl�darka kodu �r�d�owego dla edytora Vim
Name:		vim-plugin-taglist
Version:	4.0
Release:	0.b1.3
License:	GPL
Group:		Applications/Editors/Vim
Source0:	http://www.geocities.com/yegappan/taglist/taglist_40b1.zip
# Source0-md5:	5624b94870461bb2971130ed34aa7386
URL:		http://www.geocities.com/yegappan/taglist/
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
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

%description -l pl
Wtyczka "Tag List" to przegl�darka kodu �r�d�owego dla edytora Vim.
Udost�pnia widok struktury plik�w kodu �r�d�owego i umo�liwia
efektywne przegl�danie plik�w z kodem w r�nych j�zykach
programowania. Jest to jedna z najcz�ciej �ci�ganych wtyczek dla
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
