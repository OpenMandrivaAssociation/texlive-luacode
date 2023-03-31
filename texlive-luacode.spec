Name:		texlive-luacode
Version:	25193
Release:	2
Summary:	Helper for executing lua code from within TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luacode
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Executing Lua code from within TeX with directlua can sometimes
be tricky: there is no easy way to use the percent character,
counting backslashes may be hard, and Lua comments don't work
the way you expect. The package provides the \luaexec command
and the luacode(*) environments to help with these problems.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luacode/luacode.sty
%doc %{_texmfdistdir}/doc/lualatex/luacode/News
%doc %{_texmfdistdir}/doc/lualatex/luacode/README
%doc %{_texmfdistdir}/doc/lualatex/luacode/luacode.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/luacode/Makefile
%doc %{_texmfdistdir}/source/lualatex/luacode/luacode.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
