#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ddt
Version  : 1.1.1
Release  : 10
URL      : http://pypi.debian.net/ddt/ddt-1.1.1.tar.gz
Source0  : http://pypi.debian.net/ddt/ddt-1.1.1.tar.gz
Summary  : Data-Driven/Decorated Tests
Group    : Development/Tools
License  : MIT
Requires: ddt-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
[![Build Status](https://travis-ci.org/txels/ddt.svg)](https://travis-ci.org/txels/ddt)
[![Code Health](https://landscape.io/github/txels/ddt/master/landscape.svg)](https://landscape.io/github/txels/ddt/master)
<!-- [![Can I Use Python 3?](https://caniusepython3.com/project/ddt.svg)](https://caniusepython3.com/project/ddt) -->
[![codecov.io](https://codecov.io/github/txels/ddt/coverage.svg?branch=master)](https://codecov.io/github/txels/ddt)
[![Version](https://img.shields.io/pypi/v/ddt.svg)](https://pypi.python.org/pypi/ddt)
[![Downloads](https://img.shields.io/pypi/dm/ddt.svg)](https://pypi.python.org/pypi/ddt)

%package python
Summary: python components for the ddt package.
Group: Default

%description python
python components for the ddt package.


%prep
%setup -q -n ddt-1.1.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
