%global tl_name luacode
%global tl_revision 78415

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Helper for executing Lua code from within TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luacode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Executing Lua code from within TeX with directlua can sometimes be
tricky: there is no easy way to use the percent character, counting
backslashes may be hard, and Lua comments don't work the way you expect.
The package provides the \luaexec command and the luacode(*)
environments to help with these problems.

