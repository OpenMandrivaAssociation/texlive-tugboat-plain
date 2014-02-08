# revision 26611
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-tugboat-plain
Version:	20120809
Release:	2
Summary:	TeXLive tugboat-plain package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat-plain.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive tugboat-plain package.

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


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813132
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.18-2
+ Revision: 757156
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.18-1
+ Revision: 719815
- texlive-tugboat-plain
- texlive-tugboat-plain
- texlive-tugboat-plain

