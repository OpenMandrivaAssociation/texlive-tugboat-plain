# revision 21720
# category Package
# catalog-ctan /macros/plain/contrib/tugboat
# catalog-date 2011-03-12 15:13:24 +0100
# catalog-license other-free
# catalog-version 1.18
Name:		texlive-tugboat-plain
Version:	1.18
Release:	1
Summary:	Plain TeX macros for TUGboat
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/tugboat
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The macros defined in this directory (in files tugboat.sty and
tugboat.cmn) are used in papers written in Plain TeX for
publication in TUGboat.

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
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.cmn
%{_texmfdistdir}/tex/plain/tugboat-plain/tugboat.sty
%{_texmfdistdir}/tex/plain/tugboat-plain/tugproc.sty
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/README
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.pdf
%doc %{_texmfdistdir}/doc/plain/tugboat-plain/tubguide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
