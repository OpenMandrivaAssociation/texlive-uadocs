# revision 31042
# category Package
# catalog-ctan /macros/latex/contrib/uadocs
# catalog-date 2013-06-19 11:29:28 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-uadocs
Version:	1.1
Release:	6
Summary:	Course texts and masters theses in University of Antwerp style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uadocs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uadocs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uadocs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uadocs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These class files implement the house style of the University
of Antwerp for course texts and master theses. Using these
class files will make it easy for you to make and keep your
documents compliant to this version and future versions of the
house style of the University of Antwerp.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uadocs/ua_color.eps
%{_texmfdistdir}/tex/latex/uadocs/ua_color.pdf
%{_texmfdistdir}/tex/latex/uadocs/uacoursetext.cls
%{_texmfdistdir}/tex/latex/uadocs/uamasterthesis.cls
%doc %{_texmfdistdir}/doc/latex/uadocs/LICENSE
%doc %{_texmfdistdir}/doc/latex/uadocs/uacoursetext-example.pdf
%doc %{_texmfdistdir}/doc/latex/uadocs/uacoursetext-example.tex
%doc %{_texmfdistdir}/doc/latex/uadocs/uadocs.pdf
%doc %{_texmfdistdir}/doc/latex/uadocs/uamasterthesis-example.pdf
%doc %{_texmfdistdir}/doc/latex/uadocs/uamasterthesis-example.tex
#- source
%doc %{_texmfdistdir}/source/latex/uadocs/uadocs.dtx
%doc %{_texmfdistdir}/source/latex/uadocs/uadocs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
