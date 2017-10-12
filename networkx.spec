#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : networkx
Version  : 2.0
Release  : 26
URL      : https://pypi.debian.net/networkx/networkx-2.0.zip
Source0  : https://pypi.debian.net/networkx/networkx-2.0.zip
Summary  : Python package for creating and manipulating graphs and networks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: networkx-legacypython
Requires: networkx-python3
Requires: networkx-data
Requires: networkx-python
Requires: decorator
Requires: lxml
Requires: matplotlib
Requires: numpy
Requires: pandas
Requires: pydot
Requires: scipy
BuildRequires : decorator
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
NetworkX is a Python package for the creation, manipulation, and
        study of the structure, dynamics, and functions of complex networks.

%package data
Summary: data components for the networkx package.
Group: Data

%description data
data components for the networkx package.


%package legacypython
Summary: legacypython components for the networkx package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the networkx package.


%package python
Summary: python components for the networkx package.
Group: Default
Requires: networkx-legacypython
Requires: networkx-python3

%description python
python components for the networkx package.


%package python3
Summary: python3 components for the networkx package.
Group: Default
Requires: python3-core

%description python3
python3 components for the networkx package.


%prep
%setup -q -n networkx-2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507834357
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507834357
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/doc/networkx-2.0/LICENSE.txt
/usr/share/doc/networkx-2.0/examples/3d_drawing/mayavi2_spring.py
/usr/share/doc/networkx-2.0/examples/3d_drawing/mayavi2_spring.pyc
/usr/share/doc/networkx-2.0/examples/advanced/iterated_dynamical_systems.py
/usr/share/doc/networkx-2.0/examples/advanced/iterated_dynamical_systems.pyc
/usr/share/doc/networkx-2.0/examples/advanced/plot_eigenvalues.py
/usr/share/doc/networkx-2.0/examples/advanced/plot_eigenvalues.pyc
/usr/share/doc/networkx-2.0/examples/advanced/plot_heavy_metal_umlaut.py
/usr/share/doc/networkx-2.0/examples/advanced/plot_heavy_metal_umlaut.pyc
/usr/share/doc/networkx-2.0/examples/advanced/plot_parallel_betweenness.py
/usr/share/doc/networkx-2.0/examples/advanced/plot_parallel_betweenness.pyc
/usr/share/doc/networkx-2.0/examples/algorithms/beam_search.py
/usr/share/doc/networkx-2.0/examples/algorithms/beam_search.pyc
/usr/share/doc/networkx-2.0/examples/algorithms/hartford_drug.edgelist
/usr/share/doc/networkx-2.0/examples/algorithms/plot_blockmodel.py
/usr/share/doc/networkx-2.0/examples/algorithms/plot_blockmodel.pyc
/usr/share/doc/networkx-2.0/examples/algorithms/plot_davis_club.py
/usr/share/doc/networkx-2.0/examples/algorithms/plot_davis_club.pyc
/usr/share/doc/networkx-2.0/examples/algorithms/plot_krackhardt_centrality.py
/usr/share/doc/networkx-2.0/examples/algorithms/plot_krackhardt_centrality.pyc
/usr/share/doc/networkx-2.0/examples/algorithms/rcm.py
/usr/share/doc/networkx-2.0/examples/algorithms/rcm.pyc
/usr/share/doc/networkx-2.0/examples/basic/plot_properties.py
/usr/share/doc/networkx-2.0/examples/basic/plot_properties.pyc
/usr/share/doc/networkx-2.0/examples/basic/plot_read_write.py
/usr/share/doc/networkx-2.0/examples/basic/plot_read_write.pyc
/usr/share/doc/networkx-2.0/examples/drawing/chess_masters_WCC.pgn.bz2
/usr/share/doc/networkx-2.0/examples/drawing/knuth_miles.txt.gz
/usr/share/doc/networkx-2.0/examples/drawing/lanl_routes.edgelist
/usr/share/doc/networkx-2.0/examples/drawing/plot_atlas.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_atlas.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_chess_masters.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_chess_masters.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_circular_tree.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_circular_tree.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_degree_histogram.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_degree_histogram.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_degree_rank.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_degree_rank.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_edge_colormap.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_edge_colormap.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_ego_graph.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_ego_graph.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_four_grids.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_four_grids.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_giant_component.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_giant_component.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_house_with_colors.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_house_with_colors.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_knuth_miles.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_knuth_miles.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_labels_and_colors.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_labels_and_colors.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_lanl_routes.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_lanl_routes.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_node_colormap.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_node_colormap.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_random_geometric_graph.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_random_geometric_graph.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_sampson.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_sampson.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_simple_path.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_simple_path.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_unix_email.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_unix_email.pyc
/usr/share/doc/networkx-2.0/examples/drawing/plot_weighted_graph.py
/usr/share/doc/networkx-2.0/examples/drawing/plot_weighted_graph.pyc
/usr/share/doc/networkx-2.0/examples/drawing/unix_email.mbox
/usr/share/doc/networkx-2.0/examples/graph/atlas2.py
/usr/share/doc/networkx-2.0/examples/graph/atlas2.pyc
/usr/share/doc/networkx-2.0/examples/graph/expected_degree_sequence.py
/usr/share/doc/networkx-2.0/examples/graph/expected_degree_sequence.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_degree_sequence.py
/usr/share/doc/networkx-2.0/examples/graph/plot_degree_sequence.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_erdos_renyi.py
/usr/share/doc/networkx-2.0/examples/graph/plot_erdos_renyi.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_football.py
/usr/share/doc/networkx-2.0/examples/graph/plot_football.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_karate_club.py
/usr/share/doc/networkx-2.0/examples/graph/plot_karate_club.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_napoleon_russian_campaign.py
/usr/share/doc/networkx-2.0/examples/graph/plot_napoleon_russian_campaign.pyc
/usr/share/doc/networkx-2.0/examples/graph/plot_roget.py
/usr/share/doc/networkx-2.0/examples/graph/plot_roget.pyc
/usr/share/doc/networkx-2.0/examples/graph/roget_dat.txt.gz
/usr/share/doc/networkx-2.0/examples/graph/words.py
/usr/share/doc/networkx-2.0/examples/graph/words.pyc
/usr/share/doc/networkx-2.0/examples/graph/words_dat.txt.gz
/usr/share/doc/networkx-2.0/examples/javascript/force.py
/usr/share/doc/networkx-2.0/examples/javascript/force.pyc
/usr/share/doc/networkx-2.0/examples/jit/plot_rgraph.py
/usr/share/doc/networkx-2.0/examples/jit/plot_rgraph.pyc
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_attributes.py
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_attributes.pyc
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_draw.py
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_draw.pyc
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_simple.py
/usr/share/doc/networkx-2.0/examples/pygraphviz/pygraphviz_simple.pyc
/usr/share/doc/networkx-2.0/examples/pygraphviz/write_dotfile.py
/usr/share/doc/networkx-2.0/examples/pygraphviz/write_dotfile.pyc
/usr/share/doc/networkx-2.0/examples/subclass/plot_antigraph.py
/usr/share/doc/networkx-2.0/examples/subclass/plot_antigraph.pyc
/usr/share/doc/networkx-2.0/examples/subclass/plot_printgraph.py
/usr/share/doc/networkx-2.0/examples/subclass/plot_printgraph.pyc
/usr/share/doc/networkx-2.0/requirements.txt

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
