Name:		texlive-pst-lens
Version:	15878
Release:	2
Summary:	Lenses with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-lens
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lens.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
