%global tl_name tugboat-plain
%global tl_revision 75521

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.32
Release:	%{tl_revision}.1
Summary:	Plain TeX macros for TUGboat
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/tugboat
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for publication in
TUGboat.

