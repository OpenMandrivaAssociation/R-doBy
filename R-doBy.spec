%global packname  doBy
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.5.2
Release:          1
Summary:          doBy - Groupwise summary statistics, general linear contrasts, population means (least-squares-means), and other utilities
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-survival R-R2HTML R-multcomp R-lme4 R-snow R-MASS 
Requires:         R-Matrix 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-survival R-R2HTML R-multcomp R-lme4 R-snow R-MASS
BuildRequires:    R-Matrix 

%description
doBy contains a variety of utilities including: 1) Facilities for
groupwise computations of summary statistics and other facilities for
working with grouped data. 2) General linear contrasts and LSMEANS
(least-squares-means also known as population means), 3) Rscript2HTML for
autmatic generation of HTML file from R-script with a minimum of markup,
4) other utilities. doBy originally contained facilities for 'doing
something to data where data would be partitioned by some variables which
define groupings of data' - hence the name doBy.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/HTMLreport
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
