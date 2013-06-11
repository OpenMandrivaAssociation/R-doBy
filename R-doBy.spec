%global packname  doBy
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          4.5.6
Release:          1
Summary:          Groupwise summary statistics, general linear contrasts, population means, etc
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/doBy_4.5-6.tar.gz
Requires:         R-survival R-R2HTML R-multcomp R-lme4 R-snow R-MASS
Requires:         R-Matrix
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-survival
BuildRequires:    R-R2HTML R-multcomp R-lme4 R-snow R-MASS R-Matrix

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
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
