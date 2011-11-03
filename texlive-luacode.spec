# revision 22605
# category Package
# catalog-ctan /macros/luatex/latex/luacode
# catalog-date 2011-05-24 21:39:05 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-luacode
Version:	1.0
Release:	1
Summary:	Helper for executing lua code from within TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luacode
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Executing Lua code from within TeX with directlua can sometimes
be tricky: there is no easy way to use the percent character,
counting backslashes may be hard, and Lua comments don't work
the way you expect. The package provides the \luaexec command
and the luacode(*) environments to help with these problems.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
