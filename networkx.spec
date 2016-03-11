#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : networkx
Version  : 1.11
Release  : 15
URL      : https://pypi.python.org/packages/source/n/networkx/networkx-1.11.tar.gz
Source0  : https://pypi.python.org/packages/source/n/networkx/networkx-1.11.tar.gz
Summary  : Python package for creating and manipulating graphs and networks
Group    : Development/Tools
License  : BSD-2-Clause
Requires: networkx-python
Requires: networkx-data
BuildRequires : decorator-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
NetworkX
--------
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package data
Summary: data components for the networkx package.
Group: Data

%description data
data components for the networkx package.


%package python
Summary: python components for the networkx package.
Group: Default
Requires: decorator-python

%description python
python components for the networkx package.


%prep
%setup -q -n networkx-1.11

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/doc/networkx-1.11/INSTALL.txt
/usr/share/doc/networkx-1.11/LICENSE.txt
/usr/share/doc/networkx-1.11/examples/3d_drawing/mayavi2_spring.py
/usr/share/doc/networkx-1.11/examples/3d_drawing/mayavi2_spring.pyc
/usr/share/doc/networkx-1.11/examples/3d_drawing/mayavi2_spring.pyo
/usr/share/doc/networkx-1.11/examples/advanced/eigenvalues.py
/usr/share/doc/networkx-1.11/examples/advanced/eigenvalues.pyc
/usr/share/doc/networkx-1.11/examples/advanced/eigenvalues.pyo
/usr/share/doc/networkx-1.11/examples/advanced/heavy_metal_umlaut.py
/usr/share/doc/networkx-1.11/examples/advanced/heavy_metal_umlaut.pyc
/usr/share/doc/networkx-1.11/examples/advanced/heavy_metal_umlaut.pyo
/usr/share/doc/networkx-1.11/examples/advanced/iterated_dynamical_systems.py
/usr/share/doc/networkx-1.11/examples/advanced/iterated_dynamical_systems.pyc
/usr/share/doc/networkx-1.11/examples/advanced/iterated_dynamical_systems.pyo
/usr/share/doc/networkx-1.11/examples/advanced/parallel_betweenness.py
/usr/share/doc/networkx-1.11/examples/advanced/parallel_betweenness.pyc
/usr/share/doc/networkx-1.11/examples/advanced/parallel_betweenness.pyo
/usr/share/doc/networkx-1.11/examples/algorithms/blockmodel.py
/usr/share/doc/networkx-1.11/examples/algorithms/blockmodel.pyc
/usr/share/doc/networkx-1.11/examples/algorithms/blockmodel.pyo
/usr/share/doc/networkx-1.11/examples/algorithms/davis_club.py
/usr/share/doc/networkx-1.11/examples/algorithms/davis_club.pyc
/usr/share/doc/networkx-1.11/examples/algorithms/davis_club.pyo
/usr/share/doc/networkx-1.11/examples/algorithms/hartford_drug.edgelist
/usr/share/doc/networkx-1.11/examples/algorithms/krackhardt_centrality.py
/usr/share/doc/networkx-1.11/examples/algorithms/krackhardt_centrality.pyc
/usr/share/doc/networkx-1.11/examples/algorithms/krackhardt_centrality.pyo
/usr/share/doc/networkx-1.11/examples/algorithms/rcm.py
/usr/share/doc/networkx-1.11/examples/algorithms/rcm.pyc
/usr/share/doc/networkx-1.11/examples/algorithms/rcm.pyo
/usr/share/doc/networkx-1.11/examples/basic/properties.py
/usr/share/doc/networkx-1.11/examples/basic/properties.pyc
/usr/share/doc/networkx-1.11/examples/basic/properties.pyo
/usr/share/doc/networkx-1.11/examples/basic/read_write.py
/usr/share/doc/networkx-1.11/examples/basic/read_write.pyc
/usr/share/doc/networkx-1.11/examples/basic/read_write.pyo
/usr/share/doc/networkx-1.11/examples/drawing/atlas.py
/usr/share/doc/networkx-1.11/examples/drawing/atlas.pyc
/usr/share/doc/networkx-1.11/examples/drawing/atlas.pyo
/usr/share/doc/networkx-1.11/examples/drawing/chess_masters.py
/usr/share/doc/networkx-1.11/examples/drawing/chess_masters.pyc
/usr/share/doc/networkx-1.11/examples/drawing/chess_masters.pyo
/usr/share/doc/networkx-1.11/examples/drawing/chess_masters_WCC.pgn.bz2
/usr/share/doc/networkx-1.11/examples/drawing/circular_tree.py
/usr/share/doc/networkx-1.11/examples/drawing/circular_tree.pyc
/usr/share/doc/networkx-1.11/examples/drawing/circular_tree.pyo
/usr/share/doc/networkx-1.11/examples/drawing/degree_histogram.py
/usr/share/doc/networkx-1.11/examples/drawing/degree_histogram.pyc
/usr/share/doc/networkx-1.11/examples/drawing/degree_histogram.pyo
/usr/share/doc/networkx-1.11/examples/drawing/edge_colormap.py
/usr/share/doc/networkx-1.11/examples/drawing/edge_colormap.pyc
/usr/share/doc/networkx-1.11/examples/drawing/edge_colormap.pyo
/usr/share/doc/networkx-1.11/examples/drawing/ego_graph.py
/usr/share/doc/networkx-1.11/examples/drawing/ego_graph.pyc
/usr/share/doc/networkx-1.11/examples/drawing/ego_graph.pyo
/usr/share/doc/networkx-1.11/examples/drawing/four_grids.py
/usr/share/doc/networkx-1.11/examples/drawing/four_grids.pyc
/usr/share/doc/networkx-1.11/examples/drawing/four_grids.pyo
/usr/share/doc/networkx-1.11/examples/drawing/giant_component.py
/usr/share/doc/networkx-1.11/examples/drawing/giant_component.pyc
/usr/share/doc/networkx-1.11/examples/drawing/giant_component.pyo
/usr/share/doc/networkx-1.11/examples/drawing/house_with_colors.py
/usr/share/doc/networkx-1.11/examples/drawing/house_with_colors.pyc
/usr/share/doc/networkx-1.11/examples/drawing/house_with_colors.pyo
/usr/share/doc/networkx-1.11/examples/drawing/knuth_miles.py
/usr/share/doc/networkx-1.11/examples/drawing/knuth_miles.pyc
/usr/share/doc/networkx-1.11/examples/drawing/knuth_miles.pyo
/usr/share/doc/networkx-1.11/examples/drawing/knuth_miles.txt.gz
/usr/share/doc/networkx-1.11/examples/drawing/labels_and_colors.py
/usr/share/doc/networkx-1.11/examples/drawing/labels_and_colors.pyc
/usr/share/doc/networkx-1.11/examples/drawing/labels_and_colors.pyo
/usr/share/doc/networkx-1.11/examples/drawing/lanl_routes.edgelist
/usr/share/doc/networkx-1.11/examples/drawing/lanl_routes.py
/usr/share/doc/networkx-1.11/examples/drawing/lanl_routes.pyc
/usr/share/doc/networkx-1.11/examples/drawing/lanl_routes.pyo
/usr/share/doc/networkx-1.11/examples/drawing/node_colormap.py
/usr/share/doc/networkx-1.11/examples/drawing/node_colormap.pyc
/usr/share/doc/networkx-1.11/examples/drawing/node_colormap.pyo
/usr/share/doc/networkx-1.11/examples/drawing/random_geometric_graph.py
/usr/share/doc/networkx-1.11/examples/drawing/random_geometric_graph.pyc
/usr/share/doc/networkx-1.11/examples/drawing/random_geometric_graph.pyo
/usr/share/doc/networkx-1.11/examples/drawing/sampson.py
/usr/share/doc/networkx-1.11/examples/drawing/sampson.pyc
/usr/share/doc/networkx-1.11/examples/drawing/sampson.pyo
/usr/share/doc/networkx-1.11/examples/drawing/simple_path.py
/usr/share/doc/networkx-1.11/examples/drawing/simple_path.pyc
/usr/share/doc/networkx-1.11/examples/drawing/simple_path.pyo
/usr/share/doc/networkx-1.11/examples/drawing/unix_email.mbox
/usr/share/doc/networkx-1.11/examples/drawing/unix_email.py
/usr/share/doc/networkx-1.11/examples/drawing/unix_email.pyc
/usr/share/doc/networkx-1.11/examples/drawing/unix_email.pyo
/usr/share/doc/networkx-1.11/examples/drawing/weighted_graph.py
/usr/share/doc/networkx-1.11/examples/drawing/weighted_graph.pyc
/usr/share/doc/networkx-1.11/examples/drawing/weighted_graph.pyo
/usr/share/doc/networkx-1.11/examples/graph/atlas.py
/usr/share/doc/networkx-1.11/examples/graph/atlas.pyc
/usr/share/doc/networkx-1.11/examples/graph/atlas.pyo
/usr/share/doc/networkx-1.11/examples/graph/atlas2.py
/usr/share/doc/networkx-1.11/examples/graph/atlas2.pyc
/usr/share/doc/networkx-1.11/examples/graph/atlas2.pyo
/usr/share/doc/networkx-1.11/examples/graph/degree_sequence.py
/usr/share/doc/networkx-1.11/examples/graph/degree_sequence.pyc
/usr/share/doc/networkx-1.11/examples/graph/degree_sequence.pyo
/usr/share/doc/networkx-1.11/examples/graph/erdos_renyi.py
/usr/share/doc/networkx-1.11/examples/graph/erdos_renyi.pyc
/usr/share/doc/networkx-1.11/examples/graph/erdos_renyi.pyo
/usr/share/doc/networkx-1.11/examples/graph/expected_degree_sequence.py
/usr/share/doc/networkx-1.11/examples/graph/expected_degree_sequence.pyc
/usr/share/doc/networkx-1.11/examples/graph/expected_degree_sequence.pyo
/usr/share/doc/networkx-1.11/examples/graph/football.py
/usr/share/doc/networkx-1.11/examples/graph/football.pyc
/usr/share/doc/networkx-1.11/examples/graph/football.pyo
/usr/share/doc/networkx-1.11/examples/graph/karate_club.py
/usr/share/doc/networkx-1.11/examples/graph/karate_club.pyc
/usr/share/doc/networkx-1.11/examples/graph/karate_club.pyo
/usr/share/doc/networkx-1.11/examples/graph/knuth_miles.py
/usr/share/doc/networkx-1.11/examples/graph/knuth_miles.pyc
/usr/share/doc/networkx-1.11/examples/graph/knuth_miles.pyo
/usr/share/doc/networkx-1.11/examples/graph/knuth_miles.txt.gz
/usr/share/doc/networkx-1.11/examples/graph/napoleon_russian_campaign.py
/usr/share/doc/networkx-1.11/examples/graph/napoleon_russian_campaign.pyc
/usr/share/doc/networkx-1.11/examples/graph/napoleon_russian_campaign.pyo
/usr/share/doc/networkx-1.11/examples/graph/roget.py
/usr/share/doc/networkx-1.11/examples/graph/roget.pyc
/usr/share/doc/networkx-1.11/examples/graph/roget.pyo
/usr/share/doc/networkx-1.11/examples/graph/roget_dat.txt.gz
/usr/share/doc/networkx-1.11/examples/graph/unix_email.mbox
/usr/share/doc/networkx-1.11/examples/graph/unix_email.py
/usr/share/doc/networkx-1.11/examples/graph/unix_email.pyc
/usr/share/doc/networkx-1.11/examples/graph/unix_email.pyo
/usr/share/doc/networkx-1.11/examples/graph/words.py
/usr/share/doc/networkx-1.11/examples/graph/words.pyc
/usr/share/doc/networkx-1.11/examples/graph/words.pyo
/usr/share/doc/networkx-1.11/examples/graph/words_dat.txt.gz
/usr/share/doc/networkx-1.11/examples/multigraph/chess_masters.py
/usr/share/doc/networkx-1.11/examples/multigraph/chess_masters.pyc
/usr/share/doc/networkx-1.11/examples/multigraph/chess_masters.pyo
/usr/share/doc/networkx-1.11/examples/multigraph/chess_masters_WCC.pgn.bz2
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_attributes.py
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_attributes.pyc
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_attributes.pyo
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_draw.py
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_draw.pyc
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_draw.pyo
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_simple.py
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_simple.pyc
/usr/share/doc/networkx-1.11/examples/pygraphviz/pygraphviz_simple.pyo
/usr/share/doc/networkx-1.11/examples/pygraphviz/write_dotfile.py
/usr/share/doc/networkx-1.11/examples/pygraphviz/write_dotfile.pyc
/usr/share/doc/networkx-1.11/examples/pygraphviz/write_dotfile.pyo

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
