#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : networkx
Version  : 2.6.2
Release  : 68
URL      : https://files.pythonhosted.org/packages/4b/3b/4378599026b81d1987a6e0d6d3d677e8f26308a039491a6b8a1914e58a4c/networkx-2.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/3b/4378599026b81d1987a6e0d6d3d677e8f26308a039491a6b8a1914e58a4c/networkx-2.6.2.tar.gz
Summary  : Python package for creating and manipulating graphs and networks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: networkx-license = %{version}-%{release}
Requires: networkx-python = %{version}-%{release}
Requires: networkx-python3 = %{version}-%{release}
Requires: black
Requires: matplotlib
Requires: numpy
Requires: pandas
Requires: scipy
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : scipy

%description
NetworkX
========
.. image:: https://github.com/networkx/networkx/workflows/test/badge.svg?tag=networkx-2.6.2
:target: https://github.com/networkx/networkx/actions?query=branch%3Anetworkx-2.6.2

%package doc
Summary: doc components for the networkx package.
Group: Documentation

%description doc
doc components for the networkx package.


%package license
Summary: license components for the networkx package.
Group: Default

%description license
license components for the networkx package.


%package python
Summary: python components for the networkx package.
Group: Default
Requires: networkx-python3 = %{version}-%{release}

%description python
python components for the networkx package.


%package python3
Summary: python3 components for the networkx package.
Group: Default
Requires: python3-core
Provides: pypi(networkx)

%description python3
python3 components for the networkx package.


%prep
%setup -q -n networkx-2.6.2
cd %{_builddir}/networkx-2.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627492883
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/networkx
cp %{_builddir}/networkx-2.6.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/networkx/83fa4c0e929ce0a6f16342a9297b5e8e1fdae429
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/networkx-2.6.2/LICENSE.txt
/usr/share/doc/networkx-2.6.2/examples/3d_drawing/README.txt
/usr/share/doc/networkx-2.6.2/examples/3d_drawing/mayavi2_spring.py
/usr/share/doc/networkx-2.6.2/examples/3d_drawing/plot_basic.py
/usr/share/doc/networkx-2.6.2/examples/README.txt
/usr/share/doc/networkx-2.6.2/examples/algorithms/README.txt
/usr/share/doc/networkx-2.6.2/examples/algorithms/WormNet.v3.benchmark.txt
/usr/share/doc/networkx-2.6.2/examples/algorithms/hartford_drug.edgelist
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_beam_search.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_betweenness_centrality.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_blockmodel.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_circuits.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_davis_club.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_dedensification.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_iterated_dynamical_systems.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_krackhardt_centrality.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_parallel_betweenness.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_rcm.py
/usr/share/doc/networkx-2.6.2/examples/algorithms/plot_snap.py
/usr/share/doc/networkx-2.6.2/examples/basic/README.txt
/usr/share/doc/networkx-2.6.2/examples/basic/plot_properties.py
/usr/share/doc/networkx-2.6.2/examples/basic/plot_read_write.py
/usr/share/doc/networkx-2.6.2/examples/basic/plot_simple_graph.py
/usr/share/doc/networkx-2.6.2/examples/drawing/README.txt
/usr/share/doc/networkx-2.6.2/examples/drawing/chess_masters_WCC.pgn.bz2
/usr/share/doc/networkx-2.6.2/examples/drawing/knuth_miles.txt.gz
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_chess_masters.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_custom_node_icons.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_degree.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_directed.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_edge_colormap.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_ego_graph.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_eigenvalues.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_four_grids.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_house_with_colors.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_knuth_miles.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_labels_and_colors.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_multipartite_graph.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_node_colormap.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_rainbow_coloring.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_random_geometric_graph.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_sampson.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_selfloops.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_simple_path.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_spectral_grid.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_unix_email.py
/usr/share/doc/networkx-2.6.2/examples/drawing/plot_weighted_graph.py
/usr/share/doc/networkx-2.6.2/examples/drawing/unix_email.mbox
/usr/share/doc/networkx-2.6.2/examples/graph/README.txt
/usr/share/doc/networkx-2.6.2/examples/graph/plot_degree_sequence.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_erdos_renyi.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_expected_degree_sequence.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_football.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_karate_club.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_napoleon_russian_campaign.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_roget.py
/usr/share/doc/networkx-2.6.2/examples/graph/plot_words.py
/usr/share/doc/networkx-2.6.2/examples/graph/roget_dat.txt.gz
/usr/share/doc/networkx-2.6.2/examples/graph/words_dat.txt.gz
/usr/share/doc/networkx-2.6.2/examples/subclass/README.txt
/usr/share/doc/networkx-2.6.2/examples/subclass/plot_antigraph.py
/usr/share/doc/networkx-2.6.2/examples/subclass/plot_printgraph.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/networkx/83fa4c0e929ce0a6f16342a9297b5e8e1fdae429

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
