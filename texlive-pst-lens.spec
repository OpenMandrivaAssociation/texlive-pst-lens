# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-lens
# catalog-date 2007-06-15 10:24:12 +0200
# catalog-license lppl
# catalog-version 1.02
Name:		texlive-pst-lens
Version:	1.02
Release:	8
Summary:	Lenses with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-lens
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PSTricks package provides a really rather simple command
\PstLens that will draw a lens. Command parameters provide a
remarkable range of effects.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-lens/pst-lens.tex
%{_texmfdistdir}/tex/latex/pst-lens/pst-lens.sty
%doc %{_texmfdistdir}/doc/generic/pst-lens/Changes
%doc %{_texmfdistdir}/doc/generic/pst-lens/README
%doc %{_texmfdistdir}/doc/generic/pst-lens/pst-lens.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-lens/pst-lens.dtx
%doc %{_texmfdistdir}/source/generic/pst-lens/pst-lens.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.02-2
+ Revision: 755321
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.02-1
+ Revision: 719365
- texlive-pst-lens
- texlive-pst-lens
- texlive-pst-lens
- texlive-pst-lens

