python make_fields_list.py

pushd plots
rm *.png *.html
python plot_all_plotly.py
popd

pushd datarst
rm *.rst
python make_rst_files.py
popd

