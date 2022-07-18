python make_fields_list.py

pushd plots
rm *.png
python plot_all.py
popd

pushd datarst
rm *.rst
python make_rst_files.py
popd

