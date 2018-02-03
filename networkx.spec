#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : networkx
Version  : 2.1
Release  : 32
URL      : https://pypi.debian.net/networkx/networkx-2.1.zip
Source0  : https://pypi.debian.net/networkx/networkx-2.1.zip
Summary  : Python package for creating and manipulating graphs and networks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: networkx-legacypython
Requires: networkx-python3
Requires: networkx-data
Requires: networkx-python
Requires: decorator
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
%setup -q -n networkx-2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517685769
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1517685769
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
/usr/share/doc/networkx-2.1/LICENSE.txt
/usr/share/doc/networkx-2.1/examples/3d_drawing/__pycache__/mayavi2_spring.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/3d_drawing/mayavi2_spring.py
/usr/share/doc/networkx-2.1/examples/advanced/__pycache__/iterated_dynamical_systems.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/advanced/__pycache__/plot_eigenvalues.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/advanced/__pycache__/plot_heavy_metal_umlaut.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/advanced/__pycache__/plot_parallel_betweenness.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/advanced/iterated_dynamical_systems.py
/usr/share/doc/networkx-2.1/examples/advanced/plot_eigenvalues.py
/usr/share/doc/networkx-2.1/examples/advanced/plot_heavy_metal_umlaut.py
/usr/share/doc/networkx-2.1/examples/advanced/plot_parallel_betweenness.py
/usr/share/doc/networkx-2.1/examples/algorithms/__pycache__/beam_search.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/algorithms/__pycache__/plot_blockmodel.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/algorithms/__pycache__/plot_davis_club.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/algorithms/__pycache__/plot_krackhardt_centrality.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/algorithms/__pycache__/rcm.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/algorithms/beam_search.py
/usr/share/doc/networkx-2.1/examples/algorithms/hartford_drug.edgelist
/usr/share/doc/networkx-2.1/examples/algorithms/plot_blockmodel.py
/usr/share/doc/networkx-2.1/examples/algorithms/plot_davis_club.py
/usr/share/doc/networkx-2.1/examples/algorithms/plot_krackhardt_centrality.py
/usr/share/doc/networkx-2.1/examples/algorithms/rcm.py
/usr/share/doc/networkx-2.1/examples/basic/__pycache__/plot_properties.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/basic/__pycache__/plot_read_write.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/basic/plot_properties.py
/usr/share/doc/networkx-2.1/examples/basic/plot_read_write.py
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_atlas.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_chess_masters.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_circular_tree.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_degree_histogram.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_degree_rank.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_directed.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_edge_colormap.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_ego_graph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_four_grids.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_giant_component.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_house_with_colors.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_knuth_miles.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_labels_and_colors.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_lanl_routes.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_node_colormap.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_random_geometric_graph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_sampson.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_simple_path.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_spectral_grid.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_unix_email.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/__pycache__/plot_weighted_graph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/drawing/chess_masters_WCC.pgn.bz2
/usr/share/doc/networkx-2.1/examples/drawing/knuth_miles.txt.gz
/usr/share/doc/networkx-2.1/examples/drawing/lanl_routes.edgelist
/usr/share/doc/networkx-2.1/examples/drawing/plot_atlas.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_chess_masters.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_circular_tree.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_degree_histogram.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_degree_rank.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_directed.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_edge_colormap.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_ego_graph.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_four_grids.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_giant_component.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_house_with_colors.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_knuth_miles.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_labels_and_colors.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_lanl_routes.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_node_colormap.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_random_geometric_graph.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_sampson.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_simple_path.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_spectral_grid.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_unix_email.py
/usr/share/doc/networkx-2.1/examples/drawing/plot_weighted_graph.py
/usr/share/doc/networkx-2.1/examples/drawing/unix_email.mbox
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/atlas2.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/expected_degree_sequence.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_degree_sequence.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_erdos_renyi.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_football.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_karate_club.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_napoleon_russian_campaign.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/plot_roget.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/__pycache__/words.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/graph/atlas2.py
/usr/share/doc/networkx-2.1/examples/graph/expected_degree_sequence.py
/usr/share/doc/networkx-2.1/examples/graph/plot_degree_sequence.py
/usr/share/doc/networkx-2.1/examples/graph/plot_erdos_renyi.py
/usr/share/doc/networkx-2.1/examples/graph/plot_football.py
/usr/share/doc/networkx-2.1/examples/graph/plot_karate_club.py
/usr/share/doc/networkx-2.1/examples/graph/plot_napoleon_russian_campaign.py
/usr/share/doc/networkx-2.1/examples/graph/plot_roget.py
/usr/share/doc/networkx-2.1/examples/graph/roget_dat.txt.gz
/usr/share/doc/networkx-2.1/examples/graph/words.py
/usr/share/doc/networkx-2.1/examples/graph/words_dat.txt.gz
/usr/share/doc/networkx-2.1/examples/javascript/__pycache__/force.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/javascript/force.py
/usr/share/doc/networkx-2.1/examples/jit/__pycache__/plot_rgraph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/jit/plot_rgraph.py
/usr/share/doc/networkx-2.1/examples/pygraphviz/__pycache__/pygraphviz_attributes.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/pygraphviz/__pycache__/pygraphviz_draw.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/pygraphviz/__pycache__/pygraphviz_simple.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/pygraphviz/__pycache__/write_dotfile.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/pygraphviz/pygraphviz_attributes.py
/usr/share/doc/networkx-2.1/examples/pygraphviz/pygraphviz_draw.py
/usr/share/doc/networkx-2.1/examples/pygraphviz/pygraphviz_simple.py
/usr/share/doc/networkx-2.1/examples/pygraphviz/write_dotfile.py
/usr/share/doc/networkx-2.1/examples/subclass/__pycache__/plot_antigraph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/subclass/__pycache__/plot_printgraph.cpython-36.pyc
/usr/share/doc/networkx-2.1/examples/subclass/plot_antigraph.py
/usr/share/doc/networkx-2.1/examples/subclass/plot_printgraph.py
/usr/share/doc/networkx-2.1/requirements.txt

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
