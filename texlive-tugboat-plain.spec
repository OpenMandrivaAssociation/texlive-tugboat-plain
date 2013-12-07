# revision 31340
# category Package
# catalog-ctan /macros/plain/contrib/tugboat
# catalog-date 2013-08-03 12:08:10 +0200
# catalog-license other-free
# catalog-version 1.21
Name:		texlive-tugboat-plain
Epoch:		1
Version:	1.21
Release:	4
Summary:	Plain TeX macros for TUGboat
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/tugboat
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for
publication in TUGboat.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.cmn
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.sty
%{_texmfdistdir}/tex/plain/tugboat-plain/tugproc.sty
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/README
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.pdf
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
